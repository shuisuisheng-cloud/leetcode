# 题目：移除元素
# 难度：Easy
# 标签：数组、双指针、原地修改
# 题目描述：
# 给定一个长度为 n 的数组 nums 和一个整数 val，请你移除数组中所有等于 val 的元素。
# 要求保持剩余元素的原相对顺序。

# 输入格式：
# 第一行：n val
# 第二行：n 个整数 nums[0] nums[1] ... nums[n-1]

# 输出格式：
# 第一行：移除后的元素个数 k
# 第二行：移除后的前 k 个元素

# 样例输入 1：
# 4 3
# 3 2 2 3

# 样例输出 1：
# 2
# 2 2

# 样例输入 2：
# 8 2
# 0 1 2 2 3 0 4 2

# 样例输出 2：
# 5
# 0 1 3 0 4

# 约束：
# - 0 <= n <= 100
# - 0 <= nums[i] <= 50
# - 0 <= val <= 100
# """

import sys


def main():
    # 读取第一行：n 表示数组长度，val 表示要删除的目标值
    first = sys.stdin.readline().split()
    n = int(first[0])
    val = int(first[1])

    # 读取第二行：把输入的一整行数字转成整数列表
    # 例如输入：3 2 2 3
    # 会得到 nums = [3, 2, 2, 3]
    nums = list(map(int, sys.stdin.readline().split()))

    # fast：负责遍历原数组中的每一个元素
    # slow：表示“下一个要保留的元素”应该放到哪里
    fast = 0
    slow = 0

    while fast < n:
        # 如果 nums[fast] 不等于 val，说明这个元素需要保留
        if nums[fast] != val:
            # 把需要保留的元素覆盖到 nums[slow] 位置
            # 注意：这里不是让数组真正变短，而是把有效元素往前放
            nums[slow] = nums[fast]

            # slow 往后移动，表示下一个保留元素应该放到下一个位置
            slow += 1

        # fast 每一轮都要往后走，继续检查下一个原数组元素
        fast += 1

    # slow 最后表示保留下来的元素个数，也就是新数组长度 k
    print(slow)

    # nums 的真实长度没有变化
    # 但是 nums[:slow] 表示前 slow 个有效元素
    # 例如 nums = [2, 2, 2, 3], slow = 2
    # 那么 nums[:slow] 就是 [2, 2]
    #
    # join 不是 json
    # " ".join(...) 表示用空格把字符串连接起来
    # map(str, nums[:slow]) 是把整数列表转成字符串列表
    # 例如 [2, 2] -> ["2", "2"] -> "2 2"
    print(" ".join(map(str, nums[:slow])))

if __name__ == "__main__":
    main()
