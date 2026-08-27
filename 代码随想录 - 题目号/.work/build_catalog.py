#!/usr/bin/env python3
"""Build the ordered LeetCode workbook in Markdown and PDF.

The source-of-truth for ordering is the local ``代码随想录-Markdown`` folder.
Current official LeetCode metadata and statements are cached through the public
GraphQL endpoint so link-only recommendations still receive a complete entry.
"""

from __future__ import annotations

import argparse
import base64
import concurrent.futures
import hashlib
import html
import json
import re
import ssl
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import OrderedDict, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Iterable


WORK_DIR = Path(__file__).resolve().parent
TARGET_DIR = WORK_DIR.parent
REPO_DIR = TARGET_DIR.parent
SOURCE_DIR = REPO_DIR / "代码随想录-Markdown"
CACHE_DIR = WORK_DIR / "cache"
IMAGE_CACHE_DIR = CACHE_DIR / "images"
OUTPUT_MD = TARGET_DIR / "代码随想录-LeetCode题目册.md"
OUTPUT_PDF = TARGET_DIR / "代码随想录-LeetCode题目册.pdf"

CHAPTER_NAMES = {
    1: "数组",
    2: "链表",
    3: "哈希表",
    4: "字符串",
    5: "双指针",
    6: "栈与队列",
    7: "二叉树",
    8: "回溯算法",
    9: "贪心算法",
    10: "动态规划",
    11: "单调栈",
}

