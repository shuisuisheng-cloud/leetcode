
"""
Day 12 - Problem 2
LeetCode 121. 买卖股票的最佳时机

给定一个长度为 n 的整数数组 prices。

prices[i] 表示第 i 天一支股票的价格。

你只能选择某一天买入股票，
然后在未来的某一天卖出股票。

请计算你能获得的最大利润。

要求：
1. 最多只能进行一次买入和一次卖出。
2. 必须先买入，再卖出。
3. 如果无法获得正利润，输出 0。

输入格式：
第一行：整数 n。
第二行:n 个空格分隔的整数 prices。

输出格式：
一行，一个整数，表示最大利润。

示例 1:
输入：
6
7 1 5 3 6 4

输出：
5

示例 2:
输入：
5
7 6 4 3 1

输出：
0

示例 3:
输入：
3
2 4 1

输出：
2

约束：
1 <= n <= 100000
0 <= prices[i] <= 10000
"""

import sys

def main():
    n=int(sys.stdin.readline())
    nums=list(map(int,sys.stdin.readline().split()))
    min_price=float('inf')
    max_profit=0
    for num in nums:
        if num<min_price:
            min_price=num
        if num-min_price>max_profit:
            max_profit=num-min_price
    print(max_profit)


if __name__ == "__main__":
    main()
