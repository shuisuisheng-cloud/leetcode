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