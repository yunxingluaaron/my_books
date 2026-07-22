# LeetCode 六十天美国面试刷题路线图

每天五题，采用专题递进、主动回忆、短间隔盲写与长间隔盲写，覆盖美国软件工程面试高频考点。

> 本文件由原工作簿转换而来。题目、链接、排期、复习间隔和训练字段均已保留。Markdown 不会自动执行 Excel 公式、数据验证和图表，因此进度统计部分采用可手动填写的静态字段。

## 计划总览

| 指标 | 数值 | 指标 | 数值 |
| :--- | ---: | :--- | ---: |
| 计划天数 | 60 | 每日任务 | 5 |
| 核心题数 | 100 | 总训练次数 | 300 |
| 首次学习 | 100 | 盲写复做 | 200 |
| 预计总时长 | 94.6 小时 | 日均限时 | 95 分钟 |

## 一 计划设计

| 序号 | 设计项 | 说明 |
| :---: | :--- | :--- |
| 1 | 题单融合 | 代码随想录提供从基础数据结构到回溯、贪心、动态规划、单调栈和图论的专题递进。Grind 75提供美国面试常见题型的优先级与跨专题交错顺序。 |
| 2 | 训练总量 | 一百道核心题，每题首次学习一次、短间隔盲写一次、长间隔盲写一次，共三百次训练，恰好覆盖六十天每天五题。 |
| 3 | 间隔策略 | 不采用固定神奇数字。首次复做安排在首次学习后的一至十天内，第二次复做安排在十五至二十八天内，并保证两次复做之间至少七天。 |
| 4 | 交错策略 | 同一天尽量混合不同考点，避免连续多天只刷一个专题。前四十五天逐步引入新题，后十五天只做限时复做与错题回收。 |
| 5 | 面试策略 | 每次提交前必须口述模式、关键不变量、时间复杂度、空间复杂度、边界条件和一种可替代方案。 |

## 二 每道题的执行流程

| 步骤 | 建议时长 | 动作 | 可验收输出 |
| :---: | :---: | :--- | :--- |
| 1 | 二分钟 | 复述题意，写出输入输出、约束和至少一个边界样例 | 能准确说明题目，不急着写代码 |
| 2 | 三分钟 | 先说暴力法，再定位瓶颈并识别核心模式 | 写出暴力复杂度和优化方向 |
| 3 | 按路线图限时 | 空白编辑器独立编码。复做时禁止查看旧代码 | 在限时内通过主要样例 |
| 4 | 三分钟 | 解释正确性、不变量、复杂度和可替代实现 | 能像面试现场一样完整表达 |
| 5 | 二分钟 | 打分并记录错误标签。分数为零或一时进入错题复盘表 | 形成下一次可执行修正动作 |

## 三 独立完成评分

| 分数 | 判定标准 | 后续动作 |
| :---: | :--- | :--- |
| 0 | 看题解后仍不能独立复现，或无法解释核心不变量 | 当天登记错题，次日先做五分钟口述回忆 |
| 1 | 能说出部分思路，但需要关键提示或代码无法独立完成 | 四十八小时内补一次不看代码的手写框架 |
| 2 | 独立完成，但超时、调试较多或表达不完整 | 下次复做前先口述边界和复杂度 |
| 3 | 限时内独立完成，并能清楚解释正确性、复杂度和替代方案 | 保持原计划，不额外加练 |

## 四 六个阶段的节奏

| 阶段 | 天数 | 每日新题 | 每日复做 | 主要目标 |
| :--- | :--- | :--- | :--- | :--- |
| 阶段一 基础模式与语言热身 | 第一至第八天 | 首日五题，其余三题 | 首日零题，其余两题 | 建立数组、哈希、链表、栈、树和二分的基础语言 |
| 阶段二 高频中等题主干 | 第九至第二十天 | 两题 | 三题 | 扩大高频中等题模式，开始稳定限时表达 |
| 阶段三 树图动态规划深化 | 第二十一至第三十三天 | 两题 | 三题 | 深化树、图、回溯和动态规划，强化状态定义 |
| 阶段四 专题补强与难题 | 第三十四至第四十五天 | 两题 | 三题 | 补齐区间、堆、单调结构、位运算和困难题 |
| 阶段五 交错限时模拟 | 第四十六至第五十二天 | 零题 | 五题 | 跨专题限时模拟，减少依赖最近记忆 |
| 阶段六 面试冲刺与错题回收 | 第五十三至第六十天 | 零题 | 五题 | 面试冲刺，回收低分题和高频模式 |

## 五 训练类型与执行动作

| 训练类型 | 执行动作 |
| :--- | :--- |
| 新题 | 盲做并先口述暴力法与优化方向，到时停笔，完成后写复杂度、边界与可追问点 |
| 短间隔复做 | 空白编辑器重写，禁止看旧代码，卡住五分钟后只看最小提示 |
| 长间隔复做 | 严格限时独立完成，先说模式与不变量，再回答复杂度和替代方案 |

## 六 资料与研究依据

