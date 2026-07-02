# """
# Day 7：两个数组的交集

# 题目：
# 给定两个整数数组 nums1 和 nums2，找出两个数组中共同出现的元素。

# 结果中的每个元素只能出现一次。

# 为保证 ACM 输出结果唯一，
# 按照元素在 nums1 中第一次出现的顺序输出交集。

# 输入格式：
# 第一行输入两个整数：
# n m

# 第二行输入 n 个整数：
# nums1[0] nums1[1] ... nums1[n-1]

# 第三行输入 m 个整数：
# nums2[0] nums2[1] ... nums2[m-1]

# 输出格式：
# 第一行输出交集元素的数量 k。
# 第二行输出 k 个交集元素。

# 如果没有交集：
# 第一行输出 0；
# 第二行输出空行。

# 样例输入 1：
# 4 2
# 1 2 2 1
# 2 2

# 样例输出 1：
# 1
# 2

# 样例输入 2：
# 3 5
# 4 9 5
# 9 4 9 8 4

# 样例输出 2：
# 2
# 4 9

# 样例输入 3：
# 3 3
# 1 2 3
# 4 5 6

# 样例输出 3：
# 0


# 约束：
# - 1 <= n, m <= 100000
# - -10^9 <= nums1[i], nums2[i] <= 10^9

# 要求：
# - 使用 Python
# - 自己处理 ACM 输入输出
# - 结果元素不能重复
# - 可以使用 set 或 dict
# - 不直接使用 set(nums1) & set(nums2)
# - 核心算法尽量达到 O(n + m)

# 难度：Easy
# 标签：数组、哈希集合、去重
# """

import sys


def main():
    # 我自己在这里读取输入、计算交集并输出结果
    a=list(map(int,sys.stdin.readline().split()))
    n1=a[0]
    n2=a[1]
    nums1=list(map(int,sys.stdin.readline().split()))
    nums2=list(map(int,sys.stdin.readline().split()))
    s=set(nums2)
    seen=set()
    result=[]
    for serial_data in nums1:
        if serial_data in s and serial_data not in seen:
            result.append(serial_data)
            seen.add(serial_data)
    k=len(result)
    print(k)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()


# """
# Day 7 总结：两个数组的交集

# 题型：
# 数组、哈希集合、去重

# 一、核心目标

# 给定两个数组 nums1 和 nums2，找出共同出现的元素。

# 要求：

# 1. 每个交集元素只能输出一次；
# 2. 按照元素在 nums1 中第一次出现的顺序输出。


# 二、核心思路

# 使用三个容器：

# 1. 查询集合 s

# s = set(nums2)

# 作用：
# 快速判断 nums1 中的元素是否也存在于 nums2。

# 集合查询的平均时间复杂度是 O(1)。


# 2. 去重集合 seen

# seen = set()

# 作用：
# 记录哪些交集元素已经加入结果，
# 防止同一个元素重复输出。


# 3. 结果列表 result

# result = []

# 作用：
# 按照 nums1 的遍历顺序保存最终答案。

# 列表会保留插入顺序，因此能满足题目要求。


# 三、处理流程

# 首先将 nums2 转换成集合：

# s = set(nums2)

# 然后按照原顺序遍历 nums1：

# for value in nums1:
#     if value in s and value not in seen:
#         result.append(value)
#         seen.add(value)

# 判断条件包括两部分：

# value in s

# 表示当前元素也存在于 nums2 中。

# value not in seen

# 表示当前元素还没有被加入结果，
# 用于避免重复。


# 四、为什么遍历 nums1？

# 题目要求：

# 按照元素在 nums1 中第一次出现的顺序输出。

# 因此必须按顺序遍历 nums1。

# 例如：

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

# 按照 nums1 遍历，结果是：

# [4, 9]

# 如果遍历 nums2，则可能得到：

# [9, 4]

# 不符合题目要求。


# 五、为什么不能只使用一个 set 保存答案？

# 如果直接写：

# result_set = set()

# 虽然可以去重，但集合不用于表达题目要求的顺序。

