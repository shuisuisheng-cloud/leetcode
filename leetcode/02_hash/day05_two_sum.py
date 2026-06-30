# """
# Day 5：两数之和

# 题目：
# 给定一个长度为 n 的整数数组 nums 和一个整数 target。

# 请找出数组中两个不同位置的元素，使它们的和等于 target，
# 并输出这两个元素的下标。

# 题目保证恰好存在一个有效答案，并且同一个元素不能重复使用。
# 数组下标从 0 开始，输出时较小的下标放在前面。

# 输入格式：
# 第一行输入两个整数：
# n target

# 第二行输入 n 个整数：
# nums[0] nums[1] ... nums[n-1]

# 输出格式：
# 输出两个整数：
# index1 index2

# 其中 index1 < index2。

# 样例输入 1：
# 4 9
# 2 7 11 15

# 样例输出 1：
# 0 1

# 样例输入 2：
# 3 6
# 3 2 4

# 样例输出 2：
# 1 2

# 样例输入 3：
# 2 6
# 3 3

# 样例输出 3：
# 0 1

# 约束：
# - 2 <= n <= 100000
# - -10^9 <= nums[i] <= 10^9
# - -10^9 <= target <= 10^9
# - 恰好存在一个有效答案
# - 同一个数组元素不能重复使用

# 要求：
# - 使用 Python
# - 自己处理 ACM 输入输出
# - 不使用 list.index()
# - 尝试让核心算法达到 O(n)
# - 可以使用 Python 字典

# 难度：Easy
# 标签：数组、哈希表
# """

import sys


def main():
    # 我自己在这里读取输入、查找两个下标并输出
    first_line=list(map(int,sys.stdin.readline().split()))
    n=first_line[0]
    target=first_line[1]
    nums=list(map(int,sys.stdin.readline().split()))
    d={}
    i=0
    while i <n:
        another_num=target-nums[i]
        if another_num in d:
            print(d[another_num],i)
            return
        else:
            d[nums[i]]=i
        i+=1


if __name__ == "__main__":
    main()

# """
# Day 5 总结：两数之和

# 题型：
# 数组、哈希表

# 核心思路：
# 遍历数组时，假设当前元素为 nums[i]。

# 要找到另一个数字满足：

# nums[i] + another_num = target

# 因此：

# another_num = target - nums[i]

# 使用字典保存已经遍历过的元素：

# 数字 -> 该数字的下标

# 例如：

# d = {
#     2: 0,
#     7: 1
# }

# 当 another_num 已经存在于字典中时，说明之前出现过一个数字，
# 它与当前 nums[i] 的和等于 target。

# 此时两个下标分别是：

# d[another_num]
# i


# 为什么字典保存“当前数字”，而不是保存补数？

# 遍历到 nums[i] 时，如果没有找到答案，需要记录：

# d[nums[i]] = i

# 这样后面的元素计算出补数时，
# 就可以在字典中查到 nums[i] 以及它原来的下标。


# 为什么要先检查，再存入当前元素？

# 正确顺序：

# 1. 计算补数 another_num
# 2. 检查补数是否在字典中
# 3. 如果不存在，再保存当前元素

# 这样可以避免同一个元素被重复使用。

# 例如：

# nums = [3, 3]
# target = 6

# 遍历第一个 3 时：
# - 补数是 3
# - 字典里还没有 3
# - 保存 3 -> 0

# 遍历第二个 3 时：
# - 补数是 3
# - 字典中已经有 3 -> 0
# - 输出 0 1


# 字典的核心操作：

# 创建空字典：

# d = {}

# 保存键值对：

# d[nums[i]] = i

# 判断某个键是否存在：

# if another_num in d:

# 根据键获取对应的值：

# d[another_num]


# 找到答案后为什么要 return？

# 题目保证恰好存在一个有效答案。

# 找到并输出以后：

# print(d[another_num], i)
# return

# 可以立即结束 main()，
# 避免继续进行没有意义的遍历。


# ACM 输入模板：

# 读取 n 和 target：

# first_line = list(map(int, sys.stdin.readline().split()))
# n = first_line[0]
# target = first_line[1]

# 读取数组：

# nums = list(map(int, sys.stdin.readline().split()))


# 时间复杂度：

# O(n)

# 原因：
# 数组只遍历一次。

# 字典的查找和插入在平均情况下都是 O(1)，
# 所以 n 次遍历的总时间复杂度为 O(n)。


# 空间复杂度：

# O(n)

# 原因：
# 最坏情况下，字典需要保存数组中接近 n 个元素及其下标。


# 本题易错点：

# 1. sys.stdin.readline() 读取后要使用 split()

# 2. 第一行需要转换成整数列表，不能直接对字符串取下标

# 3. 字典没有 add() 方法

# 错误：

# d.add(...)

# 正确：

# d[nums[i]] = i

# 4. 字典需要保存：

# 数字 -> 下标

# 不能只保存数字，否则找到补数后无法输出下标。

# 5. 找到补数后要输出两个下标：

# d[another_num], i

# 6. 找到答案后最好立即 return

# 7. 必须先检查补数，再保存当前元素，
# 避免同一个元素重复使用


# Python 常用模板：

# seen = {}

# for i in range(len(nums)):
#     another_num = target - nums[i]

#     if another_num in seen:
#         print(seen[another_num], i)
#         return

#     seen[nums[i]] = i


# 以后使用 C++ 实现时：

# 数组容器：

# vector<int>

# 哈希表：

# unordered_map<int, int>

# 含义同样是：

# 数字 -> 下标

# 常用操作：

# unordered_map<int, int> seen;

# 判断键是否存在：

# seen.find(another_num) != seen.end()

# 保存数字和下标：

# seen[nums[i]] = i;
# """