| 资料 | 本计划采用的要点 |
| :--- | :--- |
| [代码随想录主页](https://programmercarl.com/) | 采用其专题学习顺序和由基础数据结构逐步进入算法专题的组织方式 |
| [代码随想录题单](https://programmercarl.com/qita/12.list.html) | 用于补齐链表、回溯、贪心、动态规划、单调结构和图论代表题 |
| [Grind 75题单](https://www.techinterviewhandbook.org/grind75/) | 采用其高频核心题与美国面试常见题型优先级 |
| [Grind 75说明](https://www.techinterviewhandbook.org/grind75/about) | 参考题目选择、难度排序、主题覆盖与建议解题时长 |
| [Grind 75常见问题](https://www.techinterviewhandbook.org/grind75/faq) | 参考跨主题顺序、常见中等难度和二十至三十分钟限时建议 |
| [间隔练习研究](https://pubmed.ncbi.nlm.nih.gov/19076480/) | 复习间隔应随目标保留时间增长，本计划据此使用短窗口和长窗口 |
| [分散练习综述](https://pubmed.ncbi.nlm.nih.gov/16507066/) | 分散学习相对集中学习具有稳定的长期记忆优势 |
| [主动回忆研究](https://pubmed.ncbi.nlm.nih.gov/26173288/) | 用测试和独立提取替代单纯重读，长期保持更强 |

## 七 六十天每日路线图

完成一题后，可将“☐”改为“☑”。独立完成分填写零至三分。

### 阶段一 基础模式与语言热身

#### 第 1 天

阶段：阶段一 基础模式与语言热身  计划：新题 5 道，复做 0 道，共 5 道  建议总限时：90 分钟  当日重点：数组与哈希、栈与队列、链表、数组与贪心、字符串与双指针

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 新题<br>基础建模一 | [LeetCode 1 两数之和](https://leetcode.com/problems/two-sum/)<br>Two Sum<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 哈希表查补数 | 首次学习 | 15 分钟 |
| 2 | ☐ | 新题<br>基础建模二 | [LeetCode 20 有效的括号](https://leetcode.com/problems/valid-parentheses/)<br>Valid Parentheses<br>来源：Grind 75核心 | 简单 | 栈与队列<br>栈与队列 | 栈与括号匹配 | 首次学习 | 20 分钟 |
| 3 | ☐ | 新题<br>基础建模三 | [LeetCode 21 合并两个有序链表](https://leetcode.com/problems/merge-two-sorted-lists/)<br>Merge Two Sorted Lists<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 归并双指针 | 首次学习 | 20 分钟 |
| 4 | ☐ | 新题<br>基础建模四 | [LeetCode 121 买卖股票的最佳时机](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)<br>Best Time to Buy and Sell Stock<br>来源：Grind 75核心 | 简单 | 贪心与区间<br>数组与贪心 | 维护历史最小值 | 首次学习 | 20 分钟 |
| 5 | ☐ | 新题<br>基础建模五 | [LeetCode 125 验证回文串](https://leetcode.com/problems/valid-palindrome/)<br>Valid Palindrome<br>来源：Grind 75核心 | 简单 | 双指针<br>字符串与双指针 | 对撞指针 | 首次学习 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 两数之和 | 未开始 |  |  |  |  |
| 2 | 有效的括号 | 未开始 |  |  |  |  |
| 3 | 合并两个有序链表 | 未开始 |  |  |  |  |
| 4 | 买卖股票的最佳时机 | 未开始 |  |  |  |  |
| 5 | 验证回文串 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 2 天

阶段：阶段一 基础模式与语言热身  计划：新题 3 道，复做 2 道，共 5 道  建议总限时：71 分钟  当日重点：二叉树、数组与哈希、二分查找

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 20 有效的括号](https://leetcode.com/problems/valid-parentheses/)<br>Valid Parentheses<br>来源：Grind 75核心 | 简单 | 栈与队列<br>栈与队列 | 栈与括号匹配 | 距首次 1 天<br>距上次 1 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 226 翻转二叉树](https://leetcode.com/problems/invert-binary-tree/)<br>Invert Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 递归遍历 | 首次学习 | 15 分钟 |
| 3 | ☐ | 新题<br>主练二 | [LeetCode 242 有效的字母异位词](https://leetcode.com/problems/valid-anagram/)<br>Valid Anagram<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 字符频次计数 | 首次学习 | 15 分钟 |
| 4 | ☐ | 短间隔复做<br>短测复做 | [LeetCode 21 合并两个有序链表](https://leetcode.com/problems/merge-two-sorted-lists/)<br>Merge Two Sorted Lists<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 归并双指针 | 距首次 1 天<br>距上次 1 天 | 13 分钟 |
| 5 | ☐ | 新题<br>主练三 | [LeetCode 704 二分查找](https://leetcode.com/problems/binary-search/)<br>Binary Search<br>来源：Grind 75核心 | 简单 | 二分查找<br>二分查找 | 区间定义与循环不变量 | 首次学习 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 有效的括号 | 未开始 |  |  |  |  |
| 2 | 翻转二叉树 | 未开始 |  |  |  |  |
| 3 | 有效的字母异位词 | 未开始 |  |  |  |  |
| 4 | 合并两个有序链表 | 未开始 |  |  |  |  |
| 5 | 二分查找 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 3 天

阶段：阶段一 基础模式与语言热身  计划：新题 3 道，复做 2 道，共 5 道  建议总限时：80 分钟  当日重点：图论、二叉搜索树、二叉树

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 1 两数之和](https://leetcode.com/problems/two-sum/)<br>Two Sum<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 哈希表查补数 | 距首次 2 天<br>距上次 2 天 | 12 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 733 图像渲染](https://leetcode.com/problems/flood-fill/)<br>Flood Fill<br>来源：Grind 75核心 | 简单 | 图与并查集<br>图论 | 网格深搜或广搜 | 首次学习 | 20 分钟 |
| 3 | ☐ | 新题<br>主练二 | [LeetCode 235 二叉搜索树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)<br>Lowest Common Ancestor of a Binary Search Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 利用有序性质缩小范围 | 首次学习 | 20 分钟 |
| 4 | ☐ | 短间隔复做<br>短测复做 | [LeetCode 121 买卖股票的最佳时机](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)<br>Best Time to Buy and Sell Stock<br>来源：Grind 75核心 | 简单 | 贪心与区间<br>数组与贪心 | 维护历史最小值 | 距首次 2 天<br>距上次 2 天 | 13 分钟 |
| 5 | ☐ | 新题<br>主练三 | [LeetCode 110 平衡二叉树](https://leetcode.com/problems/balanced-binary-tree/)<br>Balanced Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 自底向上递归 | 首次学习 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 两数之和 | 未开始 |  |  |  |  |
| 2 | 图像渲染 | 未开始 |  |  |  |  |
| 3 | 二叉搜索树的最近公共祖先 | 未开始 |  |  |  |  |
| 4 | 买卖股票的最佳时机 | 未开始 |  |  |  |  |
| 5 | 平衡二叉树 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 4 天

阶段：阶段一 基础模式与语言热身  计划：新题 3 道，复做 2 道，共 5 道  建议总限时：84 分钟  当日重点：链表、栈与队列、二分查找

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 125 验证回文串](https://leetcode.com/problems/valid-palindrome/)<br>Valid Palindrome<br>来源：Grind 75核心 | 简单 | 双指针<br>字符串与双指针 | 对撞指针 | 距首次 3 天<br>距上次 3 天 | 12 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 141 环形链表](https://leetcode.com/problems/linked-list-cycle/)<br>Linked List Cycle<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 快慢指针 | 首次学习 | 20 分钟 |
| 3 | ☐ | 新题<br>主练二 | [LeetCode 232 用栈实现队列](https://leetcode.com/problems/implement-queue-using-stacks/)<br>Implement Queue using Stacks<br>来源：Grind 75核心 | 简单 | 栈与队列<br>栈与队列 | 双栈模拟 | 首次学习 | 20 分钟 |
| 4 | ☐ | 短间隔复做<br>短测复做 | [LeetCode 226 翻转二叉树](https://leetcode.com/problems/invert-binary-tree/)<br>Invert Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 递归遍历 | 距首次 2 天<br>距上次 2 天 | 12 分钟 |
| 5 | ☐ | 新题<br>主练三 | [LeetCode 278 第一个错误的版本](https://leetcode.com/problems/first-bad-version/)<br>First Bad Version<br>来源：Grind 75核心 | 简单 | 二分查找<br>二分查找 | 左边界查找 | 首次学习 | 20 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 验证回文串 | 未开始 |  |  |  |  |
| 2 | 环形链表 | 未开始 |  |  |  |  |
| 3 | 用栈实现队列 | 未开始 |  |  |  |  |
| 4 | 翻转二叉树 | 未开始 |  |  |  |  |
| 5 | 第一个错误的版本 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 5 天

阶段：阶段一 基础模式与语言热身  计划：新题 3 道，复做 2 道，共 5 道  建议总限时：80 分钟  当日重点：数组与哈希、动态规划、字符串与哈希

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 704 二分查找](https://leetcode.com/problems/binary-search/)<br>Binary Search<br>来源：Grind 75核心 | 简单 | 二分查找<br>二分查找 | 区间定义与循环不变量 | 距首次 3 天<br>距上次 3 天 | 12 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 383 赎金信](https://leetcode.com/problems/ransom-note/)<br>Ransom Note<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 字符频次计数 | 首次学习 | 15 分钟 |
| 3 | ☐ | 新题<br>主练二 | [LeetCode 70 爬楼梯](https://leetcode.com/problems/climbing-stairs/)<br>Climbing Stairs<br>来源：Grind 75核心 | 简单 | 动态规划<br>动态规划 | 一维状态转移 | 首次学习 | 20 分钟 |
| 4 | ☐ | 短间隔复做<br>短测复做 | [LeetCode 733 图像渲染](https://leetcode.com/problems/flood-fill/)<br>Flood Fill<br>来源：Grind 75核心 | 简单 | 图与并查集<br>图论 | 网格深搜或广搜 | 距首次 2 天<br>距上次 2 天 | 13 分钟 |
| 5 | ☐ | 新题<br>主练三 | [LeetCode 409 最长回文串](https://leetcode.com/problems/longest-palindrome/)<br>Longest Palindrome<br>来源：Grind 75核心 | 简单 | 字符串<br>字符串与哈希 | 频次奇偶性 | 首次学习 | 20 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 二分查找 | 未开始 |  |  |  |  |
| 2 | 赎金信 | 未开始 |  |  |  |  |
| 3 | 爬楼梯 | 未开始 |  |  |  |  |
| 4 | 图像渲染 | 未开始 |  |  |  |  |
| 5 | 最长回文串 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 6 天

阶段：阶段一 基础模式与语言热身  计划：新题 3 道，复做 2 道，共 5 道  建议总限时：80 分钟  当日重点：链表、数组与贪心、位运算与字符串

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 235 二叉搜索树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)<br>Lowest Common Ancestor of a Binary Search Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 利用有序性质缩小范围 | 距首次 3 天<br>距上次 3 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 206 反转链表](https://leetcode.com/problems/reverse-linked-list/)<br>Reverse Linked List<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 指针反转 | 首次学习 | 20 分钟 |
| 3 | ☐ | 新题<br>主练二 | [LeetCode 169 多数元素](https://leetcode.com/problems/majority-element/)<br>Majority Element<br>来源：Grind 75核心 | 简单 | 贪心与区间<br>数组与贪心 | Boyer Moore投票 | 首次学习 | 20 分钟 |
| 4 | ☐ | 短间隔复做<br>短测复做 | [LeetCode 242 有效的字母异位词](https://leetcode.com/problems/valid-anagram/)<br>Valid Anagram<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 字符频次计数 | 距首次 4 天<br>距上次 4 天 | 12 分钟 |
| 5 | ☐ | 新题<br>主练三 | [LeetCode 67 二进制求和](https://leetcode.com/problems/add-binary/)<br>Add Binary<br>来源：Grind 75核心 | 简单 | 位运算<br>位运算与字符串 | 逐位模拟进位 | 首次学习 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 二叉搜索树的最近公共祖先 | 未开始 |  |  |  |  |
| 2 | 反转链表 | 未开始 |  |  |  |  |
| 3 | 多数元素 | 未开始 |  |  |  |  |
| 4 | 有效的字母异位词 | 未开始 |  |  |  |  |
| 5 | 二进制求和 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 7 天

阶段：阶段一 基础模式与语言热身  计划：新题 3 道，复做 2 道，共 5 道  建议总限时：91 分钟  当日重点：二叉树、链表

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 232 用栈实现队列](https://leetcode.com/problems/implement-queue-using-stacks/)<br>Implement Queue using Stacks<br>来源：Grind 75核心 | 简单 | 栈与队列<br>栈与队列 | 双栈模拟 | 距首次 3 天<br>距上次 3 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 543 二叉树的直径](https://leetcode.com/problems/diameter-of-binary-tree/)<br>Diameter of Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 树形动态规划 | 首次学习 | 30 分钟 |
| 3 | ☐ | 新题<br>主练二 | [LeetCode 876 链表的中间结点](https://leetcode.com/problems/middle-of-the-linked-list/)<br>Middle of the Linked List<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 快慢指针 | 首次学习 | 20 分钟 |
| 4 | ☐ | 短间隔复做<br>短测复做 | [LeetCode 278 第一个错误的版本](https://leetcode.com/problems/first-bad-version/)<br>First Bad Version<br>来源：Grind 75核心 | 简单 | 二分查找<br>二分查找 | 左边界查找 | 距首次 3 天<br>距上次 3 天 | 13 分钟 |
| 5 | ☐ | 新题<br>主练三 | [LeetCode 104 二叉树的最大深度](https://leetcode.com/problems/maximum-depth-of-binary-tree/)<br>Maximum Depth of Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 深搜或层序遍历 | 首次学习 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 用栈实现队列 | 未开始 |  |  |  |  |
| 2 | 二叉树的直径 | 未开始 |  |  |  |  |
| 3 | 链表的中间结点 | 未开始 |  |  |  |  |
| 4 | 第一个错误的版本 | 未开始 |  |  |  |  |
| 5 | 二叉树的最大深度 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 8 天

阶段：阶段一 基础模式与语言热身  计划：新题 3 道，复做 2 道，共 5 道  建议总限时：85 分钟  当日重点：数组与哈希、动态规划、区间与贪心

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 110 平衡二叉树](https://leetcode.com/problems/balanced-binary-tree/)<br>Balanced Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 自底向上递归 | 距首次 5 天<br>距上次 5 天 | 12 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 217 存在重复元素](https://leetcode.com/problems/contains-duplicate/)<br>Contains Duplicate<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 集合去重 | 首次学习 | 15 分钟 |
| 3 | ☐ | 新题<br>主练二 | [LeetCode 53 最大子数组和](https://leetcode.com/problems/maximum-subarray/)<br>Maximum Subarray<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | Kadane状态转移 | 首次学习 | 20 分钟 |
| 4 | ☐ | 短间隔复做<br>短测复做 | [LeetCode 141 环形链表](https://leetcode.com/problems/linked-list-cycle/)<br>Linked List Cycle<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 快慢指针 | 距首次 4 天<br>距上次 4 天 | 13 分钟 |
| 5 | ☐ | 新题<br>主练三 | [LeetCode 57 插入区间](https://leetcode.com/problems/insert-interval/)<br>Insert Interval<br>来源：Grind 75核心 | 中等 | 贪心与区间<br>区间与贪心 | 区间分类与合并 | 首次学习 | 25 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 平衡二叉树 | 未开始 |  |  |  |  |
| 2 | 存在重复元素 | 未开始 |  |  |  |  |
| 3 | 最大子数组和 | 未开始 |  |  |  |  |
| 4 | 环形链表 | 未开始 |  |  |  |  |
| 5 | 插入区间 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

### 阶段二 高频中等题主干

#### 第 9 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：98 分钟  当日重点：图论、堆与优先队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 383 赎金信](https://leetcode.com/problems/ransom-note/)<br>Ransom Note<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 字符频次计数 | 距首次 4 天<br>距上次 4 天 | 12 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 542 01矩阵](https://leetcode.com/problems/01-matrix/)<br>01 Matrix<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 多源广搜 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 70 爬楼梯](https://leetcode.com/problems/climbing-stairs/)<br>Climbing Stairs<br>来源：Grind 75核心 | 简单 | 动态规划<br>动态规划 | 一维状态转移 | 距首次 4 天<br>距上次 4 天 | 13 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 973 最接近原点的K个点](https://leetcode.com/problems/k-closest-points-to-origin/)<br>K Closest Points to Origin<br>来源：Grind 75核心 | 中等 | 堆与优先队列<br>堆与优先队列 | Top K与堆 | 首次学习 | 30 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 409 最长回文串](https://leetcode.com/problems/longest-palindrome/)<br>Longest Palindrome<br>来源：Grind 75核心 | 简单 | 字符串<br>字符串与哈希 | 频次奇偶性 | 距首次 4 天<br>距上次 4 天 | 13 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 赎金信 | 未开始 |  |  |  |  |
| 2 | 01矩阵 | 未开始 |  |  |  |  |
| 3 | 爬楼梯 | 未开始 |  |  |  |  |
| 4 | 最接近原点的K个点 | 未开始 |  |  |  |  |
| 5 | 最长回文串 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 10 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：98 分钟  当日重点：滑动窗口、双指针

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 206 反转链表](https://leetcode.com/problems/reverse-linked-list/)<br>Reverse Linked List<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 指针反转 | 距首次 4 天<br>距上次 4 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 3 无重复字符的最长子串](https://leetcode.com/problems/longest-substring-without-repeating-characters/)<br>Longest Substring Without Repeating Characters<br>来源：Grind 75核心 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 可变长度窗口 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 169 多数元素](https://leetcode.com/problems/majority-element/)<br>Majority Element<br>来源：Grind 75核心 | 简单 | 贪心与区间<br>数组与贪心 | Boyer Moore投票 | 距首次 4 天<br>距上次 4 天 | 13 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 15 三数之和](https://leetcode.com/problems/3sum/)<br>3Sum<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 排序与对撞指针 | 首次学习 | 30 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 67 二进制求和](https://leetcode.com/problems/add-binary/)<br>Add Binary<br>来源：Grind 75核心 | 简单 | 位运算<br>位运算与字符串 | 逐位模拟进位 | 距首次 4 天<br>距上次 4 天 | 12 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 反转链表 | 未开始 |  |  |  |  |
| 2 | 无重复字符的最长子串 | 未开始 |  |  |  |  |
| 3 | 多数元素 | 未开始 |  |  |  |  |
| 4 | 三数之和 | 未开始 |  |  |  |  |
| 5 | 二进制求和 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 11 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：83 分钟  当日重点：二叉树、图论

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 53 最大子数组和](https://leetcode.com/problems/maximum-subarray/)<br>Maximum Subarray<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | Kadane状态转移 | 距首次 3 天<br>距上次 3 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 102 二叉树的层序遍历](https://leetcode.com/problems/binary-tree-level-order-traversal/)<br>Binary Tree Level Order Traversal<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 广搜分层 | 首次学习 | 20 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 876 链表的中间结点](https://leetcode.com/problems/middle-of-the-linked-list/)<br>Middle of the Linked List<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 快慢指针 | 距首次 4 天<br>距上次 4 天 | 13 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 133 克隆图](https://leetcode.com/problems/clone-graph/)<br>Clone Graph<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 图遍历与映射 | 首次学习 | 25 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 217 存在重复元素](https://leetcode.com/problems/contains-duplicate/)<br>Contains Duplicate<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 集合去重 | 距首次 3 天<br>距上次 3 天 | 12 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 最大子数组和 | 未开始 |  |  |  |  |
| 2 | 二叉树的层序遍历 | 未开始 |  |  |  |  |
| 3 | 链表的中间结点 | 未开始 |  |  |  |  |
| 4 | 克隆图 | 未开始 |  |  |  |  |
| 5 | 存在重复元素 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 12 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：108 分钟  当日重点：栈与队列、图论

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 57 插入区间](https://leetcode.com/problems/insert-interval/)<br>Insert Interval<br>来源：Grind 75核心 | 中等 | 贪心与区间<br>区间与贪心 | 区间分类与合并 | 距首次 4 天<br>距上次 4 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 150 逆波兰表达式求值](https://leetcode.com/problems/evaluate-reverse-polish-notation/)<br>Evaluate Reverse Polish Notation<br>来源：Grind 75核心 | 中等 | 栈与队列<br>栈与队列 | 栈处理表达式 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 543 二叉树的直径](https://leetcode.com/problems/diameter-of-binary-tree/)<br>Diameter of Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 树形动态规划 | 距首次 5 天<br>距上次 5 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 207 课程表](https://leetcode.com/problems/course-schedule/)<br>Course Schedule<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 拓扑排序与环检测 | 首次学习 | 30 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 104 二叉树的最大深度](https://leetcode.com/problems/maximum-depth-of-binary-tree/)<br>Maximum Depth of Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 深搜或层序遍历 | 距首次 5 天<br>距上次 5 天 | 12 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 插入区间 | 未开始 |  |  |  |  |
| 2 | 逆波兰表达式求值 | 未开始 |  |  |  |  |
| 3 | 二叉树的直径 | 未开始 |  |  |  |  |
| 4 | 课程表 | 未开始 |  |  |  |  |
| 5 | 二叉树的最大深度 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 13 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：120 分钟  当日重点：Trie、动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 542 01矩阵](https://leetcode.com/problems/01-matrix/)<br>01 Matrix<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 多源广搜 | 距首次 4 天<br>距上次 4 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 208 实现Trie前缀树](https://leetcode.com/problems/implement-trie-prefix-tree/)<br>Implement Trie Prefix Tree<br>来源：Grind 75核心 | 中等 | Trie<br>Trie | 前缀树设计 | 首次学习 | 35 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 973 最接近原点的K个点](https://leetcode.com/problems/k-closest-points-to-origin/)<br>K Closest Points to Origin<br>来源：Grind 75核心 | 中等 | 堆与优先队列<br>堆与优先队列 | Top K与堆 | 距首次 4 天<br>距上次 4 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 322 零钱兑换](https://leetcode.com/problems/coin-change/)<br>Coin Change<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 完全背包最值 | 首次学习 | 25 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 3 无重复字符的最长子串](https://leetcode.com/problems/longest-substring-without-repeating-characters/)<br>Longest Substring Without Repeating Characters<br>来源：Grind 75核心 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 可变长度窗口 | 距首次 3 天<br>距上次 3 天 | 20 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 01矩阵 | 未开始 |  |  |  |  |
| 2 | 实现Trie前缀树 | 未开始 |  |  |  |  |
| 3 | 最接近原点的K个点 | 未开始 |  |  |  |  |
| 4 | 零钱兑换 | 未开始 |  |  |  |  |
| 5 | 无重复字符的最长子串 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 14 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：99 分钟  当日重点：数组与前缀、栈与队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 15 三数之和](https://leetcode.com/problems/3sum/)<br>3Sum<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 排序与对撞指针 | 距首次 4 天<br>距上次 4 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 238 除自身以外数组的乘积](https://leetcode.com/problems/product-of-array-except-self/)<br>Product of Array Except Self<br>来源：Grind 75核心 | 中等 | 数组与哈希<br>数组与前缀 | 前缀积与后缀积 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 102 二叉树的层序遍历](https://leetcode.com/problems/binary-tree-level-order-traversal/)<br>Binary Tree Level Order Traversal<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 广搜分层 | 距首次 3 天<br>距上次 3 天 | 13 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 155 最小栈](https://leetcode.com/problems/min-stack/)<br>Min Stack<br>来源：Grind 75核心 | 中等 | 栈与队列<br>栈与队列 | 辅助栈维护最值 | 首次学习 | 20 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 133 克隆图](https://leetcode.com/problems/clone-graph/)<br>Clone Graph<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 图遍历与映射 | 距首次 3 天<br>距上次 3 天 | 16 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 三数之和 | 未开始 |  |  |  |  |
| 2 | 除自身以外数组的乘积 | 未开始 |  |  |  |  |
| 3 | 二叉树的层序遍历 | 未开始 |  |  |  |  |
| 4 | 最小栈 | 未开始 |  |  |  |  |
| 5 | 克隆图 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 15 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：104 分钟  当日重点：二叉搜索树、图论

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 150 逆波兰表达式求值](https://leetcode.com/problems/evaluate-reverse-polish-notation/)<br>Evaluate Reverse Polish Notation<br>来源：Grind 75核心 | 中等 | 栈与队列<br>栈与队列 | 栈处理表达式 | 距首次 3 天<br>距上次 3 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 98 验证二叉搜索树](https://leetcode.com/problems/validate-binary-search-tree/)<br>Validate Binary Search Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 中序有序或上下界 | 首次学习 | 20 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 208 实现Trie前缀树](https://leetcode.com/problems/implement-trie-prefix-tree/)<br>Implement Trie Prefix Tree<br>来源：Grind 75核心 | 中等 | Trie<br>Trie | 前缀树设计 | 距首次 2 天<br>距上次 2 天 | 23 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 200 岛屿数量](https://leetcode.com/problems/number-of-islands/)<br>Number of Islands<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 网格连通分量 | 首次学习 | 25 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 322 零钱兑换](https://leetcode.com/problems/coin-change/)<br>Coin Change<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 完全背包最值 | 距首次 2 天<br>距上次 2 天 | 16 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 逆波兰表达式求值 | 未开始 |  |  |  |  |
| 2 | 验证二叉搜索树 | 未开始 |  |  |  |  |
| 3 | 实现Trie前缀树 | 未开始 |  |  |  |  |
| 4 | 岛屿数量 | 未开始 |  |  |  |  |
| 5 | 零钱兑换 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 16 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：113 分钟  当日重点：图论、二分查找

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 207 课程表](https://leetcode.com/problems/course-schedule/)<br>Course Schedule<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 拓扑排序与环检测 | 距首次 4 天<br>距上次 4 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 994 腐烂的橘子](https://leetcode.com/problems/rotting-oranges/)<br>Rotting Oranges<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 多源广搜分层 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 238 除自身以外数组的乘积](https://leetcode.com/problems/product-of-array-except-self/)<br>Product of Array Except Self<br>来源：Grind 75核心 | 中等 | 数组与哈希<br>数组与前缀 | 前缀积与后缀积 | 距首次 2 天<br>距上次 2 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 33 搜索旋转排序数组](https://leetcode.com/problems/search-in-rotated-sorted-array/)<br>Search in Rotated Sorted Array<br>来源：Grind 75核心 | 中等 | 二分查找<br>二分查找 | 有序半区判断 | 首次学习 | 30 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 155 最小栈](https://leetcode.com/problems/min-stack/)<br>Min Stack<br>来源：Grind 75核心 | 中等 | 栈与队列<br>栈与队列 | 辅助栈维护最值 | 距首次 2 天<br>距上次 2 天 | 13 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 课程表 | 未开始 |  |  |  |  |
| 2 | 腐烂的橘子 | 未开始 |  |  |  |  |
| 3 | 除自身以外数组的乘积 | 未开始 |  |  |  |  |
| 4 | 搜索旋转排序数组 | 未开始 |  |  |  |  |
| 5 | 最小栈 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 17 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：109 分钟  当日重点：回溯

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 98 验证二叉搜索树](https://leetcode.com/problems/validate-binary-search-tree/)<br>Validate Binary Search Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 中序有序或上下界 | 距首次 2 天<br>距上次 2 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 39 组合总和](https://leetcode.com/problems/combination-sum/)<br>Combination Sum<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 可重复选择的组合搜索 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 200 岛屿数量](https://leetcode.com/problems/number-of-islands/)<br>Number of Islands<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 网格连通分量 | 距首次 2 天<br>距上次 2 天 | 16 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 46 全排列](https://leetcode.com/problems/permutations/)<br>Permutations<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 排列搜索与使用标记 | 首次学习 | 30 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 33 搜索旋转排序数组](https://leetcode.com/problems/search-in-rotated-sorted-array/)<br>Search in Rotated Sorted Array<br>来源：Grind 75核心 | 中等 | 二分查找<br>二分查找 | 有序半区判断 | 距首次 1 天<br>距上次 1 天 | 20 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 验证二叉搜索树 | 未开始 |  |  |  |  |
| 2 | 组合总和 | 未开始 |  |  |  |  |
| 3 | 岛屿数量 | 未开始 |  |  |  |  |
| 4 | 全排列 | 未开始 |  |  |  |  |
| 5 | 搜索旋转排序数组 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 18 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：115 分钟  当日重点：区间与贪心、二叉树

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 994 腐烂的橘子](https://leetcode.com/problems/rotting-oranges/)<br>Rotting Oranges<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 多源广搜分层 | 距首次 2 天<br>距上次 2 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 56 合并区间](https://leetcode.com/problems/merge-intervals/)<br>Merge Intervals<br>来源：Grind 75核心 | 中等 | 贪心与区间<br>区间与贪心 | 排序后合并 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 39 组合总和](https://leetcode.com/problems/combination-sum/)<br>Combination Sum<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 可重复选择的组合搜索 | 距首次 1 天<br>距上次 1 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 236 二叉树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)<br>Lowest Common Ancestor of a Binary Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 后序递归汇总 | 首次学习 | 25 分钟 |
| 5 | ☐ | 短间隔复做<br>长间隔复做 | [LeetCode 46 全排列](https://leetcode.com/problems/permutations/)<br>Permutations<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 排列搜索与使用标记 | 距首次 1 天<br>距上次 1 天 | 20 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 腐烂的橘子 | 未开始 |  |  |  |  |
| 2 | 合并区间 | 未开始 |  |  |  |  |
| 3 | 组合总和 | 未开始 |  |  |  |  |
| 4 | 二叉树的最近公共祖先 | 未开始 |  |  |  |  |
| 5 | 全排列 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 19 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：111 分钟  当日重点：二分查找、图论

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 56 合并区间](https://leetcode.com/problems/merge-intervals/)<br>Merge Intervals<br>来源：Grind 75核心 | 中等 | 贪心与区间<br>区间与贪心 | 排序后合并 | 距首次 1 天<br>距上次 1 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 981 基于时间的键值存储](https://leetcode.com/problems/time-based-key-value-store/)<br>Time Based Key Value Store<br>来源：Grind 75核心 | 中等 | 二分查找<br>二分查找 | 时间序列二分 | 首次学习 | 35 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 236 二叉树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)<br>Lowest Common Ancestor of a Binary Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 后序递归汇总 | 距首次 1 天<br>距上次 1 天 | 16 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 721 账户合并](https://leetcode.com/problems/accounts-merge/)<br>Accounts Merge<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 并查集或图遍历 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 1 两数之和](https://leetcode.com/problems/two-sum/)<br>Two Sum<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 哈希表查补数 | 距首次 18 天<br>距上次 16 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 合并区间 | 未开始 |  |  |  |  |
| 2 | 基于时间的键值存储 | 未开始 |  |  |  |  |
| 3 | 二叉树的最近公共祖先 | 未开始 |  |  |  |  |
| 4 | 账户合并 | 未开始 |  |  |  |  |
| 5 | 两数之和 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 20 天

阶段：阶段二 高频中等题主干  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：108 分钟  当日重点：双指针、动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 981 基于时间的键值存储](https://leetcode.com/problems/time-based-key-value-store/)<br>Time Based Key Value Store<br>来源：Grind 75核心 | 中等 | 二分查找<br>二分查找 | 时间序列二分 | 距首次 1 天<br>距上次 1 天 | 23 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 75 颜色分类](https://leetcode.com/problems/sort-colors/)<br>Sort Colors<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 荷兰国旗三指针 | 首次学习 | 25 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 721 账户合并](https://leetcode.com/problems/accounts-merge/)<br>Accounts Merge<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 并查集或图遍历 | 距首次 1 天<br>距上次 1 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 139 单词拆分](https://leetcode.com/problems/word-break/)<br>Word Break<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 字符串划分状态转移 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 20 有效的括号](https://leetcode.com/problems/valid-parentheses/)<br>Valid Parentheses<br>来源：Grind 75核心 | 简单 | 栈与队列<br>栈与队列 | 栈与括号匹配 | 距首次 19 天<br>距上次 18 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 基于时间的键值存储 | 未开始 |  |  |  |  |
| 2 | 颜色分类 | 未开始 |  |  |  |  |
| 3 | 账户合并 | 未开始 |  |  |  |  |
| 4 | 单词拆分 | 未开始 |  |  |  |  |
| 5 | 有效的括号 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

### 阶段三 树图动态规划深化

#### 第 21 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：85 分钟  当日重点：动态规划、字符串与模拟

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>主动回忆热身 | [LeetCode 21 合并两个有序链表](https://leetcode.com/problems/merge-two-sorted-lists/)<br>Merge Two Sorted Lists<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 归并双指针 | 距首次 20 天<br>距上次 19 天 | 10 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 416 分割等和子集](https://leetcode.com/problems/partition-equal-subset-sum/)<br>Partition Equal Subset Sum<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 零一背包可行性 | 首次学习 | 30 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 121 买卖股票的最佳时机](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)<br>Best Time to Buy and Sell Stock<br>来源：Grind 75核心 | 简单 | 贪心与区间<br>数组与贪心 | 维护历史最小值 | 距首次 20 天<br>距上次 18 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 8 字符串转换整数](https://leetcode.com/problems/string-to-integer-atoi/)<br>String to Integer atoi<br>来源：Grind 75核心 | 中等 | 字符串<br>字符串与模拟 | 状态解析与溢出处理 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 125 验证回文串](https://leetcode.com/problems/valid-palindrome/)<br>Valid Palindrome<br>来源：Grind 75核心 | 简单 | 双指针<br>字符串与双指针 | 对撞指针 | 距首次 20 天<br>距上次 17 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 合并两个有序链表 | 未开始 |  |  |  |  |
| 2 | 分割等和子集 | 未开始 |  |  |  |  |
| 3 | 买卖股票的最佳时机 | 未开始 |  |  |  |  |
| 4 | 字符串转换整数 | 未开始 |  |  |  |  |
| 5 | 验证回文串 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 22 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：101 分钟  当日重点：矩阵与模拟、回溯

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 75 颜色分类](https://leetcode.com/problems/sort-colors/)<br>Sort Colors<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 荷兰国旗三指针 | 距首次 2 天<br>距上次 2 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 54 螺旋矩阵](https://leetcode.com/problems/spiral-matrix/)<br>Spiral Matrix<br>来源：Grind 75核心 | 中等 | 矩阵<br>矩阵与模拟 | 边界收缩模拟 | 首次学习 | 25 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 139 单词拆分](https://leetcode.com/problems/word-break/)<br>Word Break<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 字符串划分状态转移 | 距首次 2 天<br>距上次 2 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 78 子集](https://leetcode.com/problems/subsets/)<br>Subsets<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 子集型搜索 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 226 翻转二叉树](https://leetcode.com/problems/invert-binary-tree/)<br>Invert Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 递归遍历 | 距首次 20 天<br>距上次 18 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 颜色分类 | 未开始 |  |  |  |  |
| 2 | 螺旋矩阵 | 未开始 |  |  |  |  |
| 3 | 单词拆分 | 未开始 |  |  |  |  |
| 4 | 子集 | 未开始 |  |  |  |  |
| 5 | 翻转二叉树 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 23 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：85 分钟  当日重点：二叉树、字符串与动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 416 分割等和子集](https://leetcode.com/problems/partition-equal-subset-sum/)<br>Partition Equal Subset Sum<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 零一背包可行性 | 距首次 2 天<br>距上次 2 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 199 二叉树的右视图](https://leetcode.com/problems/binary-tree-right-side-view/)<br>Binary Tree Right Side View<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 层序遍历或右优先深搜 | 首次学习 | 20 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 242 有效的字母异位词](https://leetcode.com/problems/valid-anagram/)<br>Valid Anagram<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 字符频次计数 | 距首次 21 天<br>距上次 17 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 5 最长回文子串](https://leetcode.com/problems/longest-palindromic-substring/)<br>Longest Palindromic Substring<br>来源：Grind 75核心 | 中等 | 动态规划<br>字符串与动态规划 | 中心扩展 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 704 二分查找](https://leetcode.com/problems/binary-search/)<br>Binary Search<br>来源：Grind 75核心 | 简单 | 二分查找<br>二分查找 | 区间定义与循环不变量 | 距首次 21 天<br>距上次 18 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 分割等和子集 | 未开始 |  |  |  |  |
| 2 | 二叉树的右视图 | 未开始 |  |  |  |  |
| 3 | 有效的字母异位词 | 未开始 |  |  |  |  |
| 4 | 最长回文子串 | 未开始 |  |  |  |  |
| 5 | 二分查找 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 24 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：81 分钟  当日重点：动态规划、二叉树

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 8 字符串转换整数](https://leetcode.com/problems/string-to-integer-atoi/)<br>String to Integer atoi<br>来源：Grind 75核心 | 中等 | 字符串<br>字符串与模拟 | 状态解析与溢出处理 | 距首次 3 天<br>距上次 3 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 62 不同路径](https://leetcode.com/problems/unique-paths/)<br>Unique Paths<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 网格状态转移 | 首次学习 | 20 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 235 二叉搜索树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)<br>Lowest Common Ancestor of a Binary Search Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 利用有序性质缩小范围 | 距首次 21 天<br>距上次 18 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 105 从前序与中序遍历序列构造二叉树](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)<br>Construct Binary Tree from Preorder and Inorder Traversal<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 分治与索引映射 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 733 图像渲染](https://leetcode.com/problems/flood-fill/)<br>Flood Fill<br>来源：Grind 75核心 | 简单 | 图与并查集<br>图论 | 网格深搜或广搜 | 距首次 21 天<br>距上次 19 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 字符串转换整数 | 未开始 |  |  |  |  |
| 2 | 不同路径 | 未开始 |  |  |  |  |
| 3 | 二叉搜索树的最近公共祖先 | 未开始 |  |  |  |  |
| 4 | 从前序与中序遍历序列构造二叉树 | 未开始 |  |  |  |  |
| 5 | 图像渲染 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 25 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：101 分钟  当日重点：双指针、回溯

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 54 螺旋矩阵](https://leetcode.com/problems/spiral-matrix/)<br>Spiral Matrix<br>来源：Grind 75核心 | 中等 | 矩阵<br>矩阵与模拟 | 边界收缩模拟 | 距首次 3 天<br>距上次 3 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 11 盛最多水的容器](https://leetcode.com/problems/container-with-most-water/)<br>Container With Most Water<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 对撞指针与单调决策 | 首次学习 | 35 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 110 平衡二叉树](https://leetcode.com/problems/balanced-binary-tree/)<br>Balanced Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 自底向上递归 | 距首次 22 天<br>距上次 17 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 17 电话号码的字母组合](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)<br>Letter Combinations of a Phone Number<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 多叉树组合搜索 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 141 环形链表](https://leetcode.com/problems/linked-list-cycle/)<br>Linked List Cycle<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 快慢指针 | 距首次 21 天<br>距上次 17 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 螺旋矩阵 | 未开始 |  |  |  |  |
| 2 | 盛最多水的容器 | 未开始 |  |  |  |  |
| 3 | 平衡二叉树 | 未开始 |  |  |  |  |
| 4 | 电话号码的字母组合 | 未开始 |  |  |  |  |
| 5 | 环形链表 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 26 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：100 分钟  当日重点：回溯与图论、滑动窗口

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 78 子集](https://leetcode.com/problems/subsets/)<br>Subsets<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 子集型搜索 | 距首次 4 天<br>距上次 4 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 79 单词搜索](https://leetcode.com/problems/word-search/)<br>Word Search<br>来源：Grind 75核心 | 中等 | 图与并查集<br>回溯与图论 | 网格回溯 | 首次学习 | 30 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 232 用栈实现队列](https://leetcode.com/problems/implement-queue-using-stacks/)<br>Implement Queue using Stacks<br>来源：Grind 75核心 | 简单 | 栈与队列<br>栈与队列 | 双栈模拟 | 距首次 22 天<br>距上次 19 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 438 找到字符串中所有字母异位词](https://leetcode.com/problems/find-all-anagrams-in-a-string/)<br>Find All Anagrams in a String<br>来源：Grind 75核心 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 定长窗口与频次 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 278 第一个错误的版本](https://leetcode.com/problems/first-bad-version/)<br>First Bad Version<br>来源：Grind 75核心 | 简单 | 二分查找<br>二分查找 | 左边界查找 | 距首次 22 天<br>距上次 19 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 子集 | 未开始 |  |  |  |  |
| 2 | 单词搜索 | 未开始 |  |  |  |  |
| 3 | 用栈实现队列 | 未开始 |  |  |  |  |
| 4 | 找到字符串中所有字母异位词 | 未开始 |  |  |  |  |
| 5 | 第一个错误的版本 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 27 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：104 分钟  当日重点：图论、堆与贪心

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 199 二叉树的右视图](https://leetcode.com/problems/binary-tree-right-side-view/)<br>Binary Tree Right Side View<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 层序遍历或右优先深搜 | 距首次 4 天<br>距上次 4 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 310 最小高度树](https://leetcode.com/problems/minimum-height-trees/)<br>Minimum Height Trees<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 拓扑剥叶 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 5 最长回文子串](https://leetcode.com/problems/longest-palindromic-substring/)<br>Longest Palindromic Substring<br>来源：Grind 75核心 | 中等 | 动态规划<br>字符串与动态规划 | 中心扩展 | 距首次 4 天<br>距上次 4 天 | 16 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 621 任务调度器](https://leetcode.com/problems/task-scheduler/)<br>Task Scheduler<br>来源：Grind 75核心 | 中等 | 堆与优先队列<br>堆与贪心 | 频次计数与调度 | 首次学习 | 35 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 383 赎金信](https://leetcode.com/problems/ransom-note/)<br>Ransom Note<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 字符频次计数 | 距首次 22 天<br>距上次 18 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 二叉树的右视图 | 未开始 |  |  |  |  |
| 2 | 最小高度树 | 未开始 |  |  |  |  |
| 3 | 最长回文子串 | 未开始 |  |  |  |  |
| 4 | 任务调度器 | 未开始 |  |  |  |  |
| 5 | 赎金信 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 28 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：91 分钟  当日重点：设计、二叉搜索树

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 105 从前序与中序遍历序列构造二叉树](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)<br>Construct Binary Tree from Preorder and Inorder Traversal<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 分治与索引映射 | 距首次 4 天<br>距上次 4 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 146 LRU缓存](https://leetcode.com/problems/lru-cache/)<br>LRU Cache<br>来源：Grind 75核心 | 中等 | 设计<br>设计 | 哈希表与双向链表 | 首次学习 | 30 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 70 爬楼梯](https://leetcode.com/problems/climbing-stairs/)<br>Climbing Stairs<br>来源：Grind 75核心 | 简单 | 动态规划<br>动态规划 | 一维状态转移 | 距首次 23 天<br>距上次 19 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 230 二叉搜索树中第K小的元素](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)<br>Kth Smallest Element in a BST<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 中序遍历 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 409 最长回文串](https://leetcode.com/problems/longest-palindrome/)<br>Longest Palindrome<br>来源：Grind 75核心 | 简单 | 字符串<br>字符串与哈希 | 频次奇偶性 | 距首次 23 天<br>距上次 19 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 从前序与中序遍历序列构造二叉树 | 未开始 |  |  |  |  |
| 2 | LRU缓存 | 未开始 |  |  |  |  |
| 3 | 爬楼梯 | 未开始 |  |  |  |  |
| 4 | 二叉搜索树中第K小的元素 | 未开始 |  |  |  |  |
| 5 | 最长回文串 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 29 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：103 分钟  当日重点：滑动窗口、二叉树

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 62 不同路径](https://leetcode.com/problems/unique-paths/)<br>Unique Paths<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 网格状态转移 | 距首次 5 天<br>距上次 5 天 | 13 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 76 最小覆盖子串](https://leetcode.com/problems/minimum-window-substring/)<br>Minimum Window Substring<br>来源：Grind 75核心 | 困难 | 滑动窗口与单调队列<br>滑动窗口 | 满足条件后的收缩 | 首次学习 | 30 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 206 反转链表](https://leetcode.com/problems/reverse-linked-list/)<br>Reverse Linked List<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 指针反转 | 距首次 23 天<br>距上次 19 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 297 二叉树的序列化与反序列化](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)<br>Serialize and Deserialize Binary Tree<br>来源：Grind 75核心 | 困难 | 树与递归<br>二叉树 | 编解码与遍历 | 首次学习 | 40 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 169 多数元素](https://leetcode.com/problems/majority-element/)<br>Majority Element<br>来源：Grind 75核心 | 简单 | 贪心与区间<br>数组与贪心 | Boyer Moore投票 | 距首次 23 天<br>距上次 19 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 不同路径 | 未开始 |  |  |  |  |
| 2 | 最小覆盖子串 | 未开始 |  |  |  |  |
| 3 | 反转链表 | 未开始 |  |  |  |  |
| 4 | 二叉树的序列化与反序列化 | 未开始 |  |  |  |  |
| 5 | 多数元素 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 30 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：118 分钟  当日重点：单调栈与双指针、堆与优先队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 11 盛最多水的容器](https://leetcode.com/problems/container-with-most-water/)<br>Container With Most Water<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 对撞指针与单调决策 | 距首次 5 天<br>距上次 5 天 | 23 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 42 接雨水](https://leetcode.com/problems/trapping-rain-water/)<br>Trapping Rain Water<br>来源：Grind 75核心 | 困难 | 单调栈<br>单调栈与双指针 | 左右最大值或单调栈 | 首次学习 | 35 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 17 电话号码的字母组合](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)<br>Letter Combinations of a Phone Number<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 多叉树组合搜索 | 距首次 5 天<br>距上次 5 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 295 数据流的中位数](https://leetcode.com/problems/find-median-from-data-stream/)<br>Find Median from Data Stream<br>来源：Grind 75核心 | 困难 | 堆与优先队列<br>堆与优先队列 | 大小堆平衡 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 67 二进制求和](https://leetcode.com/problems/add-binary/)<br>Add Binary<br>来源：Grind 75核心 | 简单 | 位运算<br>位运算与字符串 | 逐位模拟进位 | 距首次 24 天<br>距上次 20 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 盛最多水的容器 | 未开始 |  |  |  |  |
| 2 | 接雨水 | 未开始 |  |  |  |  |
| 3 | 电话号码的字母组合 | 未开始 |  |  |  |  |
| 4 | 数据流的中位数 | 未开始 |  |  |  |  |
| 5 | 二进制求和 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 31 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：130 分钟  当日重点：图论、栈与队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 79 单词搜索](https://leetcode.com/problems/word-search/)<br>Word Search<br>来源：Grind 75核心 | 中等 | 图与并查集<br>回溯与图论 | 网格回溯 | 距首次 5 天<br>距上次 5 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 127 单词接龙](https://leetcode.com/problems/word-ladder/)<br>Word Ladder<br>来源：Grind 75核心 | 困难 | 图与并查集<br>图论 | 广搜最短路 | 首次学习 | 45 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 543 二叉树的直径](https://leetcode.com/problems/diameter-of-binary-tree/)<br>Diameter of Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 树形动态规划 | 距首次 24 天<br>距上次 19 天 | 15 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 224 基本计算器](https://leetcode.com/problems/basic-calculator/)<br>Basic Calculator<br>来源：Grind 75核心 | 困难 | 栈与队列<br>栈与队列 | 表达式解析 | 首次学习 | 40 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 876 链表的中间结点](https://leetcode.com/problems/middle-of-the-linked-list/)<br>Middle of the Linked List<br>来源：Grind 75核心 | 简单 | 链表<br>链表 | 快慢指针 | 距首次 24 天<br>距上次 20 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 单词搜索 | 未开始 |  |  |  |  |
| 2 | 单词接龙 | 未开始 |  |  |  |  |
| 3 | 二叉树的直径 | 未开始 |  |  |  |  |
| 4 | 基本计算器 | 未开始 |  |  |  |  |
| 5 | 链表的中间结点 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 32 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：115 分钟  当日重点：动态规划与二分、堆与链表

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 438 找到字符串中所有字母异位词](https://leetcode.com/problems/find-all-anagrams-in-a-string/)<br>Find All Anagrams in a String<br>来源：Grind 75核心 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 定长窗口与频次 | 距首次 6 天<br>距上次 6 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 1235 规划兼职工作](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)<br>Maximum Profit in Job Scheduling<br>来源：Grind 75核心 | 困难 | 动态规划<br>动态规划与二分 | 加权区间调度 | 首次学习 | 45 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 104 二叉树的最大深度](https://leetcode.com/problems/maximum-depth-of-binary-tree/)<br>Maximum Depth of Binary Tree<br>来源：Grind 75核心 | 简单 | 树与递归<br>二叉树 | 深搜或层序遍历 | 距首次 25 天<br>距上次 20 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 23 合并K个升序链表](https://leetcode.com/problems/merge-k-sorted-lists/)<br>Merge k Sorted Lists<br>来源：Grind 75核心 | 困难 | 堆与优先队列<br>堆与链表 | 多路归并 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 217 存在重复元素](https://leetcode.com/problems/contains-duplicate/)<br>Contains Duplicate<br>来源：Grind 75核心 | 简单 | 数组与哈希<br>数组与哈希 | 集合去重 | 距首次 24 天<br>距上次 21 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 找到字符串中所有字母异位词 | 未开始 |  |  |  |  |
| 2 | 规划兼职工作 | 未开始 |  |  |  |  |
| 3 | 二叉树的最大深度 | 未开始 |  |  |  |  |
| 4 | 合并K个升序链表 | 未开始 |  |  |  |  |
| 5 | 存在重复元素 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 33 天

阶段：阶段三 树图动态规划深化  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：92 分钟  当日重点：单调栈、双指针

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 310 最小高度树](https://leetcode.com/problems/minimum-height-trees/)<br>Minimum Height Trees<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 拓扑剥叶 | 距首次 6 天<br>距上次 6 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 84 柱状图中最大的矩形](https://leetcode.com/problems/largest-rectangle-in-histogram/)<br>Largest Rectangle in Histogram<br>来源：Grind 75核心 | 困难 | 单调栈<br>单调栈 | 寻找左右第一个更小值 | 首次学习 | 35 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 53 最大子数组和](https://leetcode.com/problems/maximum-subarray/)<br>Maximum Subarray<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | Kadane状态转移 | 距首次 25 天<br>距上次 22 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 27 移除元素](https://leetcode.com/problems/remove-element/)<br>Remove Element<br>来源：代码随想录补充 | 简单 | 双指针<br>双指针 | 快慢指针原地覆盖 | 首次学习 | 15 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 57 插入区间](https://leetcode.com/problems/insert-interval/)<br>Insert Interval<br>来源：Grind 75核心 | 中等 | 贪心与区间<br>区间与贪心 | 区间分类与合并 | 距首次 25 天<br>距上次 21 天 | 12 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 最小高度树 | 未开始 |  |  |  |  |
| 2 | 柱状图中最大的矩形 | 未开始 |  |  |  |  |
| 3 | 最大子数组和 | 未开始 |  |  |  |  |
| 4 | 移除元素 | 未开始 |  |  |  |  |
| 5 | 插入区间 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

### 阶段四 专题补强与难题

#### 第 34 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：103 分钟  当日重点：滑动窗口、链表

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 621 任务调度器](https://leetcode.com/problems/task-scheduler/)<br>Task Scheduler<br>来源：Grind 75核心 | 中等 | 堆与优先队列<br>堆与贪心 | 频次计数与调度 | 距首次 7 天<br>距上次 7 天 | 23 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 209 长度最小的子数组](https://leetcode.com/problems/minimum-size-subarray-sum/)<br>Minimum Size Subarray Sum<br>来源：代码随想录补充 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 最短满足窗口 | 首次学习 | 25 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 542 01矩阵](https://leetcode.com/problems/01-matrix/)<br>01 Matrix<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 多源广搜 | 距首次 25 天<br>距上次 21 天 | 15 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 19 删除链表的倒数第N个结点](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)<br>Remove Nth Node From End of List<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | 快慢指针与虚拟头结点 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 973 最接近原点的K个点](https://leetcode.com/problems/k-closest-points-to-origin/)<br>K Closest Points to Origin<br>来源：Grind 75核心 | 中等 | 堆与优先队列<br>堆与优先队列 | Top K与堆 | 距首次 25 天<br>距上次 21 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 任务调度器 | 未开始 |  |  |  |  |
| 2 | 长度最小的子数组 | 未开始 |  |  |  |  |
| 3 | 01矩阵 | 未开始 |  |  |  |  |
| 4 | 删除链表的倒数第N个结点 | 未开始 |  |  |  |  |
| 5 | 最接近原点的K个点 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 35 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：101 分钟  当日重点：链表

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 146 LRU缓存](https://leetcode.com/problems/lru-cache/)<br>LRU Cache<br>来源：Grind 75核心 | 中等 | 设计<br>设计 | 哈希表与双向链表 | 距首次 7 天<br>距上次 7 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 24 两两交换链表中的节点](https://leetcode.com/problems/swap-nodes-in-pairs/)<br>Swap Nodes in Pairs<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | 局部指针重连 | 首次学习 | 25 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 230 二叉搜索树中第K小的元素](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)<br>Kth Smallest Element in a BST<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 中序遍历 | 距首次 7 天<br>距上次 7 天 | 16 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 142 环形链表II](https://leetcode.com/problems/linked-list-cycle-ii/)<br>Linked List Cycle II<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | Floyd环入口推导 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 3 无重复字符的最长子串](https://leetcode.com/problems/longest-substring-without-repeating-characters/)<br>Longest Substring Without Repeating Characters<br>来源：Grind 75核心 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 可变长度窗口 | 距首次 25 天<br>距上次 22 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | LRU缓存 | 未开始 |  |  |  |  |
| 2 | 两两交换链表中的节点 | 未开始 |  |  |  |  |
| 3 | 二叉搜索树中第K小的元素 | 未开始 |  |  |  |  |
| 4 | 环形链表II | 未开始 |  |  |  |  |
| 5 | 无重复字符的最长子串 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 36 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：130 分钟  当日重点：前缀和与哈希、单调队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 76 最小覆盖子串](https://leetcode.com/problems/minimum-window-substring/)<br>Minimum Window Substring<br>来源：Grind 75核心 | 困难 | 滑动窗口与单调队列<br>滑动窗口 | 满足条件后的收缩 | 距首次 7 天<br>距上次 7 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 560 和为K的子数组](https://leetcode.com/problems/subarray-sum-equals-k/)<br>Subarray Sum Equals K<br>来源：Grind 169扩展 | 中等 | 数组与哈希<br>前缀和与哈希 | 前缀和频次计数 | 首次学习 | 35 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 297 二叉树的序列化与反序列化](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)<br>Serialize and Deserialize Binary Tree<br>来源：Grind 75核心 | 困难 | 树与递归<br>二叉树 | 编解码与遍历 | 距首次 7 天<br>距上次 7 天 | 25 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 239 滑动窗口最大值](https://leetcode.com/problems/sliding-window-maximum/)<br>Sliding Window Maximum<br>来源：代码随想录补充 | 困难 | 滑动窗口与单调队列<br>单调队列 | 维护单调双端队列 | 首次学习 | 35 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 15 三数之和](https://leetcode.com/problems/3sum/)<br>3Sum<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 排序与对撞指针 | 距首次 26 天<br>距上次 22 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 最小覆盖子串 | 未开始 |  |  |  |  |
| 2 | 和为K的子数组 | 未开始 |  |  |  |  |
| 3 | 二叉树的序列化与反序列化 | 未开始 |  |  |  |  |
| 4 | 滑动窗口最大值 | 未开始 |  |  |  |  |
| 5 | 三数之和 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 37 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：100 分钟  当日重点：堆与优先队列、二叉树

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 42 接雨水](https://leetcode.com/problems/trapping-rain-water/)<br>Trapping Rain Water<br>来源：Grind 75核心 | 困难 | 单调栈<br>单调栈与双指针 | 左右最大值或单调栈 | 距首次 7 天<br>距上次 7 天 | 23 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 347 前K个高频元素](https://leetcode.com/problems/top-k-frequent-elements/)<br>Top K Frequent Elements<br>来源：代码随想录补充 | 中等 | 堆与优先队列<br>堆与优先队列 | 频次统计与Top K | 首次学习 | 30 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 133 克隆图](https://leetcode.com/problems/clone-graph/)<br>Clone Graph<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 图遍历与映射 | 距首次 26 天<br>距上次 23 天 | 12 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 112 路径总和](https://leetcode.com/problems/path-sum/)<br>Path Sum<br>来源：代码随想录补充 | 简单 | 树与递归<br>二叉树 | 根到叶路径递归 | 首次学习 | 20 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 150 逆波兰表达式求值](https://leetcode.com/problems/evaluate-reverse-polish-notation/)<br>Evaluate Reverse Polish Notation<br>来源：Grind 75核心 | 中等 | 栈与队列<br>栈与队列 | 栈处理表达式 | 距首次 25 天<br>距上次 22 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 接雨水 | 未开始 |  |  |  |  |
| 2 | 前K个高频元素 | 未开始 |  |  |  |  |
| 3 | 克隆图 | 未开始 |  |  |  |  |
| 4 | 路径总和 | 未开始 |  |  |  |  |
| 5 | 逆波兰表达式求值 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 38 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：100 分钟  当日重点：回溯

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 295 数据流的中位数](https://leetcode.com/problems/find-median-from-data-stream/)<br>Find Median from Data Stream<br>来源：Grind 75核心 | 困难 | 堆与优先队列<br>堆与优先队列 | 大小堆平衡 | 距首次 8 天<br>距上次 8 天 | 20 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 77 组合](https://leetcode.com/problems/combinations/)<br>Combinations<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 组合搜索与剪枝 | 首次学习 | 25 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 102 二叉树的层序遍历](https://leetcode.com/problems/binary-tree-level-order-traversal/)<br>Binary Tree Level Order Traversal<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 广搜分层 | 距首次 27 天<br>距上次 24 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 40 组合总和II](https://leetcode.com/problems/combination-sum-ii/)<br>Combination Sum II<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 树层去重 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 207 课程表](https://leetcode.com/problems/course-schedule/)<br>Course Schedule<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 拓扑排序与环检测 | 距首次 26 天<br>距上次 22 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 数据流的中位数 | 未开始 |  |  |  |  |
| 2 | 组合 | 未开始 |  |  |  |  |
| 3 | 二叉树的层序遍历 | 未开始 |  |  |  |  |
| 4 | 组合总和II | 未开始 |  |  |  |  |
| 5 | 课程表 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 39 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：128 分钟  当日重点：回溯

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 127 单词接龙](https://leetcode.com/problems/word-ladder/)<br>Word Ladder<br>来源：Grind 75核心 | 困难 | 图与并查集<br>图论 | 广搜最短路 | 距首次 8 天<br>距上次 8 天 | 25 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 131 分割回文串](https://leetcode.com/problems/palindrome-partitioning/)<br>Palindrome Partitioning<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 分割型回溯 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 224 基本计算器](https://leetcode.com/problems/basic-calculator/)<br>Basic Calculator<br>来源：Grind 75核心 | 困难 | 栈与队列<br>栈与队列 | 表达式解析 | 距首次 8 天<br>距上次 8 天 | 25 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 47 全排列II](https://leetcode.com/problems/permutations-ii/)<br>Permutations II<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 排列去重 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 208 实现Trie前缀树](https://leetcode.com/problems/implement-trie-prefix-tree/)<br>Implement Trie Prefix Tree<br>来源：Grind 75核心 | 中等 | Trie<br>Trie | 前缀树设计 | 距首次 26 天<br>距上次 24 天 | 18 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 单词接龙 | 未开始 |  |  |  |  |
| 2 | 分割回文串 | 未开始 |  |  |  |  |
| 3 | 基本计算器 | 未开始 |  |  |  |  |
| 4 | 全排列II | 未开始 |  |  |  |  |
| 5 | 实现Trie前缀树 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 40 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：112 分钟  当日重点：贪心、区间与贪心

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 1235 规划兼职工作](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)<br>Maximum Profit in Job Scheduling<br>来源：Grind 75核心 | 困难 | 动态规划<br>动态规划与二分 | 加权区间调度 | 距首次 8 天<br>距上次 8 天 | 25 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 55 跳跃游戏](https://leetcode.com/problems/jump-game/)<br>Jump Game<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>贪心 | 维护最远覆盖范围 | 首次学习 | 25 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 23 合并K个升序链表](https://leetcode.com/problems/merge-k-sorted-lists/)<br>Merge k Sorted Lists<br>来源：Grind 75核心 | 困难 | 堆与优先队列<br>堆与链表 | 多路归并 | 距首次 8 天<br>距上次 8 天 | 20 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 435 无重叠区间](https://leetcode.com/problems/non-overlapping-intervals/)<br>Non overlapping Intervals<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>区间与贪心 | 按结束点调度 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 322 零钱兑换](https://leetcode.com/problems/coin-change/)<br>Coin Change<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 完全背包最值 | 距首次 27 天<br>距上次 25 天 | 12 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 规划兼职工作 | 未开始 |  |  |  |  |
| 2 | 跳跃游戏 | 未开始 |  |  |  |  |
| 3 | 合并K个升序链表 | 未开始 |  |  |  |  |
| 4 | 无重叠区间 | 未开始 |  |  |  |  |
| 5 | 零钱兑换 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 41 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：103 分钟  当日重点：区间与贪心、动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 84 柱状图中最大的矩形](https://leetcode.com/problems/largest-rectangle-in-histogram/)<br>Largest Rectangle in Histogram<br>来源：Grind 75核心 | 困难 | 单调栈<br>单调栈 | 寻找左右第一个更小值 | 距首次 8 天<br>距上次 8 天 | 23 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 452 用最少数量的箭引爆气球](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)<br>Minimum Number of Arrows to Burst Balloons<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>区间与贪心 | 区间交集 | 首次学习 | 30 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 238 除自身以外数组的乘积](https://leetcode.com/problems/product-of-array-except-self/)<br>Product of Array Except Self<br>来源：Grind 75核心 | 中等 | 数组与哈希<br>数组与前缀 | 前缀积与后缀积 | 距首次 27 天<br>距上次 25 天 | 15 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 198 打家劫舍](https://leetcode.com/problems/house-robber/)<br>House Robber<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 相邻约束一维状态 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 155 最小栈](https://leetcode.com/problems/min-stack/)<br>Min Stack<br>来源：Grind 75核心 | 中等 | 栈与队列<br>栈与队列 | 辅助栈维护最值 | 距首次 27 天<br>距上次 25 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 柱状图中最大的矩形 | 未开始 |  |  |  |  |
| 2 | 用最少数量的箭引爆气球 | 未开始 |  |  |  |  |
| 3 | 除自身以外数组的乘积 | 未开始 |  |  |  |  |
| 4 | 打家劫舍 | 未开始 |  |  |  |  |
| 5 | 最小栈 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 42 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：94 分钟  当日重点：动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 27 移除元素](https://leetcode.com/problems/remove-element/)<br>Remove Element<br>来源：代码随想录补充 | 简单 | 双指针<br>双指针 | 快慢指针原地覆盖 | 距首次 9 天<br>距上次 9 天 | 12 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 300 最长递增子序列](https://leetcode.com/problems/longest-increasing-subsequence/)<br>Longest Increasing Subsequence<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 序列状态或耐心排序 | 首次学习 | 30 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 98 验证二叉搜索树](https://leetcode.com/problems/validate-binary-search-tree/)<br>Validate Binary Search Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 中序有序或上下界 | 距首次 27 天<br>距上次 25 天 | 10 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 1143 最长公共子序列](https://leetcode.com/problems/longest-common-subsequence/)<br>Longest Common Subsequence<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 双序列状态转移 | 首次学习 | 30 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 200 岛屿数量](https://leetcode.com/problems/number-of-islands/)<br>Number of Islands<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 网格连通分量 | 距首次 27 天<br>距上次 25 天 | 12 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 移除元素 | 未开始 |  |  |  |  |
| 2 | 最长递增子序列 | 未开始 |  |  |  |  |
| 3 | 验证二叉搜索树 | 未开始 |  |  |  |  |
| 4 | 最长公共子序列 | 未开始 |  |  |  |  |
| 5 | 岛屿数量 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 43 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：107 分钟  当日重点：动态规划、单调栈

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 209 长度最小的子数组](https://leetcode.com/problems/minimum-size-subarray-sum/)<br>Minimum Size Subarray Sum<br>来源：代码随想录补充 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 最短满足窗口 | 距首次 9 天<br>距上次 9 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 72 编辑距离](https://leetcode.com/problems/edit-distance/)<br>Edit Distance<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 增删改二维状态 | 首次学习 | 35 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 19 删除链表的倒数第N个结点](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)<br>Remove Nth Node From End of List<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | 快慢指针与虚拟头结点 | 距首次 9 天<br>距上次 9 天 | 16 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 739 每日温度](https://leetcode.com/problems/daily-temperatures/)<br>Daily Temperatures<br>来源：代码随想录补充 | 中等 | 单调栈<br>单调栈 | 下一个更大元素 | 首次学习 | 25 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 994 腐烂的橘子](https://leetcode.com/problems/rotting-oranges/)<br>Rotting Oranges<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 多源广搜分层 | 距首次 27 天<br>距上次 25 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 长度最小的子数组 | 未开始 |  |  |  |  |
| 2 | 编辑距离 | 未开始 |  |  |  |  |
| 3 | 删除链表的倒数第N个结点 | 未开始 |  |  |  |  |
| 4 | 每日温度 | 未开始 |  |  |  |  |
| 5 | 腐烂的橘子 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 44 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：81 分钟  当日重点：位运算、位运算与动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 24 两两交换链表中的节点](https://leetcode.com/problems/swap-nodes-in-pairs/)<br>Swap Nodes in Pairs<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | 局部指针重连 | 距首次 9 天<br>距上次 9 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 136 只出现一次的数字](https://leetcode.com/problems/single-number/)<br>Single Number<br>来源：Grind 169扩展 | 简单 | 位运算<br>位运算 | 异或消除成对元素 | 首次学习 | 15 分钟 |
| 3 | ☐ | 长间隔复做<br>交错复盘 | [LeetCode 33 搜索旋转排序数组](https://leetcode.com/problems/search-in-rotated-sorted-array/)<br>Search in Rotated Sorted Array<br>来源：Grind 75核心 | 中等 | 二分查找<br>二分查找 | 有序半区判断 | 距首次 28 天<br>距上次 27 天 | 15 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 338 比特位计数](https://leetcode.com/problems/counting-bits/)<br>Counting Bits<br>来源：Grind 169扩展 | 简单 | 动态规划<br>位运算与动态规划 | 最低位递推 | 首次学习 | 20 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 39 组合总和](https://leetcode.com/problems/combination-sum/)<br>Combination Sum<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 可重复选择的组合搜索 | 距首次 27 天<br>距上次 26 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 两两交换链表中的节点 | 未开始 |  |  |  |  |
| 2 | 只出现一次的数字 | 未开始 |  |  |  |  |
| 3 | 搜索旋转排序数组 | 未开始 |  |  |  |  |
| 4 | 比特位计数 | 未开始 |  |  |  |  |
| 5 | 组合总和 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 45 天

阶段：阶段四 专题补强与难题  计划：新题 2 道，复做 3 道，共 5 道  建议总限时：119 分钟  当日重点：图论

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>主动回忆热身 | [LeetCode 142 环形链表II](https://leetcode.com/problems/linked-list-cycle-ii/)<br>Linked List Cycle II<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | Floyd环入口推导 | 距首次 10 天<br>距上次 10 天 | 16 分钟 |
| 2 | ☐ | 新题<br>主练一 | [LeetCode 684 冗余连接](https://leetcode.com/problems/redundant-connection/)<br>Redundant Connection<br>来源：代码随想录图论扩展 | 中等 | 图与并查集<br>图论 | 并查集检测成环 | 首次学习 | 30 分钟 |
| 3 | ☐ | 短间隔复做<br>交错复盘 | [LeetCode 560 和为K的子数组](https://leetcode.com/problems/subarray-sum-equals-k/)<br>Subarray Sum Equals K<br>来源：Grind 169扩展 | 中等 | 数组与哈希<br>前缀和与哈希 | 前缀和频次计数 | 距首次 9 天<br>距上次 9 天 | 23 分钟 |
| 4 | ☐ | 新题<br>主练二 | [LeetCode 210 课程表II](https://leetcode.com/problems/course-schedule-ii/)<br>Course Schedule II<br>来源：Grind 169扩展 | 中等 | 图与并查集<br>图论 | 拓扑排序输出路径 | 首次学习 | 35 分钟 |
| 5 | ☐ | 长间隔复做<br>长间隔复做 | [LeetCode 46 全排列](https://leetcode.com/problems/permutations/)<br>Permutations<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 排列搜索与使用标记 | 距首次 28 天<br>距上次 27 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 环形链表II | 未开始 |  |  |  |  |
| 2 | 冗余连接 | 未开始 |  |  |  |  |
| 3 | 和为K的子数组 | 未开始 |  |  |  |  |
| 4 | 课程表II | 未开始 |  |  |  |  |
| 5 | 全排列 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

### 阶段五 交错限时模拟

#### 第 46 天

阶段：阶段五 交错限时模拟  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：88 分钟  当日重点：交错复盘：堆与优先队列、区间与贪心、二叉树、单调队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 347 前K个高频元素](https://leetcode.com/problems/top-k-frequent-elements/)<br>Top K Frequent Elements<br>来源：代码随想录补充 | 中等 | 堆与优先队列<br>堆与优先队列 | 频次统计与Top K | 距首次 9 天<br>距上次 9 天 | 20 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 56 合并区间](https://leetcode.com/problems/merge-intervals/)<br>Merge Intervals<br>来源：Grind 75核心 | 中等 | 贪心与区间<br>区间与贪心 | 排序后合并 | 距首次 28 天<br>距上次 27 天 | 15 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 236 二叉树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)<br>Lowest Common Ancestor of a Binary Tree<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 后序递归汇总 | 距首次 28 天<br>距上次 27 天 | 12 分钟 |
| 4 | ☐ | 短间隔复做<br>进阶题 | [LeetCode 239 滑动窗口最大值](https://leetcode.com/problems/sliding-window-maximum/)<br>Sliding Window Maximum<br>来源：代码随想录补充 | 困难 | 滑动窗口与单调队列<br>单调队列 | 维护单调双端队列 | 距首次 10 天<br>距上次 10 天 | 23 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 981 基于时间的键值存储](https://leetcode.com/problems/time-based-key-value-store/)<br>Time Based Key Value Store<br>来源：Grind 75核心 | 中等 | 二分查找<br>二分查找 | 时间序列二分 | 距首次 27 天<br>距上次 26 天 | 18 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 前K个高频元素 | 未开始 |  |  |  |  |
| 2 | 合并区间 | 未开始 |  |  |  |  |
| 3 | 二叉树的最近公共祖先 | 未开始 |  |  |  |  |
| 4 | 滑动窗口最大值 | 未开始 |  |  |  |  |
| 5 | 基于时间的键值存储 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 47 天

阶段：阶段五 交错限时模拟  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：71 分钟  当日重点：交错复盘：二叉树、回溯、图论、动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 112 路径总和](https://leetcode.com/problems/path-sum/)<br>Path Sum<br>来源：代码随想录补充 | 简单 | 树与递归<br>二叉树 | 根到叶路径递归 | 距首次 10 天<br>距上次 10 天 | 13 分钟 |
| 2 | ☐ | 短间隔复做<br>模拟题一 | [LeetCode 77 组合](https://leetcode.com/problems/combinations/)<br>Combinations<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 组合搜索与剪枝 | 距首次 9 天<br>距上次 9 天 | 16 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 721 账户合并](https://leetcode.com/problems/accounts-merge/)<br>Accounts Merge<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 并查集或图遍历 | 距首次 28 天<br>距上次 27 天 | 15 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 139 单词拆分](https://leetcode.com/problems/word-break/)<br>Word Break<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 字符串划分状态转移 | 距首次 27 天<br>距上次 25 天 | 15 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 75 颜色分类](https://leetcode.com/problems/sort-colors/)<br>Sort Colors<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 荷兰国旗三指针 | 距首次 27 天<br>距上次 25 天 | 12 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 路径总和 | 未开始 |  |  |  |  |
| 2 | 组合 | 未开始 |  |  |  |  |
| 3 | 账户合并 | 未开始 |  |  |  |  |
| 4 | 单词拆分 | 未开始 |  |  |  |  |
| 5 | 颜色分类 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 48 天

阶段：阶段五 交错限时模拟  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：83 分钟  当日重点：交错复盘：回溯、贪心、区间与贪心、字符串与模拟

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 40 组合总和II](https://leetcode.com/problems/combination-sum-ii/)<br>Combination Sum II<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 树层去重 | 距首次 10 天<br>距上次 10 天 | 20 分钟 |
| 2 | ☐ | 短间隔复做<br>模拟题一 | [LeetCode 55 跳跃游戏](https://leetcode.com/problems/jump-game/)<br>Jump Game<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>贪心 | 维护最远覆盖范围 | 距首次 8 天<br>距上次 8 天 | 16 分钟 |
| 3 | ☐ | 短间隔复做<br>模拟题二 | [LeetCode 435 无重叠区间](https://leetcode.com/problems/non-overlapping-intervals/)<br>Non overlapping Intervals<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>区间与贪心 | 按结束点调度 | 距首次 8 天<br>距上次 8 天 | 20 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 8 字符串转换整数](https://leetcode.com/problems/string-to-integer-atoi/)<br>String to Integer atoi<br>来源：Grind 75核心 | 中等 | 字符串<br>字符串与模拟 | 状态解析与溢出处理 | 距首次 27 天<br>距上次 24 天 | 12 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 416 分割等和子集](https://leetcode.com/problems/partition-equal-subset-sum/)<br>Partition Equal Subset Sum<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 零一背包可行性 | 距首次 27 天<br>距上次 25 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 组合总和II | 未开始 |  |  |  |  |
| 2 | 跳跃游戏 | 未开始 |  |  |  |  |
| 3 | 无重叠区间 | 未开始 |  |  |  |  |
| 4 | 字符串转换整数 | 未开始 |  |  |  |  |
| 5 | 分割等和子集 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 49 天

阶段：阶段五 交错限时模拟  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：88 分钟  当日重点：交错复盘：回溯、区间与贪心、矩阵与模拟、动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 131 分割回文串](https://leetcode.com/problems/palindrome-partitioning/)<br>Palindrome Partitioning<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 分割型回溯 | 距首次 10 天<br>距上次 10 天 | 20 分钟 |
| 2 | ☐ | 短间隔复做<br>模拟题一 | [LeetCode 47 全排列II](https://leetcode.com/problems/permutations-ii/)<br>Permutations II<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 排列去重 | 距首次 10 天<br>距上次 10 天 | 20 分钟 |
| 3 | ☐ | 短间隔复做<br>模拟题二 | [LeetCode 452 用最少数量的箭引爆气球](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)<br>Minimum Number of Arrows to Burst Balloons<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>区间与贪心 | 区间交集 | 距首次 8 天<br>距上次 8 天 | 20 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 54 螺旋矩阵](https://leetcode.com/problems/spiral-matrix/)<br>Spiral Matrix<br>来源：Grind 75核心 | 中等 | 矩阵<br>矩阵与模拟 | 边界收缩模拟 | 距首次 27 天<br>距上次 24 天 | 12 分钟 |
| 5 | ☐ | 短间隔复做<br>错题回收 | [LeetCode 198 打家劫舍](https://leetcode.com/problems/house-robber/)<br>House Robber<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 相邻约束一维状态 | 距首次 8 天<br>距上次 8 天 | 16 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 分割回文串 | 未开始 |  |  |  |  |
| 2 | 全排列II | 未开始 |  |  |  |  |
| 3 | 用最少数量的箭引爆气球 | 未开始 |  |  |  |  |
| 4 | 螺旋矩阵 | 未开始 |  |  |  |  |
| 5 | 打家劫舍 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 50 天

阶段：阶段五 交错限时模拟  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：73 分钟  当日重点：交错复盘：动态规划、单调栈、回溯、字符串与动态规划

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 300 最长递增子序列](https://leetcode.com/problems/longest-increasing-subsequence/)<br>Longest Increasing Subsequence<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 序列状态或耐心排序 | 距首次 8 天<br>距上次 8 天 | 20 分钟 |
| 2 | ☐ | 短间隔复做<br>模拟题一 | [LeetCode 739 每日温度](https://leetcode.com/problems/daily-temperatures/)<br>Daily Temperatures<br>来源：代码随想录补充 | 中等 | 单调栈<br>单调栈 | 下一个更大元素 | 距首次 7 天<br>距上次 7 天 | 16 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 78 子集](https://leetcode.com/problems/subsets/)<br>Subsets<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 子集型搜索 | 距首次 28 天<br>距上次 24 天 | 15 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 5 最长回文子串](https://leetcode.com/problems/longest-palindromic-substring/)<br>Longest Palindromic Substring<br>来源：Grind 75核心 | 中等 | 动态规划<br>字符串与动态规划 | 中心扩展 | 距首次 27 天<br>距上次 23 天 | 12 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 199 二叉树的右视图](https://leetcode.com/problems/binary-tree-right-side-view/)<br>Binary Tree Right Side View<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 层序遍历或右优先深搜 | 距首次 27 天<br>距上次 23 天 | 10 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 最长递增子序列 | 未开始 |  |  |  |  |
| 2 | 每日温度 | 未开始 |  |  |  |  |
| 3 | 子集 | 未开始 |  |  |  |  |
| 4 | 最长回文子串 | 未开始 |  |  |  |  |
| 5 | 二叉树的右视图 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 51 天

阶段：阶段五 交错限时模拟  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：75 分钟  当日重点：交错复盘：动态规划、二叉树、回溯、双指针

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 1143 最长公共子序列](https://leetcode.com/problems/longest-common-subsequence/)<br>Longest Common Subsequence<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 双序列状态转移 | 距首次 9 天<br>距上次 9 天 | 20 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 62 不同路径](https://leetcode.com/problems/unique-paths/)<br>Unique Paths<br>来源：Grind 75核心 | 中等 | 动态规划<br>动态规划 | 网格状态转移 | 距首次 27 天<br>距上次 22 天 | 10 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 105 从前序与中序遍历序列构造二叉树](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)<br>Construct Binary Tree from Preorder and Inorder Traversal<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉树 | 分治与索引映射 | 距首次 27 天<br>距上次 23 天 | 12 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 17 电话号码的字母组合](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)<br>Letter Combinations of a Phone Number<br>来源：Grind 75核心 | 中等 | 回溯<br>回溯 | 多叉树组合搜索 | 距首次 26 天<br>距上次 21 天 | 15 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 11 盛最多水的容器](https://leetcode.com/problems/container-with-most-water/)<br>Container With Most Water<br>来源：Grind 75核心 | 中等 | 双指针<br>双指针 | 对撞指针与单调决策 | 距首次 26 天<br>距上次 21 天 | 18 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 最长公共子序列 | 未开始 |  |  |  |  |
| 2 | 不同路径 | 未开始 |  |  |  |  |
| 3 | 从前序与中序遍历序列构造二叉树 | 未开始 |  |  |  |  |
| 4 | 电话号码的字母组合 | 未开始 |  |  |  |  |
| 5 | 盛最多水的容器 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 52 天

阶段：阶段五 交错限时模拟  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：78 分钟  当日重点：交错复盘：位运算、位运算与动态规划、动态规划、滑动窗口

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 136 只出现一次的数字](https://leetcode.com/problems/single-number/)<br>Single Number<br>来源：Grind 169扩展 | 简单 | 位运算<br>位运算 | 异或消除成对元素 | 距首次 8 天<br>距上次 8 天 | 12 分钟 |
| 2 | ☐ | 短间隔复做<br>模拟题一 | [LeetCode 338 比特位计数](https://leetcode.com/problems/counting-bits/)<br>Counting Bits<br>来源：Grind 169扩展 | 简单 | 动态规划<br>位运算与动态规划 | 最低位递推 | 距首次 8 天<br>距上次 8 天 | 13 分钟 |
| 3 | ☐ | 短间隔复做<br>模拟题二 | [LeetCode 72 编辑距离](https://leetcode.com/problems/edit-distance/)<br>Edit Distance<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 增删改二维状态 | 距首次 9 天<br>距上次 9 天 | 23 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 438 找到字符串中所有字母异位词](https://leetcode.com/problems/find-all-anagrams-in-a-string/)<br>Find All Anagrams in a String<br>来源：Grind 75核心 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 定长窗口与频次 | 距首次 26 天<br>距上次 20 天 | 15 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 79 单词搜索](https://leetcode.com/problems/word-search/)<br>Word Search<br>来源：Grind 75核心 | 中等 | 图与并查集<br>回溯与图论 | 网格回溯 | 距首次 26 天<br>距上次 21 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 只出现一次的数字 | 未开始 |  |  |  |  |
| 2 | 比特位计数 | 未开始 |  |  |  |  |
| 3 | 编辑距离 | 未开始 |  |  |  |  |
| 4 | 找到字符串中所有字母异位词 | 未开始 |  |  |  |  |
| 5 | 单词搜索 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

### 阶段六 面试冲刺与错题回收

#### 第 53 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：88 分钟  当日重点：交错复盘：图论、堆与贪心、二叉搜索树、设计

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 短间隔复做<br>热身题 | [LeetCode 684 冗余连接](https://leetcode.com/problems/redundant-connection/)<br>Redundant Connection<br>来源：代码随想录图论扩展 | 中等 | 图与并查集<br>图论 | 并查集检测成环 | 距首次 8 天<br>距上次 8 天 | 20 分钟 |
| 2 | ☐ | 短间隔复做<br>模拟题一 | [LeetCode 210 课程表II](https://leetcode.com/problems/course-schedule-ii/)<br>Course Schedule II<br>来源：Grind 169扩展 | 中等 | 图与并查集<br>图论 | 拓扑排序输出路径 | 距首次 8 天<br>距上次 8 天 | 23 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 621 任务调度器](https://leetcode.com/problems/task-scheduler/)<br>Task Scheduler<br>来源：Grind 75核心 | 中等 | 堆与优先队列<br>堆与贪心 | 频次计数与调度 | 距首次 26 天<br>距上次 19 天 | 18 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 230 二叉搜索树中第K小的元素](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)<br>Kth Smallest Element in a BST<br>来源：Grind 75核心 | 中等 | 树与递归<br>二叉搜索树 | 中序遍历 | 距首次 25 天<br>距上次 18 天 | 12 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 146 LRU缓存](https://leetcode.com/problems/lru-cache/)<br>LRU Cache<br>来源：Grind 75核心 | 中等 | 设计<br>设计 | 哈希表与双向链表 | 距首次 25 天<br>距上次 18 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 冗余连接 | 未开始 |  |  |  |  |
| 2 | 课程表II | 未开始 |  |  |  |  |
| 3 | 任务调度器 | 未开始 |  |  |  |  |
| 4 | 二叉搜索树中第K小的元素 | 未开始 |  |  |  |  |
| 5 | LRU缓存 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 54 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：83 分钟  当日重点：交错复盘：图论、滑动窗口、二叉树、堆与优先队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>热身题 | [LeetCode 310 最小高度树](https://leetcode.com/problems/minimum-height-trees/)<br>Minimum Height Trees<br>来源：Grind 75核心 | 中等 | 图与并查集<br>图论 | 拓扑剥叶 | 距首次 27 天<br>距上次 21 天 | 15 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 76 最小覆盖子串](https://leetcode.com/problems/minimum-window-substring/)<br>Minimum Window Substring<br>来源：Grind 75核心 | 困难 | 滑动窗口与单调队列<br>滑动窗口 | 满足条件后的收缩 | 距首次 25 天<br>距上次 18 天 | 15 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 297 二叉树的序列化与反序列化](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)<br>Serialize and Deserialize Binary Tree<br>来源：Grind 75核心 | 困难 | 树与递归<br>二叉树 | 编解码与遍历 | 距首次 25 天<br>距上次 18 天 | 20 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 295 数据流的中位数](https://leetcode.com/problems/find-median-from-data-stream/)<br>Find Median from Data Stream<br>来源：Grind 75核心 | 困难 | 堆与优先队列<br>堆与优先队列 | 大小堆平衡 | 距首次 24 天<br>距上次 16 天 | 15 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 42 接雨水](https://leetcode.com/problems/trapping-rain-water/)<br>Trapping Rain Water<br>来源：Grind 75核心 | 困难 | 单调栈<br>单调栈与双指针 | 左右最大值或单调栈 | 距首次 24 天<br>距上次 17 天 | 18 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 最小高度树 | 未开始 |  |  |  |  |
| 2 | 最小覆盖子串 | 未开始 |  |  |  |  |
| 3 | 二叉树的序列化与反序列化 | 未开始 |  |  |  |  |
| 4 | 数据流的中位数 | 未开始 |  |  |  |  |
| 5 | 接雨水 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 55 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：93 分钟  当日重点：交错复盘：图论、栈与队列、动态规划与二分、单调栈

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>热身题 | [LeetCode 127 单词接龙](https://leetcode.com/problems/word-ladder/)<br>Word Ladder<br>来源：Grind 75核心 | 困难 | 图与并查集<br>图论 | 广搜最短路 | 距首次 24 天<br>距上次 16 天 | 20 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 224 基本计算器](https://leetcode.com/problems/basic-calculator/)<br>Basic Calculator<br>来源：Grind 75核心 | 困难 | 栈与队列<br>栈与队列 | 表达式解析 | 距首次 24 天<br>距上次 16 天 | 20 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 1235 规划兼职工作](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)<br>Maximum Profit in Job Scheduling<br>来源：Grind 75核心 | 困难 | 动态规划<br>动态规划与二分 | 加权区间调度 | 距首次 23 天<br>距上次 15 天 | 20 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 84 柱状图中最大的矩形](https://leetcode.com/problems/largest-rectangle-in-histogram/)<br>Largest Rectangle in Histogram<br>来源：Grind 75核心 | 困难 | 单调栈<br>单调栈 | 寻找左右第一个更小值 | 距首次 22 天<br>距上次 14 天 | 18 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 23 合并K个升序链表](https://leetcode.com/problems/merge-k-sorted-lists/)<br>Merge k Sorted Lists<br>来源：Grind 75核心 | 困难 | 堆与优先队列<br>堆与链表 | 多路归并 | 距首次 23 天<br>距上次 15 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 单词接龙 | 未开始 |  |  |  |  |
| 2 | 基本计算器 | 未开始 |  |  |  |  |
| 3 | 规划兼职工作 | 未开始 |  |  |  |  |
| 4 | 柱状图中最大的矩形 | 未开始 |  |  |  |  |
| 5 | 合并K个升序链表 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 56 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：70 分钟  当日重点：交错复盘：双指针、滑动窗口、链表、单调队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>热身题 | [LeetCode 27 移除元素](https://leetcode.com/problems/remove-element/)<br>Remove Element<br>来源：代码随想录补充 | 简单 | 双指针<br>双指针 | 快慢指针原地覆盖 | 距首次 23 天<br>距上次 14 天 | 10 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 209 长度最小的子数组](https://leetcode.com/problems/minimum-size-subarray-sum/)<br>Minimum Size Subarray Sum<br>来源：代码随想录补充 | 中等 | 滑动窗口与单调队列<br>滑动窗口 | 最短满足窗口 | 距首次 22 天<br>距上次 13 天 | 12 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 19 删除链表的倒数第N个结点](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)<br>Remove Nth Node From End of List<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | 快慢指针与虚拟头结点 | 距首次 22 天<br>距上次 13 天 | 12 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 239 滑动窗口最大值](https://leetcode.com/problems/sliding-window-maximum/)<br>Sliding Window Maximum<br>来源：代码随想录补充 | 困难 | 滑动窗口与单调队列<br>单调队列 | 维护单调双端队列 | 距首次 20 天<br>距上次 10 天 | 18 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 560 和为K的子数组](https://leetcode.com/problems/subarray-sum-equals-k/)<br>Subarray Sum Equals K<br>来源：Grind 169扩展 | 中等 | 数组与哈希<br>前缀和与哈希 | 前缀和频次计数 | 距首次 20 天<br>距上次 11 天 | 18 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 移除元素 | 未开始 |  |  |  |  |
| 2 | 长度最小的子数组 | 未开始 |  |  |  |  |
| 3 | 删除链表的倒数第N个结点 | 未开始 |  |  |  |  |
| 4 | 滑动窗口最大值 | 未开始 |  |  |  |  |
| 5 | 和为K的子数组 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 57 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：61 分钟  当日重点：交错复盘：二叉树、链表、回溯、堆与优先队列

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>热身题 | [LeetCode 112 路径总和](https://leetcode.com/problems/path-sum/)<br>Path Sum<br>来源：代码随想录补充 | 简单 | 树与递归<br>二叉树 | 根到叶路径递归 | 距首次 20 天<br>距上次 10 天 | 10 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 24 两两交换链表中的节点](https://leetcode.com/problems/swap-nodes-in-pairs/)<br>Swap Nodes in Pairs<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | 局部指针重连 | 距首次 22 天<br>距上次 13 天 | 12 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 142 环形链表II](https://leetcode.com/problems/linked-list-cycle-ii/)<br>Linked List Cycle II<br>来源：代码随想录补充 | 中等 | 链表<br>链表 | Floyd环入口推导 | 距首次 22 天<br>距上次 12 天 | 12 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 77 组合](https://leetcode.com/problems/combinations/)<br>Combinations<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 组合搜索与剪枝 | 距首次 19 天<br>距上次 10 天 | 12 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 347 前K个高频元素](https://leetcode.com/problems/top-k-frequent-elements/)<br>Top K Frequent Elements<br>来源：代码随想录补充 | 中等 | 堆与优先队列<br>堆与优先队列 | 频次统计与Top K | 距首次 20 天<br>距上次 11 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 路径总和 | 未开始 |  |  |  |  |
| 2 | 两两交换链表中的节点 | 未开始 |  |  |  |  |
| 3 | 环形链表II | 未开始 |  |  |  |  |
| 4 | 组合 | 未开始 |  |  |  |  |
| 5 | 前K个高频元素 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 58 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：69 分钟  当日重点：交错复盘：回溯、贪心、动态规划、区间与贪心

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>热身题 | [LeetCode 40 组合总和II](https://leetcode.com/problems/combination-sum-ii/)<br>Combination Sum II<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 树层去重 | 距首次 20 天<br>距上次 10 天 | 15 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 131 分割回文串](https://leetcode.com/problems/palindrome-partitioning/)<br>Palindrome Partitioning<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 分割型回溯 | 距首次 19 天<br>距上次 9 天 | 15 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 55 跳跃游戏](https://leetcode.com/problems/jump-game/)<br>Jump Game<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>贪心 | 维护最远覆盖范围 | 距首次 18 天<br>距上次 10 天 | 12 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 198 打家劫舍](https://leetcode.com/problems/house-robber/)<br>House Robber<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 相邻约束一维状态 | 距首次 17 天<br>距上次 9 天 | 12 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 435 无重叠区间](https://leetcode.com/problems/non-overlapping-intervals/)<br>Non overlapping Intervals<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>区间与贪心 | 按结束点调度 | 距首次 18 天<br>距上次 10 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 组合总和II | 未开始 |  |  |  |  |
| 2 | 分割回文串 | 未开始 |  |  |  |  |
| 3 | 跳跃游戏 | 未开始 |  |  |  |  |
| 4 | 打家劫舍 | 未开始 |  |  |  |  |
| 5 | 无重叠区间 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 59 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：72 分钟  当日重点：交错复盘：回溯、区间与贪心、动态规划、单调栈

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>热身题 | [LeetCode 47 全排列II](https://leetcode.com/problems/permutations-ii/)<br>Permutations II<br>来源：代码随想录补充 | 中等 | 回溯<br>回溯 | 排列去重 | 距首次 20 天<br>距上次 10 天 | 15 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 452 用最少数量的箭引爆气球](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)<br>Minimum Number of Arrows to Burst Balloons<br>来源：代码随想录补充 | 中等 | 贪心与区间<br>区间与贪心 | 区间交集 | 距首次 18 天<br>距上次 10 天 | 15 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 300 最长递增子序列](https://leetcode.com/problems/longest-increasing-subsequence/)<br>Longest Increasing Subsequence<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 序列状态或耐心排序 | 距首次 17 天<br>距上次 9 天 | 15 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 739 每日温度](https://leetcode.com/problems/daily-temperatures/)<br>Daily Temperatures<br>来源：代码随想录补充 | 中等 | 单调栈<br>单调栈 | 下一个更大元素 | 距首次 16 天<br>距上次 9 天 | 12 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 1143 最长公共子序列](https://leetcode.com/problems/longest-common-subsequence/)<br>Longest Common Subsequence<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 双序列状态转移 | 距首次 17 天<br>距上次 8 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 全排列II | 未开始 |  |  |  |  |
| 2 | 用最少数量的箭引爆气球 | 未开始 |  |  |  |  |
| 3 | 最长递增子序列 | 未开始 |  |  |  |  |
| 4 | 每日温度 | 未开始 |  |  |  |  |
| 5 | 最长公共子序列 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

#### 第 60 天

阶段：阶段六 面试冲刺与错题回收  计划：新题 0 道，复做 5 道，共 5 道  建议总限时：71 分钟  当日重点：交错复盘：位运算、位运算与动态规划、动态规划、图论

| 题次 | 完成 | 类型与角色 | 题目 | 难度 | 考点与主专题 | 核心模式 | 复习间隔 | 限时 |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :---: | ---: |
| 1 | ☐ | 长间隔复做<br>热身题 | [LeetCode 136 只出现一次的数字](https://leetcode.com/problems/single-number/)<br>Single Number<br>来源：Grind 169扩展 | 简单 | 位运算<br>位运算 | 异或消除成对元素 | 距首次 16 天<br>距上次 8 天 | 10 分钟 |
| 2 | ☐ | 长间隔复做<br>模拟题一 | [LeetCode 338 比特位计数](https://leetcode.com/problems/counting-bits/)<br>Counting Bits<br>来源：Grind 169扩展 | 简单 | 动态规划<br>位运算与动态规划 | 最低位递推 | 距首次 16 天<br>距上次 8 天 | 10 分钟 |
| 3 | ☐ | 长间隔复做<br>模拟题二 | [LeetCode 72 编辑距离](https://leetcode.com/problems/edit-distance/)<br>Edit Distance<br>来源：代码随想录补充 | 中等 | 动态规划<br>动态规划 | 增删改二维状态 | 距首次 17 天<br>距上次 8 天 | 18 分钟 |
| 4 | ☐ | 长间隔复做<br>进阶题 | [LeetCode 210 课程表II](https://leetcode.com/problems/course-schedule-ii/)<br>Course Schedule II<br>来源：Grind 169扩展 | 中等 | 图与并查集<br>图论 | 拓扑排序输出路径 | 距首次 15 天<br>距上次 7 天 | 18 分钟 |
| 5 | ☐ | 长间隔复做<br>错题回收 | [LeetCode 684 冗余连接](https://leetcode.com/problems/redundant-connection/)<br>Redundant Connection<br>来源：代码随想录图论扩展 | 中等 | 图与并查集<br>图论 | 并查集检测成环 | 距首次 15 天<br>距上次 7 天 | 15 分钟 |

##### 当日训练记录

| 题次 | 题目 | 状态 | 独立完成分 | 实际用时 | 错误标签 | 复盘笔记 |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | 只出现一次的数字 | 未开始 |  |  |  |  |
| 2 | 比特位计数 | 未开始 |  |  |  |  |
| 3 | 编辑距离 | 未开始 |  |  |  |  |
| 4 | 课程表II | 未开始 |  |  |  |  |
| 5 | 冗余连接 | 未开始 |  |  |  |  |

当日复盘：

________________________________________________________________________________

## 八 每日进度总览

初始状态中的完成数据均为零。实际执行后，可直接修改对应单元格。

| 指标 | 数值 | 指标 | 数值 |
| :--- | ---: | :--- | ---: |
| 计划任务 | 300 | 已完成 | 0 |
| 总体完成率 | 0% | 已完成新题 | 0 |
| 已完成复做 | 0 | 平均独立分 | 0 |

| 天数 | 阶段 | 新题数 | 复做数 | 计划题数 | 计划限时 | 已完成数 | 完成率 | 平均独立分 | 实际用时 | 当日重点 | 当日复盘 |
| :---: | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- | :--- |
| 1 | 阶段一 基础模式与语言热身 | 5 | 0 | 5 | 90 分钟 | 0 | 0% | 0 | 0 分钟 | 数组与哈希、栈与队列、链表、数组与贪心、字符串与双指针 |  |
| 2 | 阶段一 基础模式与语言热身 | 3 | 2 | 5 | 71 分钟 | 0 | 0% | 0 | 0 分钟 | 二叉树、数组与哈希、二分查找 |  |
| 3 | 阶段一 基础模式与语言热身 | 3 | 2 | 5 | 80 分钟 | 0 | 0% | 0 | 0 分钟 | 图论、二叉搜索树、二叉树 |  |
| 4 | 阶段一 基础模式与语言热身 | 3 | 2 | 5 | 84 分钟 | 0 | 0% | 0 | 0 分钟 | 链表、栈与队列、二分查找 |  |
| 5 | 阶段一 基础模式与语言热身 | 3 | 2 | 5 | 80 分钟 | 0 | 0% | 0 | 0 分钟 | 数组与哈希、动态规划、字符串与哈希 |  |
| 6 | 阶段一 基础模式与语言热身 | 3 | 2 | 5 | 80 分钟 | 0 | 0% | 0 | 0 分钟 | 链表、数组与贪心、位运算与字符串 |  |
| 7 | 阶段一 基础模式与语言热身 | 3 | 2 | 5 | 91 分钟 | 0 | 0% | 0 | 0 分钟 | 二叉树、链表 |  |
| 8 | 阶段一 基础模式与语言热身 | 3 | 2 | 5 | 85 分钟 | 0 | 0% | 0 | 0 分钟 | 数组与哈希、动态规划、区间与贪心 |  |
| 9 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 98 分钟 | 0 | 0% | 0 | 0 分钟 | 图论、堆与优先队列 |  |
| 10 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 98 分钟 | 0 | 0% | 0 | 0 分钟 | 滑动窗口、双指针 |  |
| 11 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 83 分钟 | 0 | 0% | 0 | 0 分钟 | 二叉树、图论 |  |
| 12 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 108 分钟 | 0 | 0% | 0 | 0 分钟 | 栈与队列、图论 |  |
| 13 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 120 分钟 | 0 | 0% | 0 | 0 分钟 | Trie、动态规划 |  |
| 14 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 99 分钟 | 0 | 0% | 0 | 0 分钟 | 数组与前缀、栈与队列 |  |
| 15 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 104 分钟 | 0 | 0% | 0 | 0 分钟 | 二叉搜索树、图论 |  |
| 16 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 113 分钟 | 0 | 0% | 0 | 0 分钟 | 图论、二分查找 |  |
| 17 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 109 分钟 | 0 | 0% | 0 | 0 分钟 | 回溯 |  |
| 18 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 115 分钟 | 0 | 0% | 0 | 0 分钟 | 区间与贪心、二叉树 |  |
| 19 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 111 分钟 | 0 | 0% | 0 | 0 分钟 | 二分查找、图论 |  |
| 20 | 阶段二 高频中等题主干 | 2 | 3 | 5 | 108 分钟 | 0 | 0% | 0 | 0 分钟 | 双指针、动态规划 |  |
| 21 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 85 分钟 | 0 | 0% | 0 | 0 分钟 | 动态规划、字符串与模拟 |  |
| 22 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 101 分钟 | 0 | 0% | 0 | 0 分钟 | 矩阵与模拟、回溯 |  |
| 23 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 85 分钟 | 0 | 0% | 0 | 0 分钟 | 二叉树、字符串与动态规划 |  |
| 24 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 81 分钟 | 0 | 0% | 0 | 0 分钟 | 动态规划、二叉树 |  |
| 25 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 101 分钟 | 0 | 0% | 0 | 0 分钟 | 双指针、回溯 |  |
| 26 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 100 分钟 | 0 | 0% | 0 | 0 分钟 | 回溯与图论、滑动窗口 |  |
| 27 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 104 分钟 | 0 | 0% | 0 | 0 分钟 | 图论、堆与贪心 |  |
| 28 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 91 分钟 | 0 | 0% | 0 | 0 分钟 | 设计、二叉搜索树 |  |
| 29 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 103 分钟 | 0 | 0% | 0 | 0 分钟 | 滑动窗口、二叉树 |  |
| 30 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 118 分钟 | 0 | 0% | 0 | 0 分钟 | 单调栈与双指针、堆与优先队列 |  |
| 31 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 130 分钟 | 0 | 0% | 0 | 0 分钟 | 图论、栈与队列 |  |
| 32 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 115 分钟 | 0 | 0% | 0 | 0 分钟 | 动态规划与二分、堆与链表 |  |
| 33 | 阶段三 树图动态规划深化 | 2 | 3 | 5 | 92 分钟 | 0 | 0% | 0 | 0 分钟 | 单调栈、双指针 |  |
| 34 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 103 分钟 | 0 | 0% | 0 | 0 分钟 | 滑动窗口、链表 |  |
| 35 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 101 分钟 | 0 | 0% | 0 | 0 分钟 | 链表 |  |
| 36 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 130 分钟 | 0 | 0% | 0 | 0 分钟 | 前缀和与哈希、单调队列 |  |
| 37 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 100 分钟 | 0 | 0% | 0 | 0 分钟 | 堆与优先队列、二叉树 |  |
| 38 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 100 分钟 | 0 | 0% | 0 | 0 分钟 | 回溯 |  |
| 39 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 128 分钟 | 0 | 0% | 0 | 0 分钟 | 回溯 |  |
| 40 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 112 分钟 | 0 | 0% | 0 | 0 分钟 | 贪心、区间与贪心 |  |
| 41 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 103 分钟 | 0 | 0% | 0 | 0 分钟 | 区间与贪心、动态规划 |  |
| 42 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 94 分钟 | 0 | 0% | 0 | 0 分钟 | 动态规划 |  |
| 43 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 107 分钟 | 0 | 0% | 0 | 0 分钟 | 动态规划、单调栈 |  |
| 44 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 81 分钟 | 0 | 0% | 0 | 0 分钟 | 位运算、位运算与动态规划 |  |
| 45 | 阶段四 专题补强与难题 | 2 | 3 | 5 | 119 分钟 | 0 | 0% | 0 | 0 分钟 | 图论 |  |
| 46 | 阶段五 交错限时模拟 | 0 | 5 | 5 | 88 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：堆与优先队列、区间与贪心、二叉树、单调队列 |  |
| 47 | 阶段五 交错限时模拟 | 0 | 5 | 5 | 71 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：二叉树、回溯、图论、动态规划 |  |
| 48 | 阶段五 交错限时模拟 | 0 | 5 | 5 | 83 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：回溯、贪心、区间与贪心、字符串与模拟 |  |
| 49 | 阶段五 交错限时模拟 | 0 | 5 | 5 | 88 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：回溯、区间与贪心、矩阵与模拟、动态规划 |  |
| 50 | 阶段五 交错限时模拟 | 0 | 5 | 5 | 73 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：动态规划、单调栈、回溯、字符串与动态规划 |  |
| 51 | 阶段五 交错限时模拟 | 0 | 5 | 5 | 75 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：动态规划、二叉树、回溯、双指针 |  |
| 52 | 阶段五 交错限时模拟 | 0 | 5 | 5 | 78 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：位运算、位运算与动态规划、动态规划、滑动窗口 |  |
| 53 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 88 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：图论、堆与贪心、二叉搜索树、设计 |  |
| 54 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 83 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：图论、滑动窗口、二叉树、堆与优先队列 |  |
| 55 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 93 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：图论、栈与队列、动态规划与二分、单调栈 |  |
| 56 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 70 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：双指针、滑动窗口、链表、单调队列 |  |
| 57 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 61 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：二叉树、链表、回溯、堆与优先队列 |  |
| 58 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 69 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：回溯、贪心、动态规划、区间与贪心 |  |
| 59 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 72 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：回溯、区间与贪心、动态规划、单调栈 |  |
| 60 | 阶段六 面试冲刺与错题回收 | 0 | 5 | 5 | 71 分钟 | 0 | 0% | 0 | 0 分钟 | 交错复盘：位运算、位运算与动态规划、动态规划、图论 |  |

## 九 一百道核心题库与复习窗口

Grind 75 核心为主，配合代码随想录和 Grind 169 补齐美国面试常见模式。

| 序号 | 题目 | 难度 | 考点大类 | 主专题 | 核心模式 | 来源 | 首做日 | 短间隔复做日 | 长间隔复做日 | 间隔结构 | 新题限时 |
| ---: | :--- | :---: | :--- | :--- | :--- | :--- | ---: | ---: | ---: | :---: | ---: |
| 1 | [LeetCode 1 两数之和](https://leetcode.com/problems/two-sum/)<br>Two Sum | 简单 | 数组与哈希 | 数组与哈希 | 哈希表查补数 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 1 | 3 | 19 | 首次 2 天<br>长期 18 天<br>两次复做 16 天 | 15 分钟 |
| 2 | [LeetCode 20 有效的括号](https://leetcode.com/problems/valid-parentheses/)<br>Valid Parentheses | 简单 | 栈与队列 | 栈与队列 | 栈与括号匹配 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 1 | 2 | 20 | 首次 1 天<br>长期 19 天<br>两次复做 18 天 | 20 分钟 |
| 3 | [LeetCode 21 合并两个有序链表](https://leetcode.com/problems/merge-two-sorted-lists/)<br>Merge Two Sorted Lists | 简单 | 链表 | 链表 | 归并双指针 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 1 | 2 | 21 | 首次 1 天<br>长期 20 天<br>两次复做 19 天 | 20 分钟 |
| 4 | [LeetCode 121 买卖股票的最佳时机](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)<br>Best Time to Buy and Sell Stock | 简单 | 贪心与区间 | 数组与贪心 | 维护历史最小值 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 1 | 3 | 21 | 首次 2 天<br>长期 20 天<br>两次复做 18 天 | 20 分钟 |
| 5 | [LeetCode 125 验证回文串](https://leetcode.com/problems/valid-palindrome/)<br>Valid Palindrome | 简单 | 双指针 | 字符串与双指针 | 对撞指针 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 1 | 4 | 21 | 首次 3 天<br>长期 20 天<br>两次复做 17 天 | 15 分钟 |
| 6 | [LeetCode 226 翻转二叉树](https://leetcode.com/problems/invert-binary-tree/)<br>Invert Binary Tree | 简单 | 树与递归 | 二叉树 | 递归遍历 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 2 | 4 | 22 | 首次 2 天<br>长期 20 天<br>两次复做 18 天 | 15 分钟 |
| 7 | [LeetCode 242 有效的字母异位词](https://leetcode.com/problems/valid-anagram/)<br>Valid Anagram | 简单 | 数组与哈希 | 数组与哈希 | 字符频次计数 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 2 | 6 | 23 | 首次 4 天<br>长期 21 天<br>两次复做 17 天 | 15 分钟 |
| 8 | [LeetCode 704 二分查找](https://leetcode.com/problems/binary-search/)<br>Binary Search | 简单 | 二分查找 | 二分查找 | 区间定义与循环不变量 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 2 | 5 | 23 | 首次 3 天<br>长期 21 天<br>两次复做 18 天 | 15 分钟 |
| 9 | [LeetCode 733 图像渲染](https://leetcode.com/problems/flood-fill/)<br>Flood Fill | 简单 | 图与并查集 | 图论 | 网格深搜或广搜 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 3 | 5 | 24 | 首次 2 天<br>长期 21 天<br>两次复做 19 天 | 20 分钟 |
| 10 | [LeetCode 235 二叉搜索树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)<br>Lowest Common Ancestor of a Binary Search Tree | 中等 | 树与递归 | 二叉搜索树 | 利用有序性质缩小范围 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 3 | 6 | 24 | 首次 3 天<br>长期 21 天<br>两次复做 18 天 | 20 分钟 |
| 11 | [LeetCode 110 平衡二叉树](https://leetcode.com/problems/balanced-binary-tree/)<br>Balanced Binary Tree | 简单 | 树与递归 | 二叉树 | 自底向上递归 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 3 | 8 | 25 | 首次 5 天<br>长期 22 天<br>两次复做 17 天 | 15 分钟 |
| 12 | [LeetCode 141 环形链表](https://leetcode.com/problems/linked-list-cycle/)<br>Linked List Cycle | 简单 | 链表 | 链表 | 快慢指针 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 4 | 8 | 25 | 首次 4 天<br>长期 21 天<br>两次复做 17 天 | 20 分钟 |
| 13 | [LeetCode 232 用栈实现队列](https://leetcode.com/problems/implement-queue-using-stacks/)<br>Implement Queue using Stacks | 简单 | 栈与队列 | 栈与队列 | 双栈模拟 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 4 | 7 | 26 | 首次 3 天<br>长期 22 天<br>两次复做 19 天 | 20 分钟 |
| 14 | [LeetCode 278 第一个错误的版本](https://leetcode.com/problems/first-bad-version/)<br>First Bad Version | 简单 | 二分查找 | 二分查找 | 左边界查找 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 4 | 7 | 26 | 首次 3 天<br>长期 22 天<br>两次复做 19 天 | 20 分钟 |
| 15 | [LeetCode 383 赎金信](https://leetcode.com/problems/ransom-note/)<br>Ransom Note | 简单 | 数组与哈希 | 数组与哈希 | 字符频次计数 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 5 | 9 | 27 | 首次 4 天<br>长期 22 天<br>两次复做 18 天 | 15 分钟 |
| 16 | [LeetCode 70 爬楼梯](https://leetcode.com/problems/climbing-stairs/)<br>Climbing Stairs | 简单 | 动态规划 | 动态规划 | 一维状态转移 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 5 | 9 | 28 | 首次 4 天<br>长期 23 天<br>两次复做 19 天 | 20 分钟 |
| 17 | [LeetCode 409 最长回文串](https://leetcode.com/problems/longest-palindrome/)<br>Longest Palindrome | 简单 | 字符串 | 字符串与哈希 | 频次奇偶性 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 5 | 9 | 28 | 首次 4 天<br>长期 23 天<br>两次复做 19 天 | 20 分钟 |
| 18 | [LeetCode 206 反转链表](https://leetcode.com/problems/reverse-linked-list/)<br>Reverse Linked List | 简单 | 链表 | 链表 | 指针反转 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 6 | 10 | 29 | 首次 4 天<br>长期 23 天<br>两次复做 19 天 | 20 分钟 |
| 19 | [LeetCode 169 多数元素](https://leetcode.com/problems/majority-element/)<br>Majority Element | 简单 | 贪心与区间 | 数组与贪心 | Boyer Moore投票 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 6 | 10 | 29 | 首次 4 天<br>长期 23 天<br>两次复做 19 天 | 20 分钟 |
| 20 | [LeetCode 67 二进制求和](https://leetcode.com/problems/add-binary/)<br>Add Binary | 简单 | 位运算 | 位运算与字符串 | 逐位模拟进位 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 6 | 10 | 30 | 首次 4 天<br>长期 24 天<br>两次复做 20 天 | 15 分钟 |
| 21 | [LeetCode 543 二叉树的直径](https://leetcode.com/problems/diameter-of-binary-tree/)<br>Diameter of Binary Tree | 简单 | 树与递归 | 二叉树 | 树形动态规划 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 7 | 12 | 31 | 首次 5 天<br>长期 24 天<br>两次复做 19 天 | 30 分钟 |
| 22 | [LeetCode 876 链表的中间结点](https://leetcode.com/problems/middle-of-the-linked-list/)<br>Middle of the Linked List | 简单 | 链表 | 链表 | 快慢指针 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 7 | 11 | 31 | 首次 4 天<br>长期 24 天<br>两次复做 20 天 | 20 分钟 |
| 23 | [LeetCode 104 二叉树的最大深度](https://leetcode.com/problems/maximum-depth-of-binary-tree/)<br>Maximum Depth of Binary Tree | 简单 | 树与递归 | 二叉树 | 深搜或层序遍历 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 7 | 12 | 32 | 首次 5 天<br>长期 25 天<br>两次复做 20 天 | 15 分钟 |
| 24 | [LeetCode 217 存在重复元素](https://leetcode.com/problems/contains-duplicate/)<br>Contains Duplicate | 简单 | 数组与哈希 | 数组与哈希 | 集合去重 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 8 | 11 | 32 | 首次 3 天<br>长期 24 天<br>两次复做 21 天 | 15 分钟 |
| 25 | [LeetCode 53 最大子数组和](https://leetcode.com/problems/maximum-subarray/)<br>Maximum Subarray | 中等 | 动态规划 | 动态规划 | Kadane状态转移 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 8 | 11 | 33 | 首次 3 天<br>长期 25 天<br>两次复做 22 天 | 20 分钟 |
| 26 | [LeetCode 57 插入区间](https://leetcode.com/problems/insert-interval/)<br>Insert Interval | 中等 | 贪心与区间 | 区间与贪心 | 区间分类与合并 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 8 | 12 | 33 | 首次 4 天<br>长期 25 天<br>两次复做 21 天 | 25 分钟 |
| 27 | [LeetCode 542 01矩阵](https://leetcode.com/problems/01-matrix/)<br>01 Matrix | 中等 | 图与并查集 | 图论 | 多源广搜 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 9 | 13 | 34 | 首次 4 天<br>长期 25 天<br>两次复做 21 天 | 30 分钟 |
| 28 | [LeetCode 973 最接近原点的K个点](https://leetcode.com/problems/k-closest-points-to-origin/)<br>K Closest Points to Origin | 中等 | 堆与优先队列 | 堆与优先队列 | Top K与堆 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 9 | 13 | 34 | 首次 4 天<br>长期 25 天<br>两次复做 21 天 | 30 分钟 |
| 29 | [LeetCode 3 无重复字符的最长子串](https://leetcode.com/problems/longest-substring-without-repeating-characters/)<br>Longest Substring Without Repeating Characters | 中等 | 滑动窗口与单调队列 | 滑动窗口 | 可变长度窗口 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 10 | 13 | 35 | 首次 3 天<br>长期 25 天<br>两次复做 22 天 | 30 分钟 |
| 30 | [LeetCode 15 三数之和](https://leetcode.com/problems/3sum/)<br>3Sum | 中等 | 双指针 | 双指针 | 排序与对撞指针 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 10 | 14 | 36 | 首次 4 天<br>长期 26 天<br>两次复做 22 天 | 30 分钟 |
| 31 | [LeetCode 102 二叉树的层序遍历](https://leetcode.com/problems/binary-tree-level-order-traversal/)<br>Binary Tree Level Order Traversal | 中等 | 树与递归 | 二叉树 | 广搜分层 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 11 | 14 | 38 | 首次 3 天<br>长期 27 天<br>两次复做 24 天 | 20 分钟 |
| 32 | [LeetCode 133 克隆图](https://leetcode.com/problems/clone-graph/)<br>Clone Graph | 中等 | 图与并查集 | 图论 | 图遍历与映射 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 11 | 14 | 37 | 首次 3 天<br>长期 26 天<br>两次复做 23 天 | 25 分钟 |
| 33 | [LeetCode 150 逆波兰表达式求值](https://leetcode.com/problems/evaluate-reverse-polish-notation/)<br>Evaluate Reverse Polish Notation | 中等 | 栈与队列 | 栈与队列 | 栈处理表达式 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 12 | 15 | 37 | 首次 3 天<br>长期 25 天<br>两次复做 22 天 | 30 分钟 |
| 34 | [LeetCode 207 课程表](https://leetcode.com/problems/course-schedule/)<br>Course Schedule | 中等 | 图与并查集 | 图论 | 拓扑排序与环检测 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 12 | 16 | 38 | 首次 4 天<br>长期 26 天<br>两次复做 22 天 | 30 分钟 |
| 35 | [LeetCode 208 实现Trie前缀树](https://leetcode.com/problems/implement-trie-prefix-tree/)<br>Implement Trie Prefix Tree | 中等 | Trie | Trie | 前缀树设计 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 13 | 15 | 39 | 首次 2 天<br>长期 26 天<br>两次复做 24 天 | 35 分钟 |
| 36 | [LeetCode 322 零钱兑换](https://leetcode.com/problems/coin-change/)<br>Coin Change | 中等 | 动态规划 | 动态规划 | 完全背包最值 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 13 | 15 | 40 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 25 分钟 |
| 37 | [LeetCode 238 除自身以外数组的乘积](https://leetcode.com/problems/product-of-array-except-self/)<br>Product of Array Except Self | 中等 | 数组与哈希 | 数组与前缀 | 前缀积与后缀积 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 14 | 16 | 41 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 30 分钟 |
| 38 | [LeetCode 155 最小栈](https://leetcode.com/problems/min-stack/)<br>Min Stack | 中等 | 栈与队列 | 栈与队列 | 辅助栈维护最值 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 14 | 16 | 41 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 20 分钟 |
| 39 | [LeetCode 98 验证二叉搜索树](https://leetcode.com/problems/validate-binary-search-tree/)<br>Validate Binary Search Tree | 中等 | 树与递归 | 二叉搜索树 | 中序有序或上下界 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 15 | 17 | 42 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 20 分钟 |
| 40 | [LeetCode 200 岛屿数量](https://leetcode.com/problems/number-of-islands/)<br>Number of Islands | 中等 | 图与并查集 | 图论 | 网格连通分量 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 15 | 17 | 42 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 25 分钟 |
| 41 | [LeetCode 994 腐烂的橘子](https://leetcode.com/problems/rotting-oranges/)<br>Rotting Oranges | 中等 | 图与并查集 | 图论 | 多源广搜分层 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 16 | 18 | 43 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 30 分钟 |
| 42 | [LeetCode 33 搜索旋转排序数组](https://leetcode.com/problems/search-in-rotated-sorted-array/)<br>Search in Rotated Sorted Array | 中等 | 二分查找 | 二分查找 | 有序半区判断 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 16 | 17 | 44 | 首次 1 天<br>长期 28 天<br>两次复做 27 天 | 30 分钟 |
| 43 | [LeetCode 39 组合总和](https://leetcode.com/problems/combination-sum/)<br>Combination Sum | 中等 | 回溯 | 回溯 | 可重复选择的组合搜索 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 17 | 18 | 44 | 首次 1 天<br>长期 27 天<br>两次复做 26 天 | 30 分钟 |
| 44 | [LeetCode 46 全排列](https://leetcode.com/problems/permutations/)<br>Permutations | 中等 | 回溯 | 回溯 | 排列搜索与使用标记 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 17 | 18 | 45 | 首次 1 天<br>长期 28 天<br>两次复做 27 天 | 30 分钟 |
| 45 | [LeetCode 56 合并区间](https://leetcode.com/problems/merge-intervals/)<br>Merge Intervals | 中等 | 贪心与区间 | 区间与贪心 | 排序后合并 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 18 | 19 | 46 | 首次 1 天<br>长期 28 天<br>两次复做 27 天 | 30 分钟 |
| 46 | [LeetCode 236 二叉树的最近公共祖先](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)<br>Lowest Common Ancestor of a Binary Tree | 中等 | 树与递归 | 二叉树 | 后序递归汇总 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 18 | 19 | 46 | 首次 1 天<br>长期 28 天<br>两次复做 27 天 | 25 分钟 |
| 47 | [LeetCode 981 基于时间的键值存储](https://leetcode.com/problems/time-based-key-value-store/)<br>Time Based Key Value Store | 中等 | 二分查找 | 二分查找 | 时间序列二分 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 19 | 20 | 46 | 首次 1 天<br>长期 27 天<br>两次复做 26 天 | 35 分钟 |
| 48 | [LeetCode 721 账户合并](https://leetcode.com/problems/accounts-merge/)<br>Accounts Merge | 中等 | 图与并查集 | 图论 | 并查集或图遍历 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 19 | 20 | 47 | 首次 1 天<br>长期 28 天<br>两次复做 27 天 | 30 分钟 |
| 49 | [LeetCode 75 颜色分类](https://leetcode.com/problems/sort-colors/)<br>Sort Colors | 中等 | 双指针 | 双指针 | 荷兰国旗三指针 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 20 | 22 | 47 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 25 分钟 |
| 50 | [LeetCode 139 单词拆分](https://leetcode.com/problems/word-break/)<br>Word Break | 中等 | 动态规划 | 动态规划 | 字符串划分状态转移 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 20 | 22 | 47 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 30 分钟 |
| 51 | [LeetCode 416 分割等和子集](https://leetcode.com/problems/partition-equal-subset-sum/)<br>Partition Equal Subset Sum | 中等 | 动态规划 | 动态规划 | 零一背包可行性 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 21 | 23 | 48 | 首次 2 天<br>长期 27 天<br>两次复做 25 天 | 30 分钟 |
| 52 | [LeetCode 8 字符串转换整数](https://leetcode.com/problems/string-to-integer-atoi/)<br>String to Integer atoi | 中等 | 字符串 | 字符串与模拟 | 状态解析与溢出处理 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 21 | 24 | 48 | 首次 3 天<br>长期 27 天<br>两次复做 24 天 | 25 分钟 |
| 53 | [LeetCode 54 螺旋矩阵](https://leetcode.com/problems/spiral-matrix/)<br>Spiral Matrix | 中等 | 矩阵 | 矩阵与模拟 | 边界收缩模拟 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 22 | 25 | 49 | 首次 3 天<br>长期 27 天<br>两次复做 24 天 | 25 分钟 |
| 54 | [LeetCode 78 子集](https://leetcode.com/problems/subsets/)<br>Subsets | 中等 | 回溯 | 回溯 | 子集型搜索 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 22 | 26 | 50 | 首次 4 天<br>长期 28 天<br>两次复做 24 天 | 30 分钟 |
| 55 | [LeetCode 199 二叉树的右视图](https://leetcode.com/problems/binary-tree-right-side-view/)<br>Binary Tree Right Side View | 中等 | 树与递归 | 二叉树 | 层序遍历或右优先深搜 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 23 | 27 | 50 | 首次 4 天<br>长期 27 天<br>两次复做 23 天 | 20 分钟 |
| 56 | [LeetCode 5 最长回文子串](https://leetcode.com/problems/longest-palindromic-substring/)<br>Longest Palindromic Substring | 中等 | 动态规划 | 字符串与动态规划 | 中心扩展 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 23 | 27 | 50 | 首次 4 天<br>长期 27 天<br>两次复做 23 天 | 25 分钟 |
| 57 | [LeetCode 62 不同路径](https://leetcode.com/problems/unique-paths/)<br>Unique Paths | 中等 | 动态规划 | 动态规划 | 网格状态转移 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 24 | 29 | 51 | 首次 5 天<br>长期 27 天<br>两次复做 22 天 | 20 分钟 |
| 58 | [LeetCode 105 从前序与中序遍历序列构造二叉树](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)<br>Construct Binary Tree from Preorder and Inorder Traversal | 中等 | 树与递归 | 二叉树 | 分治与索引映射 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 24 | 28 | 51 | 首次 4 天<br>长期 27 天<br>两次复做 23 天 | 25 分钟 |
| 59 | [LeetCode 11 盛最多水的容器](https://leetcode.com/problems/container-with-most-water/)<br>Container With Most Water | 中等 | 双指针 | 双指针 | 对撞指针与单调决策 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 25 | 30 | 51 | 首次 5 天<br>长期 26 天<br>两次复做 21 天 | 35 分钟 |
| 60 | [LeetCode 17 电话号码的字母组合](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)<br>Letter Combinations of a Phone Number | 中等 | 回溯 | 回溯 | 多叉树组合搜索 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 25 | 30 | 51 | 首次 5 天<br>长期 26 天<br>两次复做 21 天 | 30 分钟 |
| 61 | [LeetCode 79 单词搜索](https://leetcode.com/problems/word-search/)<br>Word Search | 中等 | 图与并查集 | 回溯与图论 | 网格回溯 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 26 | 31 | 52 | 首次 5 天<br>长期 26 天<br>两次复做 21 天 | 30 分钟 |
| 62 | [LeetCode 438 找到字符串中所有字母异位词](https://leetcode.com/problems/find-all-anagrams-in-a-string/)<br>Find All Anagrams in a String | 中等 | 滑动窗口与单调队列 | 滑动窗口 | 定长窗口与频次 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 26 | 32 | 52 | 首次 6 天<br>长期 26 天<br>两次复做 20 天 | 30 分钟 |
| 63 | [LeetCode 310 最小高度树](https://leetcode.com/problems/minimum-height-trees/)<br>Minimum Height Trees | 中等 | 图与并查集 | 图论 | 拓扑剥叶 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 27 | 33 | 54 | 首次 6 天<br>长期 27 天<br>两次复做 21 天 | 30 分钟 |
| 64 | [LeetCode 621 任务调度器](https://leetcode.com/problems/task-scheduler/)<br>Task Scheduler | 中等 | 堆与优先队列 | 堆与贪心 | 频次计数与调度 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 27 | 34 | 53 | 首次 7 天<br>长期 26 天<br>两次复做 19 天 | 35 分钟 |
| 65 | [LeetCode 146 LRU缓存](https://leetcode.com/problems/lru-cache/)<br>LRU Cache | 中等 | 设计 | 设计 | 哈希表与双向链表 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 28 | 35 | 53 | 首次 7 天<br>长期 25 天<br>两次复做 18 天 | 30 分钟 |
| 66 | [LeetCode 230 二叉搜索树中第K小的元素](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)<br>Kth Smallest Element in a BST | 中等 | 树与递归 | 二叉搜索树 | 中序遍历 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 28 | 35 | 53 | 首次 7 天<br>长期 25 天<br>两次复做 18 天 | 25 分钟 |
| 67 | [LeetCode 76 最小覆盖子串](https://leetcode.com/problems/minimum-window-substring/)<br>Minimum Window Substring | 困难 | 滑动窗口与单调队列 | 滑动窗口 | 满足条件后的收缩 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 29 | 36 | 54 | 首次 7 天<br>长期 25 天<br>两次复做 18 天 | 30 分钟 |
| 68 | [LeetCode 297 二叉树的序列化与反序列化](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)<br>Serialize and Deserialize Binary Tree | 困难 | 树与递归 | 二叉树 | 编解码与遍历 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 29 | 36 | 54 | 首次 7 天<br>长期 25 天<br>两次复做 18 天 | 40 分钟 |
| 69 | [LeetCode 42 接雨水](https://leetcode.com/problems/trapping-rain-water/)<br>Trapping Rain Water | 困难 | 单调栈 | 单调栈与双指针 | 左右最大值或单调栈 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 30 | 37 | 54 | 首次 7 天<br>长期 24 天<br>两次复做 17 天 | 35 分钟 |
| 70 | [LeetCode 295 数据流的中位数](https://leetcode.com/problems/find-median-from-data-stream/)<br>Find Median from Data Stream | 困难 | 堆与优先队列 | 堆与优先队列 | 大小堆平衡 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 30 | 38 | 54 | 首次 8 天<br>长期 24 天<br>两次复做 16 天 | 30 分钟 |
| 71 | [LeetCode 127 单词接龙](https://leetcode.com/problems/word-ladder/)<br>Word Ladder | 困难 | 图与并查集 | 图论 | 广搜最短路 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 31 | 39 | 55 | 首次 8 天<br>长期 24 天<br>两次复做 16 天 | 45 分钟 |
| 72 | [LeetCode 224 基本计算器](https://leetcode.com/problems/basic-calculator/)<br>Basic Calculator | 困难 | 栈与队列 | 栈与队列 | 表达式解析 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 31 | 39 | 55 | 首次 8 天<br>长期 24 天<br>两次复做 16 天 | 40 分钟 |
| 73 | [LeetCode 1235 规划兼职工作](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)<br>Maximum Profit in Job Scheduling | 困难 | 动态规划 | 动态规划与二分 | 加权区间调度 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 32 | 40 | 55 | 首次 8 天<br>长期 23 天<br>两次复做 15 天 | 45 分钟 |
| 74 | [LeetCode 23 合并K个升序链表](https://leetcode.com/problems/merge-k-sorted-lists/)<br>Merge k Sorted Lists | 困难 | 堆与优先队列 | 堆与链表 | 多路归并 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 32 | 40 | 55 | 首次 8 天<br>长期 23 天<br>两次复做 15 天 | 30 分钟 |
| 75 | [LeetCode 84 柱状图中最大的矩形](https://leetcode.com/problems/largest-rectangle-in-histogram/)<br>Largest Rectangle in Histogram | 困难 | 单调栈 | 单调栈 | 寻找左右第一个更小值 | [Grind 75核心](https://www.techinterviewhandbook.org/grind75/) | 33 | 41 | 55 | 首次 8 天<br>长期 22 天<br>两次复做 14 天 | 35 分钟 |
| 76 | [LeetCode 27 移除元素](https://leetcode.com/problems/remove-element/)<br>Remove Element | 简单 | 双指针 | 双指针 | 快慢指针原地覆盖 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 33 | 42 | 56 | 首次 9 天<br>长期 23 天<br>两次复做 14 天 | 15 分钟 |
| 77 | [LeetCode 209 长度最小的子数组](https://leetcode.com/problems/minimum-size-subarray-sum/)<br>Minimum Size Subarray Sum | 中等 | 滑动窗口与单调队列 | 滑动窗口 | 最短满足窗口 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 34 | 43 | 56 | 首次 9 天<br>长期 22 天<br>两次复做 13 天 | 25 分钟 |
| 78 | [LeetCode 19 删除链表的倒数第N个结点](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)<br>Remove Nth Node From End of List | 中等 | 链表 | 链表 | 快慢指针与虚拟头结点 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 34 | 43 | 56 | 首次 9 天<br>长期 22 天<br>两次复做 13 天 | 25 分钟 |
| 79 | [LeetCode 24 两两交换链表中的节点](https://leetcode.com/problems/swap-nodes-in-pairs/)<br>Swap Nodes in Pairs | 中等 | 链表 | 链表 | 局部指针重连 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 35 | 44 | 57 | 首次 9 天<br>长期 22 天<br>两次复做 13 天 | 25 分钟 |
| 80 | [LeetCode 142 环形链表II](https://leetcode.com/problems/linked-list-cycle-ii/)<br>Linked List Cycle II | 中等 | 链表 | 链表 | Floyd环入口推导 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 35 | 45 | 57 | 首次 10 天<br>长期 22 天<br>两次复做 12 天 | 25 分钟 |
| 81 | [LeetCode 560 和为K的子数组](https://leetcode.com/problems/subarray-sum-equals-k/)<br>Subarray Sum Equals K | 中等 | 数组与哈希 | 前缀和与哈希 | 前缀和频次计数 | [Grind 169扩展](https://www.techinterviewhandbook.org/grind75/?mode=all) | 36 | 45 | 56 | 首次 9 天<br>长期 20 天<br>两次复做 11 天 | 35 分钟 |
| 82 | [LeetCode 239 滑动窗口最大值](https://leetcode.com/problems/sliding-window-maximum/)<br>Sliding Window Maximum | 困难 | 滑动窗口与单调队列 | 单调队列 | 维护单调双端队列 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 36 | 46 | 56 | 首次 10 天<br>长期 20 天<br>两次复做 10 天 | 35 分钟 |
| 83 | [LeetCode 347 前K个高频元素](https://leetcode.com/problems/top-k-frequent-elements/)<br>Top K Frequent Elements | 中等 | 堆与优先队列 | 堆与优先队列 | 频次统计与Top K | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 37 | 46 | 57 | 首次 9 天<br>长期 20 天<br>两次复做 11 天 | 30 分钟 |
| 84 | [LeetCode 112 路径总和](https://leetcode.com/problems/path-sum/)<br>Path Sum | 简单 | 树与递归 | 二叉树 | 根到叶路径递归 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 37 | 47 | 57 | 首次 10 天<br>长期 20 天<br>两次复做 10 天 | 20 分钟 |
| 85 | [LeetCode 77 组合](https://leetcode.com/problems/combinations/)<br>Combinations | 中等 | 回溯 | 回溯 | 组合搜索与剪枝 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 38 | 47 | 57 | 首次 9 天<br>长期 19 天<br>两次复做 10 天 | 25 分钟 |
| 86 | [LeetCode 40 组合总和II](https://leetcode.com/problems/combination-sum-ii/)<br>Combination Sum II | 中等 | 回溯 | 回溯 | 树层去重 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 38 | 48 | 58 | 首次 10 天<br>长期 20 天<br>两次复做 10 天 | 30 分钟 |
| 87 | [LeetCode 131 分割回文串](https://leetcode.com/problems/palindrome-partitioning/)<br>Palindrome Partitioning | 中等 | 回溯 | 回溯 | 分割型回溯 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 39 | 49 | 58 | 首次 10 天<br>长期 19 天<br>两次复做 9 天 | 30 分钟 |
| 88 | [LeetCode 47 全排列II](https://leetcode.com/problems/permutations-ii/)<br>Permutations II | 中等 | 回溯 | 回溯 | 排列去重 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 39 | 49 | 59 | 首次 10 天<br>长期 20 天<br>两次复做 10 天 | 30 分钟 |
| 89 | [LeetCode 55 跳跃游戏](https://leetcode.com/problems/jump-game/)<br>Jump Game | 中等 | 贪心与区间 | 贪心 | 维护最远覆盖范围 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 40 | 48 | 58 | 首次 8 天<br>长期 18 天<br>两次复做 10 天 | 25 分钟 |
| 90 | [LeetCode 435 无重叠区间](https://leetcode.com/problems/non-overlapping-intervals/)<br>Non overlapping Intervals | 中等 | 贪心与区间 | 区间与贪心 | 按结束点调度 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 40 | 48 | 58 | 首次 8 天<br>长期 18 天<br>两次复做 10 天 | 30 分钟 |
| 91 | [LeetCode 452 用最少数量的箭引爆气球](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)<br>Minimum Number of Arrows to Burst Balloons | 中等 | 贪心与区间 | 区间与贪心 | 区间交集 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 41 | 49 | 59 | 首次 8 天<br>长期 18 天<br>两次复做 10 天 | 30 分钟 |
| 92 | [LeetCode 198 打家劫舍](https://leetcode.com/problems/house-robber/)<br>House Robber | 中等 | 动态规划 | 动态规划 | 相邻约束一维状态 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 41 | 49 | 58 | 首次 8 天<br>长期 17 天<br>两次复做 9 天 | 25 分钟 |
| 93 | [LeetCode 300 最长递增子序列](https://leetcode.com/problems/longest-increasing-subsequence/)<br>Longest Increasing Subsequence | 中等 | 动态规划 | 动态规划 | 序列状态或耐心排序 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 42 | 50 | 59 | 首次 8 天<br>长期 17 天<br>两次复做 9 天 | 30 分钟 |
| 94 | [LeetCode 1143 最长公共子序列](https://leetcode.com/problems/longest-common-subsequence/)<br>Longest Common Subsequence | 中等 | 动态规划 | 动态规划 | 双序列状态转移 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 42 | 51 | 59 | 首次 9 天<br>长期 17 天<br>两次复做 8 天 | 30 分钟 |
| 95 | [LeetCode 72 编辑距离](https://leetcode.com/problems/edit-distance/)<br>Edit Distance | 中等 | 动态规划 | 动态规划 | 增删改二维状态 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 43 | 52 | 60 | 首次 9 天<br>长期 17 天<br>两次复做 8 天 | 35 分钟 |
| 96 | [LeetCode 739 每日温度](https://leetcode.com/problems/daily-temperatures/)<br>Daily Temperatures | 中等 | 单调栈 | 单调栈 | 下一个更大元素 | [代码随想录补充](https://programmercarl.com/qita/12.list.html) | 43 | 50 | 59 | 首次 7 天<br>长期 16 天<br>两次复做 9 天 | 25 分钟 |
| 97 | [LeetCode 136 只出现一次的数字](https://leetcode.com/problems/single-number/)<br>Single Number | 简单 | 位运算 | 位运算 | 异或消除成对元素 | [Grind 169扩展](https://www.techinterviewhandbook.org/grind75/?mode=all) | 44 | 52 | 60 | 首次 8 天<br>长期 16 天<br>两次复做 8 天 | 15 分钟 |
| 98 | [LeetCode 338 比特位计数](https://leetcode.com/problems/counting-bits/)<br>Counting Bits | 简单 | 动态规划 | 位运算与动态规划 | 最低位递推 | [Grind 169扩展](https://www.techinterviewhandbook.org/grind75/?mode=all) | 44 | 52 | 60 | 首次 8 天<br>长期 16 天<br>两次复做 8 天 | 20 分钟 |
| 99 | [LeetCode 684 冗余连接](https://leetcode.com/problems/redundant-connection/)<br>Redundant Connection | 中等 | 图与并查集 | 图论 | 并查集检测成环 | [代码随想录图论扩展](https://programmercarl.com/qita/12.list.html) | 45 | 53 | 60 | 首次 8 天<br>长期 15 天<br>两次复做 7 天 | 30 分钟 |
| 100 | [LeetCode 210 课程表II](https://leetcode.com/problems/course-schedule-ii/)<br>Course Schedule II | 中等 | 图与并查集 | 图论 | 拓扑排序输出路径 | [Grind 169扩展](https://www.techinterviewhandbook.org/grind75/?mode=all) | 45 | 53 | 60 | 首次 8 天<br>长期 15 天<br>两次复做 7 天 | 35 分钟 |

## 十 题型覆盖与训练结构

统计按一百道核心题计算，每道题训练三次，因此训练次数等于核心题数的三倍。

### 考点大类分布

| 考点大类 | 核心题数 | 训练次数 | 占比 |
| :--- | ---: | ---: | ---: |
| 动态规划 | 13 | 39 | 13% |
| 树与递归 | 13 | 39 | 13% |
| 图与并查集 | 12 | 36 | 12% |
| 回溯 | 8 | 24 | 8% |
| 贪心与区间 | 7 | 21 | 7% |
| 链表 | 7 | 21 | 7% |
| 数组与哈希 | 6 | 18 | 6% |
| 双指针 | 5 | 15 | 5% |
| 堆与优先队列 | 5 | 15 | 5% |
| 栈与队列 | 5 | 15 | 5% |
| 滑动窗口与单调队列 | 5 | 15 | 5% |
| 二分查找 | 4 | 12 | 4% |
| 单调栈 | 3 | 9 | 3% |
| 位运算 | 2 | 6 | 2% |
| 字符串 | 2 | 6 | 2% |
| Trie | 1 | 3 | 1% |
| 矩阵 | 1 | 3 | 1% |
| 设计 | 1 | 3 | 1% |

### 难度分布

| 难度 | 核心题数 | 占比 |
| :--- | ---: | ---: |
| 简单 | 27 | 27% |
| 中等 | 63 | 63% |
| 困难 | 10 | 10% |

### 来源分布

| 来源 | 核心题数 | 占比 |
| :--- | ---: | ---: |
| Grind 75核心 | 75 | 75% |
| 代码随想录补充 | 20 | 20% |
| Grind 169扩展 | 4 | 4% |
| 代码随想录图论扩展 | 1 | 1% |

### 阶段训练量

| 阶段 | 天数 | 新题数 | 复做数 | 训练重点 |
| :--- | ---: | ---: | ---: | :--- |
| 阶段一 基础模式与语言热身 | 8 | 26 | 14 | 建立数组、哈希、链表、栈、树和二分的基础语言 |
| 阶段二 高频中等题主干 | 12 | 24 | 36 | 扩大高频中等题模式，开始稳定限时表达 |
| 阶段三 树图动态规划深化 | 13 | 26 | 39 | 深化树、图、回溯和动态规划，强化状态定义 |
| 阶段四 专题补强与难题 | 12 | 24 | 36 | 补齐区间、堆、单调结构、位运算和困难题 |
| 阶段五 交错限时模拟 | 7 | 0 | 35 | 跨专题限时模拟，减少依赖最近记忆 |
| 阶段六 面试冲刺与错题回收 | 8 | 0 | 40 | 面试冲刺，回收低分题和高频模式 |

### 主专题分布

| 主专题 | 核心题数 | 训练次数 | 占比 |
| :--- | ---: | ---: | ---: |
| 图论 | 11 | 33 | 11% |
| 二叉树 | 10 | 30 | 10% |
| 动态规划 | 10 | 30 | 10% |
| 回溯 | 8 | 24 | 8% |
| 链表 | 7 | 21 | 7% |
| 栈与队列 | 5 | 15 | 5% |
| 二分查找 | 4 | 12 | 4% |
| 区间与贪心 | 4 | 12 | 4% |
| 双指针 | 4 | 12 | 4% |
| 数组与哈希 | 4 | 12 | 4% |
| 滑动窗口 | 4 | 12 | 4% |
| 二叉搜索树 | 3 | 9 | 3% |
| 堆与优先队列 | 3 | 9 | 3% |
| 单调栈 | 2 | 6 | 2% |
| 数组与贪心 | 2 | 6 | 2% |
| Trie | 1 | 3 | 1% |
| 位运算 | 1 | 3 | 1% |
| 位运算与动态规划 | 1 | 3 | 1% |
| 位运算与字符串 | 1 | 3 | 1% |
| 前缀和与哈希 | 1 | 3 | 1% |
| 动态规划与二分 | 1 | 3 | 1% |
| 单调栈与双指针 | 1 | 3 | 1% |
| 单调队列 | 1 | 3 | 1% |
| 回溯与图论 | 1 | 3 | 1% |
| 堆与贪心 | 1 | 3 | 1% |
| 堆与链表 | 1 | 3 | 1% |
| 字符串与动态规划 | 1 | 3 | 1% |
| 字符串与双指针 | 1 | 3 | 1% |
| 字符串与哈希 | 1 | 3 | 1% |
| 字符串与模拟 | 1 | 3 | 1% |
| 数组与前缀 | 1 | 3 | 1% |
| 矩阵与模拟 | 1 | 3 | 1% |
| 设计 | 1 | 3 | 1% |
| 贪心 | 1 | 3 | 1% |

## 十一 错题复盘与修复记录

独立完成分为零或一时必须登记。根因要描述具体认知缺口，不只写粗心。

| 登记日期 | 计划日 | 题号 | 题目 | 当次得分 | 错误类型 | 根因 | 正确不变量 | 最小反例 | 修正方案 | 建议加练日 | 修复状态 | 面试表达 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |

### 单题复盘模板

登记日期：

计划日：

题号与题目：

当次得分：

错误类型：

根因：

正确不变量：

最小反例：

修正方案：

建议加练日：

修复状态：

面试表达：