# 例如：

# result_set = {4, 9}

# 不能依赖集合的输出顺序一定是：

# 4 9

# 因此：

# seen 使用 set 负责去重；
# result 使用 list 负责保持顺序。


# 六、为什么不能写 s1 = s1.add(value)？

# set.add() 会直接修改原集合，但返回值是 None。

# 错误：

# s1 = s1.add(value)

# 执行后 s1 会变成：

# None

# 正确：

# s1.add(value)


# 七、为什么 map 不能直接取下标？

# 错误：

# a = map(int, sys.stdin.readline().split())
# n = a[0]

# map 返回的是可迭代对象，不支持直接使用下标。

# 正确：

# a = list(map(int, sys.stdin.readline().split()))
# n = a[0]
# m = a[1]


# 八、ACM 输入模板

# 读取 n 和 m：

# first_line = list(map(int, sys.stdin.readline().split()))
# n = first_line[0]
# m = first_line[1]

# 读取 nums1：

# nums1 = list(map(int, sys.stdin.readline().split()))

# 读取 nums2：

# nums2 = list(map(int, sys.stdin.readline().split()))


# 九、ACM 输出模板

# 输出交集元素数量：

# k = len(result)
# print(k)

# 输出空格分隔的结果：

# print(" ".join(map(str, result)))

# 如果 result 为空：

# result = []

# 那么：

# " ".join(map(str, result))

# 结果是空字符串，print() 会输出一个空行，
# 符合题目要求。


# 十、本题易错点

# 1. map 对象不能直接使用下标；
# 2. set.add() 返回 None，不能赋值回原集合；
# 3. 集合不能用于保证题目要求的输出顺序；
# 4. 只判断元素在 nums2 中，会导致重复输出；
# 5. 需要额外使用 seen 集合去重；
# 6. 最终结果应该保存在 list 中；
# 7. 不能直接 print(set)，否则会输出大括号；
# 8. 变量名不要使用小写 l，容易和数字 1 混淆。


# 十一、时间复杂度

# 假设：

# nums1 长度为 n；
# nums2 长度为 m。

# 把 nums2 转换成集合：

# O(m)

# 遍历 nums1：

# O(n)

# 集合查询和插入的平均时间复杂度为 O(1)。

# 总时间复杂度：

# O(n + m)


# 十二、空间复杂度

# s 最多保存 nums2 中的 m 个不同元素。

# seen 和 result 最多保存 k 个交集元素。

# 空间复杂度：

# O(m + k)

# 最坏情况下也可以写成：

# O(n + m)


# 十三、Python 常用模板

# 建立查询集合：

# lookup = set(nums)

# 判断元素是否存在：

# if value in lookup:

# 判断元素尚未处理：

# if value not in seen:

# 加入集合：

# seen.add(value)

# 加入结果列表：

# result.append(value)


# 十四、以后用 C++ 实现

# 数组：

# vector<int>

# 哈希集合：

# unordered_set<int>

# 结果列表：

# vector<int>

# 可能的结构：

# unordered_set<int> lookup(nums2.begin(), nums2.end());
# unordered_set<int> seen;
# vector<int> result;

# for (int value : nums1) {
#     if (lookup.count(value) && !seen.count(value)) {
#         result.push_back(value);
#         seen.insert(value);
#     }
# }


# 十五、面试表达

# 如果面试官问本题思路，可以回答：

# 我先将 nums2 放入哈希集合，用于 O(1) 平均复杂度地判断元素是否存在。

# 然后按顺序遍历 nums1。对于同时存在于 nums2 且尚未加入答案的元素，
# 将它加入 result，并用 seen 集合记录已经处理过的元素。

# result 使用列表是为了保持 nums1 中第一次出现的顺序，
# seen 使用集合是为了避免重复。

# 建立集合需要 O(m)，遍历 nums1 需要 O(n)，
# 因此总时间复杂度为 O(n + m)。

# 额外空间主要是查询集合和去重集合，
# 空间复杂度为 O(m + k)，最坏可记为 O(n + m)。
# """