# """
# Day 11 - 题目 1:移动零

# 题目描述：
# 给定一个长度为 n 的整数数组 nums。
# 请把数组中的所有 0 移动到数组末尾，
# 同时保持所有非零元素原来的相对顺序。

# 要求直接修改原数组内容。

# 输入格式：
# 第一行输入整数 n。
# 第二行输入 n 个整数。

# 输出格式：
# 输出处理后的数组，元素之间用一个空格分隔。

# 样例输入：
# 5
# 0 1 0 3 12

# 样例输出：
# 1 3 12 0 0

# 约束：
# - 1 <= n <= 100000
# - -10^9 <= nums[i] <= 10^9

# 要求：
# - 使用 Python
# - ACM 输入输出
# - 不使用 sorted()
# - 不创建另一个长度为 n 的结果数组
# """
import sys
def main():
    n=int(sys.stdin.readline().strip())
    nums=list(map(int,sys.stdin.readline().split()))
    left=0
    right=0
    while right<n:
        if nums[right]==0:
            right+=1
        else:
            nums[left],nums[right]=nums[right],nums[left]
            right+=1
            left+=1
    print(" ".join(map(str, nums)))

if __name__ == "__main__":
    main()