
"""
Day 12 - Problem 1
LeetCode 1. 两数之和（无提示复测）

给定一个整数数组 nums 和一个整数 target。

请在数组中找到两个不同位置的元素，
使得这两个元素之和等于 target。

输出这两个元素的下标。

要求：
1. 下标从 0 开始。
2. 不能使用同一个元素两次。
3. 保证有且仅有一组有效答案。
4. 输出两个下标，按从小到大排列。

输入格式：
第一行：整数 n,表示数组长度。
第二行:n 个空格分隔的整数。
第三行：整数 target。

输出格式：
一行，两个整数下标，用空格分隔。

示例 1:
输入：
4
2 7 11 15
9

输出：
0 1

示例 2:
输入：
3
3 2 4
6

输出：
1 2

示例 3:
输入：
2
3 3
6

输出：
0 1

约束：
2 <= n <= 100000
-10^9 <= nums[i], target <= 10^9
保证恰好存在一组有效答案。
"""

import sys

def main():
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    target=int(sys.stdin.readline())
    for index,num in enumerate(nums):
        target_num=target-num
        index_num=index+1
        while index_num <=n-1:
            if nums[index_num]==target_num:
                print(f"{index} {index_num}")
                return
            else:
                index_num+=1


if __name__ == "__main__":
    main()