DIFFICULTY_ZH = {"Easy": "简单", "Medium": "中等", "Hard": "困难"}
LEGACY_DISPLAY_OVERRIDES: dict[str, dict[str, str]] = {
    "shun-shi-zhen-da-yin-ju-zhen-lcof": {
        "questionFrontendId": "剑指 Offer 29",
        "translatedTitle": "顺时针打印矩阵",
    },
    "ti-huan-kong-ge-lcof": {
        "questionFrontendId": "剑指 Offer 05",
        "translatedTitle": "替换空格",
        "translatedContent": (
            '<p>请实现一个函数，把字符串 <code>s</code> 中的每个空格替换成“%20”。</p>'
            '<p><strong>示例：</strong></p><pre>输入：s = "We are happy."\n'
            '输出："We%20are%20happy."</pre><p><strong>限制：</strong></p>'
            '<ul><li><code>0 &lt;= s.length &lt;= 10000</code></li></ul>'
        ),
    },
    "zuo-xuan-zhuan-zi-fu-chuan-lcof": {
        "questionFrontendId": "剑指 Offer 58-II",
        "translatedTitle": "左旋转字符串",
        "translatedContent": (
            '<p>字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。</p>'
            '<p>请定义一个函数实现字符串左旋转操作。给定字符串 <code>s</code> 和数字 '
            '<code>n</code>，返回左旋转 <code>n</code> 位得到的字符串。</p>'
            '<p><strong>示例 1：</strong></p><pre>输入：s = "abcdefg", n = 2\n输出："cdefgab"</pre>'
            '<p><strong>示例 2：</strong></p><pre>输入：s = "lrloseumgh", n = 6\n输出："umghlrlose"</pre>'
            '<p><strong>限制：</strong></p><ul><li><code>1 &lt;= n &lt; s.length &lt;= 10000</code></li></ul>'
        ),
    },
}
LEETCODE_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((https?://(?:www\.)?(?:leetcode\.cn|leetcode-cn\.com)"
    r"/problems/([^/?#)]+)(?:/[^)]*)?)\)",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")

GRAPHQL_QUERY = """
query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    translatedTitle
    title
    titleSlug
    translatedContent
    content
    difficulty
    isPaidOnly
  }
}
""".strip()


@dataclass
class Occurrence:
    chapter_no: int
    chapter_name: str
    source_file: str
    line: int
    label: str
    slug: str
    section: str
    kind: str


@dataclass
class Catalog:
    chapter_slugs: dict[int, list[str]] = field(default_factory=dict)
    occurrences: dict[str, list[Occurrence]] = field(default_factory=lambda: defaultdict(list))
    raw_link_count: int = 0

    @property
    def unique_slugs(self) -> list[str]:
        seen: set[str] = set()
        result: list[str] = []
        for chapter_no in range(1, 12):
            for slug in self.chapter_slugs[chapter_no]:
                if slug not in seen:
                    seen.add(slug)
                    result.append(slug)
        return result

    @property
    def chapter_entry_count(self) -> int:
        return sum(len(items) for items in self.chapter_slugs.values())


def source_files() -> list[tuple[int, Path]]:
    files: list[tuple[int, Path]] = []
    for path in SOURCE_DIR.glob("*.md"):
        match = re.match(r"^(\d+)\.", path.name)
        if not match:
            continue
        chapter_no = int(match.group(1))
        if 1 <= chapter_no <= 11:
            files.append((chapter_no, path))
    return sorted(files, key=lambda item: item[0])


def normalize_heading(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[*_`]+", "", value)
    return re.sub(r"\s+", " ", value).strip()


def classify_link(label: str, heading_path: list[str]) -> str:
    context = " / ".join(heading_path)
    if re.search(r"相关|推荐|类似", context):
        return "拓展/推荐"
    if re.search(r"力扣题目(?:链接|地址)", label):
        return "主讲题"
    if re.match(r"\s*(?:剑指\s*Offer|面试题|\d+)", label, re.IGNORECASE):
        return "章节题单"
    return "正文引用"


def canonicalize_slug(label: str, slug: str) -> str:
    slug = slug.strip().lower()
    # The source has two mislabeled links: label 637 points at LC 199.
    if re.search(r"(?:^|\D)637(?:\D|$)", label) and slug == "binary-tree-right-side-view":
        return "average-of-levels-in-binary-tree"
    return slug


def extract_catalog() -> Catalog:
    catalog = Catalog()
    for chapter_no, path in source_files():
        headings: list[str] = []
        seen_in_file: set[str] = set()
        ordered_slugs: list[str] = []
        in_fence = False
        fence_char = ""
        fence_len = 0
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_no, line in enumerate(lines, start=1):
            fence_match = FENCE_RE.match(line)
            if fence_match:
                token = fence_match.group(1)
                if not in_fence:
                    in_fence = True
                    fence_char = token[0]
                    fence_len = len(token)
                elif token[0] == fence_char and len(token) >= fence_len:
                    in_fence = False
                    fence_char = ""
                    fence_len = 0
                continue
            if in_fence:
                continue

            heading_match = HEADING_RE.match(line)
            if heading_match:
                level = len(heading_match.group(1))
                title = normalize_heading(heading_match.group(2))
                headings = headings[: level - 1]
                while len(headings) < level - 1:
                    headings.append("")
                headings.append(title)

            for link_match in LEETCODE_LINK_RE.finditer(line):
                label, _url, raw_slug = link_match.groups()
                slug = canonicalize_slug(label, raw_slug)
                catalog.raw_link_count += 1
                section_parts = [part for part in headings if part]
                occurrence = Occurrence(
                    chapter_no=chapter_no,
                    chapter_name=CHAPTER_NAMES[chapter_no],
                    source_file=path.name,
                    line=line_no,
                    label=normalize_heading(label),
                    slug=slug,
                    section=" > ".join(section_parts) or "章节正文",
                    kind=classify_link(label, section_parts),
                )
                catalog.occurrences[slug].append(occurrence)
                if slug not in seen_in_file:
                    seen_in_file.add(slug)
                    ordered_slugs.append(slug)
        catalog.chapter_slugs[chapter_no] = ordered_slugs
    return catalog


def post_graphql(slug: str, attempts: int = 4) -> dict[str, Any]:
    payload = json.dumps(
        {"query": GRAPHQL_QUERY, "variables": {"titleSlug": slug}},
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://leetcode.cn/graphql/",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 Chrome/151 Safari/537.36",
            "Referer": f"https://leetcode.cn/problems/{slug}/",
        },
        method="POST",
    )
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            context = ssl.create_default_context()
            with urllib.request.urlopen(request, timeout=35, context=context) as response:
                body = json.loads(response.read().decode("utf-8"))
            question = (body.get("data") or {}).get("question")
            if not question:
                raise RuntimeError(f"GraphQL returned no question for {slug}: {body}")
            question["requestedSlug"] = slug
            return question
        except Exception as exc:  # noqa: BLE001 - retry network/API errors
            last_error = exc
            time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {slug}: {last_error}")


def fetch_questions(slugs: Iterable[str], refresh: bool = False) -> dict[str, dict[str, Any]]:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / "questions.json"
    cached: dict[str, dict[str, Any]] = {}
    if cache_path.exists() and not refresh:
        cached = json.loads(cache_path.read_text(encoding="utf-8"))

    wanted = list(slugs)
    missing = [slug for slug in wanted if slug not in cached]
    if missing:
        print(f"Fetching {len(missing)} LeetCode records...", flush=True)
        errors: list[str] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_map = {executor.submit(post_graphql, slug): slug for slug in missing}
            for index, future in enumerate(concurrent.futures.as_completed(future_map), start=1):
                slug = future_map[future]
                try:
                    cached[slug] = future.result()
                except Exception as exc:  # noqa: BLE001
                    errors.append(str(exc))
                if index % 20 == 0 or index == len(missing):
                    print(f"  fetched {index}/{len(missing)}", flush=True)
        if errors:
            raise RuntimeError("\n".join(errors))
        cache_path.write_text(
            json.dumps(cached, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    return {slug: cached[slug] for slug in wanted}


def apply_question_overrides(questions: dict[str, dict[str, Any]]) -> None:
    """Preserve the legacy Offer numbering and wording used by the source book."""
    for slug, values in LEGACY_DISPLAY_OVERRIDES.items():
        if slug not in questions:
            continue
        questions[slug].update(values)


def load_insights(slugs: Iterable[str]) -> dict[str, dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for path in sorted(WORK_DIR.glob("insights_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise TypeError(f"{path} must contain a JSON object")
        for slug, record in data.items():
            required = {"core", "invariant", "complexity", "scope", "pitfall"}
            if set(record) != required:
                raise ValueError(f"{path}: {slug} fields must be exactly {sorted(required)}")
            if not isinstance(record["scope"], list) or not record["scope"]:
                raise ValueError(f"{path}: {slug}.scope must be a non-empty list")
            merged[slug] = record

    wanted = set(slugs)
    missing = sorted(wanted - set(merged))
    extra = sorted(set(merged) - wanted)
    if missing:
        raise ValueError(f"Missing insight records ({len(missing)}): {', '.join(missing)}")
    if extra:
        print(f"Warning: {len(extra)} unused insight records: {', '.join(extra)}", file=sys.stderr)
    return {slug: merged[slug] for slug in slugs}


def question_title(record: dict[str, Any]) -> str:
    return (record.get("translatedTitle") or record.get("title") or record["titleSlug"]).strip()


def question_id(record: dict[str, Any]) -> str:
    return str(record.get("questionFrontendId") or "未编号").strip()


def canonical_url(slug: str) -> str:
    return f"https://leetcode.cn/problems/{slug}/"


def normalize_markdown_statement(content: str) -> str:
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    soup = BeautifulSoup(content or "", "html.parser")
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()
    for tag in soup.find_all("sup"):
        tag.replace_with("^" + tag.get_text("", strip=True))
    for tag in soup.find_all("sub"):
        tag.replace_with("_" + tag.get_text("", strip=True))
    for image in soup.find_all("img"):
        if not image.get("src") and image.get("data-src"):
            image["src"] = image["data-src"]
        image["alt"] = image.get("alt") or "题目示意图"
    text = markdownify(
        str(soup),
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    text = html.unescape(text).replace("\xa0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def first_occurrence(catalog: Catalog, slug: str) -> Occurrence:
    return sorted(catalog.occurrences[slug], key=lambda item: (item.chapter_no, item.line))[0]


def file_occurrences(catalog: Catalog, slug: str, chapter_no: int) -> list[Occurrence]:
    return [item for item in catalog.occurrences[slug] if item.chapter_no == chapter_no]


def display_section(occurrences: list[Occurrence]) -> str:
    seen: list[str] = []
    for item in occurrences:
        value = item.section
        if value not in seen:
            seen.append(value)
    return "；".join(seen[:3]) + (" 等" if len(seen) > 3 else "")


def all_chapter_locations(catalog: Catalog, slug: str) -> str:
    chapters: list[int] = []
    for item in catalog.occurrences[slug]:
        if item.chapter_no not in chapters:
            chapters.append(item.chapter_no)
    return "、".join(f"第{number}章 {CHAPTER_NAMES[number]}" for number in chapters)


def anchor_for(slug: str) -> str:
    return "q-" + re.sub(r"[^a-z0-9-]", "-", slug.lower())


def repeated_focus(chapter_no: int) -> str:
    return {
        5: "本章把它作为双指针复练：明确两个指针各自表示什么，并用指针关系维持不变量。",
        10: "本章改用动态规划视角复练：先定义状态，再写清转移、初始化与遍历顺序。",
    }.get(chapter_no, "本章再次出现，建议脱离旧代码重新口述不变量并独立实现。")


def md_escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def build_markdown(
    catalog: Catalog,
    questions: dict[str, dict[str, Any]],
    insights: dict[str, dict[str, Any]],
) -> str:
    unique_slugs = catalog.unique_slugs
    first_chapter_for: dict[str, int] = {}
    for chapter_no in range(1, 12):
        for slug in catalog.chapter_slugs[chapter_no]:
            first_chapter_for.setdefault(slug, chapter_no)

    lines: list[str] = [
        "---",
        'title: "代码随想录 LeetCode 题目册"',
        f'date: "{date.today().isoformat()}"',
        'language: "zh-CN"',
        "---",
        "",
        "# 代码随想录 LeetCode 题目册",
        "",
        "> 按 `代码随想录-Markdown` 的 1-11 章顺序整理。题目筛选和出现顺序来自本地文件；题号、标题、难度与题干通过题目链接对照 LeetCode 中文站公开题目数据。",
        "",
        "## 使用说明",
        "",
        f"- 共扫描 **{catalog.raw_link_count}** 个语义化 LeetCode 链接，整理为 **{len(unique_slugs)}** 道唯一题、**{catalog.chapter_entry_count}** 个章节题目位置。",
        "- 同一章内的总览、正文、总结重复链接合并为一道；跨章节复练保留在原章节，但完整题干与思路只在首次出现处展开。",
        "- 11 个大章节默认折叠；展开章节后，每道唯一题的“我的题目思路与考察范围”仍可单独折叠。",
        "- `<details>` 中的内容是我的理解与复习提示，不是源文件原文；点击标题即可展开。PDF 版本中已全部展开。",
        "- 源文件中两处“637. 二叉树的层平均值”误链到 199，本题册已按题号校正为 637 的官方链接。",
        "- 剑指 Offer 与程序员面试金典沿用其原编号；“面试题 02.07”与主站 160 为同一主题，但保留源目录使用的编号。",
        "",
        "## 章节总览",
        "",
        "| 章节 | 主题 | 本章题目位置 |",
        "|---:|---|---:|",
    ]
    for chapter_no in range(1, 12):
        lines.append(
            f"| {chapter_no} | [{CHAPTER_NAMES[chapter_no]}](#chapter-{chapter_no}) | {len(catalog.chapter_slugs[chapter_no])} |"
        )

    lines.extend(["", "## 刷题正文", ""])
    global_index = 0
    for chapter_no in range(1, 12):
        chapter_name = CHAPTER_NAMES[chapter_no]
        source_name = dict(source_files())[chapter_no].name
        lines.extend(
            [
                f'<a id="chapter-{chapter_no}"></a>',
                "<details>",
                f"<summary><strong>第 {chapter_no} 章 {chapter_name}</strong>（{len(catalog.chapter_slugs[chapter_no])} 题）</summary>",
                "",
                f"> 来源：`代码随想录-Markdown/{source_name}`；本章共 {len(catalog.chapter_slugs[chapter_no])} 道去重题目。",
                "",
            ]
        )
        for chapter_index, slug in enumerate(catalog.chapter_slugs[chapter_no], start=1):
            record = questions[slug]
            title = question_title(record)
            qid = question_id(record)
            difficulty = DIFFICULTY_ZH.get(record.get("difficulty", ""), record.get("difficulty", "未知"))
            occurrences = file_occurrences(catalog, slug, chapter_no)
            kinds: list[str] = []
            for item in occurrences:
                if item.kind not in kinds:
                    kinds.append(item.kind)

            if first_chapter_for[slug] != chapter_no:
                first_no = first_chapter_for[slug]
                lines.extend(
                    [
                        f"### {qid}. {title}（复练）",
                        "",
                        f"- **本章顺序：** {chapter_index}/{len(catalog.chapter_slugs[chapter_no])}",
                        f"- **题目类型：** {'、'.join(kinds)}",
                        f"- **LeetCode：** [{canonical_url(slug)}]({canonical_url(slug)})",
                        f"- **本章位置：** {md_escape_table(display_section(occurrences))}",
                        f"- **完整收录：** [第 {first_no} 章 {CHAPTER_NAMES[first_no]}](#{anchor_for(slug)})",
                        "",
                        f"> {repeated_focus(chapter_no)}",
                        "",
                    ]
                )
                continue

            global_index += 1
            statement = normalize_markdown_statement(
                record.get("translatedContent") or record.get("content") or ""
            )
            insight = insights[slug]
            lines.extend(
                [
                    f'<a id="{anchor_for(slug)}"></a>',
                    f"### {qid}. {title}",
                    "",
                    f"- **唯一题序：** {global_index}/{len(unique_slugs)}",
                    f"- **本章顺序：** {chapter_index}/{len(catalog.chapter_slugs[chapter_no])}",
                    f"- **难度：** {difficulty}",
                    f"- **题目类型：** {'、'.join(kinds)}",
                    f"- **LeetCode：** [{canonical_url(slug)}]({canonical_url(slug)})",
                    f"- **源文件位置：** `{occurrences[0].source_file}:{occurrences[0].line}`；{md_escape_table(display_section(occurrences))}",
                    f"- **出现章节：** {all_chapter_locations(catalog, slug)}",
                    "",
                    "#### 题目内容",
                    "",
                    statement or "（官方题面为空，请打开题目链接查看。）",
                    "",
                    "<details>",
                    "<summary><strong>我的题目思路与考察范围</strong></summary>",
                    "",
                    f"- **核心思路：** {insight['core']}",
                    f"- **关键不变量 / 状态：** {insight['invariant']}",
                    f"- **复杂度：** {insight['complexity']}",
                    "- **考察范围：** " + " · ".join(f"`{tag}`" for tag in insight["scope"]),
                    f"- **易错点：** {insight['pitfall']}",
                    "",
                    "</details>",
                    "",
                ]
            )

        lines.extend(["</details>", ""])

    lines.extend(
        [
            "# 附录：校验口径",
            "",
            "- 章节顺序按源目录 README 与文件数字前缀确定。",
            "- 只收录指向 LeetCode `/problems/<slug>/` 的语义化 Markdown 链接；programmercarl、Bilibili、GitHub 与卡码网链接不计入题目。",
            "- 同章按首次出现顺序去重；跨章复练保留章节位置。",
            "- 题干为生成日获取的公开题面；若 LeetCode 后续修订，以题目链接为准。",
            "",
        ]
    )
    return "\n".join(lines)


def xml_escape(value: str) -> str:
    return html.escape(value, quote=True).replace("\n", "<br/>")


def clean_text(value: str) -> str:
    value = html.unescape(value).replace("\xa0", " ")
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r" *\n *", "\n", value)
    return value.strip()


def collect_image_urls(content: str) -> list[str]:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(content or "", "html.parser")
    result: list[str] = []
    for image in soup.find_all("img"):
        src = image.get("src") or image.get("data-src")
        if not src:
            continue
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = "https://leetcode.cn" + src
        if src not in result:
            result.append(src)
    return result


def image_cache_path(url: str) -> Path:
    parsed = urllib.parse.urlparse(url)
    suffix = Path(parsed.path).suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        suffix = ".img"
    return IMAGE_CACHE_DIR / f"{hashlib.sha256(url.encode()).hexdigest()}{suffix}"


def download_image(url: str) -> tuple[str, str | None]:
    if url.startswith("data:"):
        try:
            header, encoded = url.split(",", 1)
            suffix = ".png" if "png" in header else ".jpg"
            path = IMAGE_CACHE_DIR / f"{hashlib.sha256(url.encode()).hexdigest()}{suffix}"
            if not path.exists():
                payload = base64.b64decode(encoded) if ";base64" in header else urllib.parse.unquote_to_bytes(encoded)
                path.write_bytes(payload)
            return url, str(path)
        except Exception:
            return url, None

    path = image_cache_path(url)
    if path.exists() and path.stat().st_size > 0:
        return url, str(path)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 Chrome/151 Safari/537.36"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read()
            if len(payload) < 32:
                raise RuntimeError("image payload too small")
            path.write_bytes(payload)
            return url, str(path)
        except Exception:  # noqa: BLE001
            time.sleep(0.8 * (attempt + 1))
    return url, None


def prefetch_images(questions: dict[str, dict[str, Any]]) -> dict[str, str]:
    IMAGE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    urls: list[str] = []
    for record in questions.values():
        content = record.get("translatedContent") or record.get("content") or ""
        for url in collect_image_urls(content):
            if url not in urls:
                urls.append(url)
    mapping: dict[str, str] = {}
    if not urls:
        return mapping
    print(f"Fetching {len(urls)} statement images...", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for index, (url, path) in enumerate(executor.map(download_image, urls), start=1):
            if path:
                mapping[url] = path
            if index % 20 == 0 or index == len(urls):
                print(f"  images {index}/{len(urls)}", flush=True)
    return mapping


def build_pdf(
    catalog: Catalog,
    questions: dict[str, dict[str, Any]],
    insights: dict[str, dict[str, Any]],
    image_paths: dict[str, str],
) -> None:
    from bs4 import BeautifulSoup, NavigableString, Tag
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        BaseDocTemplate,
        CondPageBreak,
        Flowable,
        Frame,
        Image,
        KeepTogether,
        ListFlowable,
        ListItem,
        PageBreak,
        PageTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )
    from reportlab.platypus.tableofcontents import TableOfContents

    font_path = Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf")
    if not font_path.exists():
        raise FileNotFoundError(f"Required Chinese font not found: {font_path}")
    pdfmetrics.registerFont(TTFont("CatalogCN", str(font_path)))
    pdfmetrics.registerFontFamily(
        "CatalogCN",
        normal="CatalogCN",
        bold="CatalogCN",
        italic="CatalogCN",
        boldItalic="CatalogCN",
    )

    page_width, page_height = A4
    left_margin = 17 * mm
    right_margin = 17 * mm
    top_margin = 20 * mm
    bottom_margin = 18 * mm
    content_width = page_width - left_margin - right_margin

    palette = {
        "ink": colors.HexColor("#172033"),
        "muted": colors.HexColor("#64748B"),
        "blue": colors.HexColor("#315A9B"),
        "blue_light": colors.HexColor("#EAF1FB"),
        "teal": colors.HexColor("#0F766E"),
        "teal_light": colors.HexColor("#E7F6F3"),
        "line": colors.HexColor("#D7DEE9"),
        "paper": colors.HexColor("#F8FAFC"),
        "code": colors.HexColor("#F1F5F9"),
        "warning": colors.HexColor("#FFF7E6"),
    }

    styles = getSampleStyleSheet()
    base = ParagraphStyle(
        "BaseCN",
        parent=styles["BodyText"],
        fontName="CatalogCN",
        fontSize=9.2,
        leading=15,
        textColor=palette["ink"],
        spaceAfter=5,
        wordWrap="CJK",
        splitLongWords=True,
    )
    cover_title = ParagraphStyle(
        "CoverTitle",
        parent=base,
        fontSize=28,
        leading=40,
        alignment=TA_CENTER,
        textColor=palette["blue"],
        spaceAfter=12,
    )
    cover_subtitle = ParagraphStyle(
        "CoverSubtitle",
        parent=base,
        fontSize=12,
        leading=20,
        alignment=TA_CENTER,
        textColor=palette["muted"],
    )
    chapter_style = ParagraphStyle(
        "Chapter",
        parent=base,
        fontSize=21,
        leading=29,
        textColor=palette["blue"],
        spaceBefore=4,
        spaceAfter=14,
    )
    question_style = ParagraphStyle(
        "Question",
        parent=base,
        fontSize=14,
        leading=21,
        textColor=palette["ink"],
        spaceBefore=13,
        spaceAfter=7,
        keepWithNext=True,
    )
    section_style = ParagraphStyle(
        "Section",
        parent=base,
        fontSize=10.5,
        leading=16,
        textColor=palette["blue"],
        spaceBefore=8,
        spaceAfter=5,
        keepWithNext=True,
    )
    small = ParagraphStyle(
        "Small",
        parent=base,
        fontSize=8.1,
        leading=12.5,
        textColor=palette["muted"],
    )
    code_style = ParagraphStyle(
        "Code",
        parent=base,
        fontSize=7.8,
        leading=11.2,
        leftIndent=7,
        rightIndent=7,
        borderColor=palette["line"],
        borderWidth=0.5,
        borderPadding=7,
        borderRadius=3,
        backColor=palette["code"],
        spaceBefore=4,
        spaceAfter=7,
    )
    insight_style = ParagraphStyle(
        "Insight",
        parent=base,
        fontSize=9,
        leading=14.5,
        leftIndent=10,
        rightIndent=10,
        borderColor=palette["teal"],
        borderWidth=0.8,
        borderPadding=9,
        borderRadius=4,
        backColor=palette["teal_light"],
        spaceBefore=5,
        spaceAfter=9,
    )
    repeat_style = ParagraphStyle(
        "Repeat",
        parent=base,
        leftIndent=9,
        rightIndent=9,
        borderColor=palette["line"],
        borderWidth=0.5,
        borderPadding=8,
        backColor=palette["paper"],
        spaceAfter=8,
    )
    toc_title_style = ParagraphStyle(
        "TOCTitle",
        parent=chapter_style,
        fontSize=20,
        alignment=TA_LEFT,
    )

    class CatalogDocTemplate(BaseDocTemplate):
        def __init__(self, filename: str):
            super().__init__(
                filename,
                pagesize=A4,
                leftMargin=left_margin,
                rightMargin=right_margin,
                topMargin=top_margin,
                bottomMargin=bottom_margin,
                title="代码随想录 LeetCode 题目册",
                author="OpenAI Codex（整理）",
                subject="按代码随想录刷题顺序整理的 LeetCode 题目、思路与考察范围",
            )
            frame = Frame(
                left_margin,
                bottom_margin,
                content_width,
                page_height - top_margin - bottom_margin,
                id="body",
            )
            self.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=self._draw_page))

        def _draw_page(self, canvas, doc):
            canvas.saveState()
            canvas.setFont("CatalogCN", 7.7)
            canvas.setFillColor(palette["muted"])
            if doc.page > 1:
                canvas.drawString(left_margin, page_height - 11 * mm, "代码随想录 · LeetCode 题目册")
                canvas.drawRightString(page_width - right_margin, 10 * mm, f"第 {doc.page} 页")
                canvas.setStrokeColor(palette["line"])
                canvas.setLineWidth(0.4)
                canvas.line(left_margin, page_height - 13 * mm, page_width - right_margin, page_height - 13 * mm)
            canvas.restoreState()

        def afterFlowable(self, flowable: Flowable):
            level = getattr(flowable, "toc_level", None)
            if level is None:
                return
            text = flowable.getPlainText()
            key = getattr(flowable, "bookmark_key", f"toc-{self.page}-{id(flowable)}")
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=level, closed=(level == 0))
            self.notify("TOCEntry", (level, text, self.page, key))

    def tagged_paragraph(text: str, style, level: int, key: str):
        paragraph = Paragraph(xml_escape(text), style)
        paragraph.toc_level = level
        paragraph.bookmark_key = key
        return paragraph

    def paragraph_from_tag(tag: Tag, style=base) -> Paragraph:
        text = clean_text(tag.get_text(" ", strip=False))
        return Paragraph(xml_escape(text), style)

    def statement_flowables(content: str) -> list[Flowable]:
        soup = BeautifulSoup(content or "", "html.parser")
        for tag in soup.find_all("sup"):
            tag.replace_with("^" + tag.get_text("", strip=True))
        for tag in soup.find_all("sub"):
            tag.replace_with("_" + tag.get_text("", strip=True))
        result: list[Flowable] = []

        def add_image(src: str | None, alt: str = "题目示意图") -> None:
            if not src:
                return
            if src.startswith("//"):
                src = "https:" + src
            elif src.startswith("/"):
                src = "https://leetcode.cn" + src
            cached = image_paths.get(src)
            if not cached:
                result.append(Paragraph(f"[图示：{xml_escape(alt)}，请参阅在线题目]", small))
                return
            try:
                image = Image(cached)
                max_width = content_width * 0.78
                max_height = 82 * mm
                scale = min(max_width / image.imageWidth, max_height / image.imageHeight, 1.0)
                image.drawWidth = image.imageWidth * scale
                image.drawHeight = image.imageHeight * scale
                image.hAlign = "CENTER"
                image._restrictSize(max_width, max_height)
                result.extend([Spacer(1, 3), image, Spacer(1, 5)])
            except Exception:
                result.append(Paragraph(f"[图示：{xml_escape(alt)}，请参阅在线题目]", small))

        def walk(node) -> None:
            if isinstance(node, NavigableString):
                text = clean_text(str(node))
                if text:
                    result.append(Paragraph(xml_escape(text), base))
                return
            if not isinstance(node, Tag):
                return
            name = node.name.lower()
            if name in {"script", "style"}:
                return
            if name in {"div", "section", "article", "body"}:
                for child in node.children:
                    walk(child)
                return
            if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
                result.append(paragraph_from_tag(node, section_style))
                return
            if name == "pre":
                # Do not insert separators between nested <strong>/<code> tags:
                # LeetCode wraps individual tokens in those tags inside <pre>,
                # and a separator would turn arrays into one item per line.
                text = html.unescape(node.get_text("", strip=False)).replace("\xa0", " ")
                text = textwrap.dedent(text).strip()
                result.append(Paragraph(xml_escape(text), code_style))
                return
            if name in {"ul", "ol"}:
                items: list[ListItem] = []
                for child in node.find_all("li", recursive=False):
                    item_text = clean_text(child.get_text(" ", strip=False))
                    items.append(ListItem(Paragraph(xml_escape(item_text), base), leftIndent=10))
                if items:
                    result.append(
                        ListFlowable(
                            items,
                            bulletType="1" if name == "ol" else "bullet",
                            start="1",
                            leftIndent=18,
                            bulletFontName="CatalogCN",
                            bulletFontSize=8,
                            spaceAfter=6,
                        )
                    )
                return
            if name == "table":
                rows: list[list[Paragraph]] = []
                for tr in node.find_all("tr"):
                    cells = tr.find_all(["th", "td"], recursive=False)
                    if cells:
                        rows.append([Paragraph(xml_escape(clean_text(cell.get_text(" "))), small) for cell in cells])
                if rows:
                    columns = max(len(row) for row in rows)
                    for row in rows:
                        row.extend([Paragraph("", small)] * (columns - len(row)))
                    table = Table(rows, colWidths=[content_width / columns] * columns, repeatRows=1)
                    table.setStyle(
                        TableStyle(
                            [
                                ("GRID", (0, 0), (-1, -1), 0.4, palette["line"]),
                                ("BACKGROUND", (0, 0), (-1, 0), palette["blue_light"]),
                                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                                ("TOPPADDING", (0, 0), (-1, -1), 4),
                                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                            ]
                        )
                    )
                    result.extend([table, Spacer(1, 6)])
                return
            if name == "img":
                add_image(node.get("src") or node.get("data-src"), node.get("alt") or "题目示意图")
                return
            if name == "blockquote":
                quote_style = ParagraphStyle(
                    "QuoteDynamic",
                    parent=base,
                    leftIndent=10,
                    borderColor=palette["line"],
                    borderWidth=0.7,
                    borderPadding=6,
                    backColor=palette["paper"],
                )
                result.append(paragraph_from_tag(node, quote_style))
                return
            if name == "p":
                text = clean_text(node.get_text(" ", strip=False))
                if text:
                    result.append(Paragraph(xml_escape(text), base))
                for image in node.find_all("img"):
                    add_image(image.get("src") or image.get("data-src"), image.get("alt") or "题目示意图")
                return
            text = clean_text(node.get_text(" ", strip=False))
            if text:
                result.append(Paragraph(xml_escape(text), base))

        roots = list(soup.body.children) if soup.body else list(soup.children)
        for root in roots:
            walk(root)
        return result or [Paragraph("（官方题面为空，请打开题目链接查看。）", base)]

    unique_slugs = catalog.unique_slugs
    first_chapter_for: dict[str, int] = {}
    for chapter_no in range(1, 12):
        for slug in catalog.chapter_slugs[chapter_no]:
            first_chapter_for.setdefault(slug, chapter_no)

    story: list[Flowable] = [
        Spacer(1, 43 * mm),
        Paragraph("代码随想录", cover_subtitle),
        Spacer(1, 5 * mm),
        Paragraph("LeetCode 题目册", cover_title),
        Paragraph("按原刷题顺序整理 · 题目内容 · 思路 · 考察范围", cover_subtitle),
        Spacer(1, 21 * mm),
    ]
    stats_table = Table(
        [
            [Paragraph("11", cover_title), Paragraph(str(len(unique_slugs)), cover_title), Paragraph(str(catalog.chapter_entry_count), cover_title)],
            [Paragraph("算法章节", cover_subtitle), Paragraph("唯一题目", cover_subtitle), Paragraph("章节题位", cover_subtitle)],
        ],
        colWidths=[content_width / 3] * 3,
    )
    stats_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), palette["paper"]),
                ("BOX", (0, 0), (-1, -1), 0.7, palette["line"]),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, palette["line"]),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    story.extend(
        [
            stats_table,
            Spacer(1, 26 * mm),
            Paragraph(f"生成日期：{date.today().isoformat()}", cover_subtitle),
            PageBreak(),
            Paragraph("阅读与编排说明", toc_title_style),
            Paragraph(
                f"本题册从本地 11 个章节中扫描 {catalog.raw_link_count} 个语义化 LeetCode 链接，"
                f"整理为 {len(unique_slugs)} 道唯一题。题目顺序来自本地资料；题号、难度和题干由题目链接对照 LeetCode 中文站公开数据。",
                base,
            ),
            Paragraph(
                "同一章的总览、正文和总结重复链接已合并；跨章节复练仍在原章节出现，但完整题干只在首次出现处展示。"
                "PDF 中“我的题目思路与考察范围”均已展开。源文件中两处 637 错链已按题号修正。",
                base,
            ),
            Spacer(1, 6),
        ]
    )

    chapter_rows = [[Paragraph("章节", small), Paragraph("主题", small), Paragraph("题目位置", small)]]
    for chapter_no in range(1, 12):
        chapter_rows.append(
            [
                Paragraph(str(chapter_no), small),
                Paragraph(CHAPTER_NAMES[chapter_no], small),
                Paragraph(str(len(catalog.chapter_slugs[chapter_no])), small),
            ]
        )
    chapter_table = Table(chapter_rows, colWidths=[25 * mm, content_width - 55 * mm, 30 * mm], repeatRows=1)
    chapter_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), palette["blue_light"]),
                ("GRID", (0, 0), (-1, -1), 0.4, palette["line"]),
                ("ALIGN", (0, 0), (0, -1), "CENTER"),
                ("ALIGN", (-1, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.extend([chapter_table, PageBreak(), Paragraph("目录", toc_title_style)])
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOCChapter",
            fontName="CatalogCN",
            fontSize=10,
            leading=15,
            leftIndent=0,
            firstLineIndent=0,
            textColor=palette["blue"],
            spaceBefore=4,
        ),
        ParagraphStyle(
            "TOCQuestion",
            fontName="CatalogCN",
            fontSize=8,
            leading=11.5,
            leftIndent=12,
            firstLineIndent=0,
            textColor=palette["ink"],
        ),
    ]
    story.extend([toc, PageBreak()])

    global_index = 0
    for chapter_no in range(1, 12):
        if chapter_no > 1:
            story.append(PageBreak())
        chapter_name = CHAPTER_NAMES[chapter_no]
        chapter_heading = tagged_paragraph(
            f"第 {chapter_no} 章 {chapter_name}", chapter_style, 0, f"chapter-{chapter_no}"
        )
        story.extend(
            [
                chapter_heading,
                Paragraph(
                    f"本章 {len(catalog.chapter_slugs[chapter_no])} 道去重题目，按源文件首次出现顺序排列。",
                    small,
                ),
                Spacer(1, 5),
            ]
        )

        for chapter_index, slug in enumerate(catalog.chapter_slugs[chapter_no], start=1):
            record = questions[slug]
            title = question_title(record)
            qid = question_id(record)
            difficulty = DIFFICULTY_ZH.get(record.get("difficulty", ""), record.get("difficulty", "未知"))
            occurrences = file_occurrences(catalog, slug, chapter_no)
            heading_text = f"{qid}. {title}" + ("（复练）" if first_chapter_for[slug] != chapter_no else "")
            question_key = f"chapter-{chapter_no}-{anchor_for(slug)}"
            question_heading = tagged_paragraph(heading_text, question_style, 1, question_key)
            story.extend([CondPageBreak(35 * mm), question_heading])

            if first_chapter_for[slug] != chapter_no:
                first_no = first_chapter_for[slug]
                repeat_text = (
                    f"<b>本章顺序：</b>{chapter_index}/{len(catalog.chapter_slugs[chapter_no])}<br/>"
                    f"<b>LeetCode：</b><link href=\"{canonical_url(slug)}\">{canonical_url(slug)}</link><br/>"
                    f"<b>完整收录：</b>第 {first_no} 章 {CHAPTER_NAMES[first_no]}<br/>"
                    f"<b>复练重点：</b>{xml_escape(repeated_focus(chapter_no))}"
                )
                story.append(Paragraph(repeat_text, repeat_style))
                continue

            global_index += 1
            kinds: list[str] = []
            for item in occurrences:
                if item.kind not in kinds:
                    kinds.append(item.kind)
            metadata = [
                ["唯一题序", f"{global_index}/{len(unique_slugs)}", "本章顺序", f"{chapter_index}/{len(catalog.chapter_slugs[chapter_no])}"],
                ["难度", difficulty, "题目类型", "、".join(kinds)],
                ["出现章节", all_chapter_locations(catalog, slug), "源位置", f"{occurrences[0].source_file}:{occurrences[0].line}"],
            ]
            metadata_rows = [[Paragraph(xml_escape(str(cell)), small) for cell in row] for row in metadata]
            metadata_table = Table(
                metadata_rows,
                colWidths=[18 * mm, 50 * mm, 19 * mm, content_width - 87 * mm],
            )
            metadata_table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (0, -1), palette["blue_light"]),
                        ("BACKGROUND", (2, 0), (2, -1), palette["blue_light"]),
                        ("GRID", (0, 0), (-1, -1), 0.35, palette["line"]),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("TOPPADDING", (0, 0), (-1, -1), 4),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                        ("LEFTPADDING", (0, 0), (-1, -1), 5),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ]
                )
            )
            story.extend(
                [
                    metadata_table,
                    Spacer(1, 4),
                    Paragraph(
                        f'<b>LeetCode：</b><link href="{canonical_url(slug)}">{canonical_url(slug)}</link>',
                        small,
                    ),
                    Paragraph("题目内容", section_style),
                ]
            )
            content = record.get("translatedContent") or record.get("content") or ""
            story.extend(statement_flowables(content))
            insight = insights[slug]
            tag_text = " · ".join(str(tag) for tag in insight["scope"])
            insight_text = (
                f"<b>我的题目思路与考察范围</b><br/>"
                f"<b>核心思路：</b>{xml_escape(insight['core'])}<br/>"
                f"<b>关键不变量 / 状态：</b>{xml_escape(insight['invariant'])}<br/>"
                f"<b>复杂度：</b>{xml_escape(insight['complexity'])}<br/>"
                f"<b>考察范围：</b>{xml_escape(tag_text)}<br/>"
                f"<b>易错点：</b>{xml_escape(insight['pitfall'])}"
            )
            # Keep the review callout as one visual unit so a final orphaned
            # line does not spill onto an otherwise empty page.
            story.append(KeepTogether([Paragraph(insight_text, insight_style)]))

    story.extend(
        [
            PageBreak(),
            tagged_paragraph("附录：校验口径", chapter_style, 0, "appendix-validation"),
            Paragraph("章节顺序按源目录 README 与文件数字前缀确定。", base),
            Paragraph(
                "仅收录指向 LeetCode /problems/&lt;slug&gt;/ 的语义化 Markdown 链接；"
                "programmercarl、Bilibili、GitHub 与卡码网链接不计入题目。",
                base,
            ),
            Paragraph("同章按首次出现顺序去重；跨章复练保留章节位置。", base),
            Paragraph("题干为生成日获取的公开题面；若 LeetCode 后续修订，以题目链接为准。", base),
        ]
    )

    document = CatalogDocTemplate(str(OUTPUT_PDF))
    document.multiBuild(story)


def validate_catalog(
    catalog: Catalog,
    questions: dict[str, dict[str, Any]],
    insights: dict[str, dict[str, Any]],
) -> None:
    expected_chapter_counts = {
        1: 14,
        2: 7,
        3: 9,
        4: 7,
        5: 14,
        6: 7,
        7: 42,
        8: 15,
        9: 17,
        10: 37,
        11: 5,
    }
    actual_counts = {number: len(catalog.chapter_slugs[number]) for number in range(1, 12)}
    if actual_counts != expected_chapter_counts:
        raise AssertionError(f"Chapter counts mismatch: {actual_counts}")
    if len(catalog.unique_slugs) != 158:
        raise AssertionError(f"Expected 158 unique slugs, got {len(catalog.unique_slugs)}")
    if catalog.chapter_entry_count != 174:
        raise AssertionError(f"Expected 174 chapter entries, got {catalog.chapter_entry_count}")
    if set(questions) != set(catalog.unique_slugs):
        raise AssertionError("Question metadata coverage mismatch")
    if set(insights) != set(catalog.unique_slugs):
        raise AssertionError("Insight coverage mismatch")
    for slug, record in questions.items():
        required = [question_id(record), question_title(record), record.get("difficulty")]
        if not all(required):
            raise AssertionError(f"Incomplete question metadata for {slug}: {record}")
        content = record.get("translatedContent") or record.get("content")
        if not content or len(clean_text(re.sub(r"<[^>]+>", " ", content))) < 20:
            raise AssertionError(f"Question statement missing/too short: {slug}")
    if "average-of-levels-in-binary-tree" not in catalog.unique_slugs:
        raise AssertionError("LC 637 correction missing")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="refresh LeetCode metadata cache")
    parser.add_argument("--skip-images", action="store_true", help="do not download statement images")
    parser.add_argument("--markdown-only", action="store_true", help="build only Markdown")
    parser.add_argument("--inventory", action="store_true", help="print extracted inventory and exit")
    args = parser.parse_args()

    catalog = extract_catalog()
    print(
        f"Extracted {catalog.raw_link_count} links, {catalog.chapter_entry_count} chapter entries, "
        f"{len(catalog.unique_slugs)} unique problems."
    )
    if args.inventory:
        payload = {
            "raw_link_count": catalog.raw_link_count,
            "chapter_entry_count": catalog.chapter_entry_count,
            "unique_problem_count": len(catalog.unique_slugs),
            "chapters": {str(number): catalog.chapter_slugs[number] for number in range(1, 12)},
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    questions = fetch_questions(catalog.unique_slugs, refresh=args.refresh)
    apply_question_overrides(questions)
    insights = load_insights(catalog.unique_slugs)
    validate_catalog(catalog, questions, insights)

    markdown = build_markdown(catalog, questions, insights)
    OUTPUT_MD.write_text(markdown.rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_MD}")

    if not args.markdown_only:
        image_paths = {} if args.skip_images else prefetch_images(questions)
        build_pdf(catalog, questions, insights, image_paths)
        print(f"Wrote {OUTPUT_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
