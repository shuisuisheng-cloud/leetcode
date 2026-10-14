
"""
Day 12 - Problem 3
LeetCode 169. 多数元素

给定一个长度为 n 的整数数组 nums。

数组中存在一个“多数元素”。

多数元素的定义：
在数组中出现次数严格大于 floor(n / 2)
的元素。

请找出并输出这个多数元素。

要求：
1. 保证数组中一定存在多数元素。
2. 输出这个元素的数值，而不是下标。
3. 可以使用 Python 标准库。

输入格式：
第一行：整数 n。
第二行:n 个空格分隔的整数 nums。

输出格式：
一行，一个整数，表示多数元素。

示例 1:
输入：
3
3 2 3

输出：
3

示例 2:
输入：
7
2 2 1 1 1 2 2

输出：
2

示例 3:
输入：
5
-1 2 -1 -1 3

输出：
-1

约束：
1 <= n <= 100000
-10^9 <= nums[i] <= 10^9

保证多数元素存在。
"""

import sys

def main():
    seen={}
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    for num in nums:
        if num not in seen:
            seen[num]=1
        else:
            seen[num]+=1
    print(f"{max(seen,key=seen.get)}")


if __name__ == "__main__":
    main()
