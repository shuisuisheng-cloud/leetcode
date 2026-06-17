# ```python
# """
# Day 3：有序数组的平方

# 题目：
# 给定一个按非递减顺序排列的整数数组 nums，
# 计算每个元素的平方，并输出一个同样按非递减顺序排列的新数组。

# 输入格式：
# 第一行：整数 n，表示数组长度
# 第二行：n 个按非递减顺序排列的整数

# 输出格式：
# 输出平方后按非递减顺序排列的数组，
# 元素之间用一个空格分隔。

# 样例输入：
# 5
# -4 -1 0 3 10

# 样例输出：
# 0 1 9 16 100

# 要求：
# - 使用 Python
# - 自己处理 ACM 输入输出
# - 不使用 sorted()
# - 不使用 list.sort()

# 题型：
# 数组、双指针、排序

# 核心思路：
# 1. 原数组虽然是有序的，但存在负数。
# 2. 负数平方后可能变得很大，因此直接从左到右平方不能保证结果有序。
# 3. 平方后的最大值一定来自当前数组区间的左端或右端。
# 4. 使用 left 和 right 分别指向两端。
# 5. 每次比较 nums[left] 和 nums[right]，把较大的值放到 result[pos]。
# 6. result 从最后一个位置向前填写，因此最终结果是升序的。

# 注意：
# 这里先把 nums 中的每个数平方，所以双指针阶段直接比较 nums[left]
# 和 nums[right] 即可，不需要再计算绝对值或平方。
# """

import sys


def main():
    # 第一行只有一个整数 n。
    # sys.stdin.readline() 读到的是字符串，例如 "5\n"。
    # int() 可以直接把它转换成整数 5。
    n = int(sys.stdin.readline())

    # 读取第二行。
    # split()：按空格拆分字符串。
    # map(int, ...)：把拆分后的每个字符串转换成整数。
    # list(...)：把结果转换成整数列表。
    nums = list(map(int, sys.stdin.readline().split()))

    # 第一步：把原数组中的每个元素平方。
    i = 0

    while i < n:
        current = nums[i]
        nums[i] = current * current
        i += 1

    # 平方后的数组不一定有序。
    # 例如：
    # 原数组：[-4, -1, 0, 3, 10]
    # 平方后：[16, 1, 0, 9, 100]

    # left 指向当前待处理区间的左端。
    left = 0

    # right 指向当前待处理区间的右端。
    right = n - 1

    # pos 表示下一次应该把较大值放到 result 的哪个位置。
    # 因为每次找到的是当前最大值，所以从结果数组末尾开始填写。
    pos = n - 1

    # 创建长度为 n 的结果数组。
    # [0] * n 表示创建 n 个 0。
    result = [0] * n

    # 使用 left <= right。
    # 当 left == right 时，还有最后一个元素没有处理，不能漏掉。
    while left <= right:

        # 如果左端值大于或等于右端值，
        # 就把左端值放到当前结果位置。
        #
        # 使用 >= 可以同时处理两端相等的情况，
        # 不需要单独再写一个 elif 或 else 来一次放两个元素。
        if nums[left] >= nums[right]:
            result[pos] = nums[left]

            # 左端元素已经使用，left 向右移动。
            left += 1

        else:
            # 右端值更大，把右端值放到当前结果位置。
            result[pos] = nums[right]

            # 右端元素已经使用，right 向左移动。
            right -= 1

        # 每一轮只确定 result 中的一个位置。
        # 当前最大值放好以后，pos 向前移动。
        pos -= 1

    # result 是整数列表，join() 不能直接连接整数。
    #
    # map(str, result)：
    # 把 [0, 1, 9, 16, 100]
    # 转换成 ["0", "1", "9", "16", "100"]
    #
    # " ".join(...)：
    # 使用空格把字符串连接起来，
    # 得到 "0 1 9 16 100"
    print(" ".join(map(str, result)))


# __name__ 不是文件名。
#
# 当执行：
# python3 977_sorted_squares.py
#
# Python 会把当前文件中的 __name__ 设置为 "__main__"，
# 因此条件成立并调用 main()。
#
# 如果该文件被其他 Python 文件导入，
# main() 就不会自动执行。
if __name__ == "__main__":
    main()


# """
# 本题易错点：

# 1. n 的读取

# 错误：
# n = int(sys.stdin.readline().split())

# 原因：
# split() 返回的是列表，不能直接把整个列表传给 int()。

# 正确理解：
# 第一行只有一个整数，可以直接使用：
# n = int(sys.stdin.readline())


# 2. 数组下标边界

# 数组长度为 n 时，合法下标是：

# 0, 1, 2, ..., n - 1

# 所以遍历数组时应该使用：

# while i < n

# 不能写：

# while i <= n

# 否则 i == n 时访问 nums[i] 会越界。


# 3. 双指针循环条件

# 应该使用：

# while left <= right

# 原因：
# 当 left == right 时，还有最后一个元素没有放入结果数组。


# 4. right 的移动方向

# right 从数组右端向中间移动。

# 使用右端元素后应该：

# right -= 1

# 不能写：

# right += 1

# 否则 right 会继续向数组外移动并造成越界。


# 5. 每轮只放一个元素

# 双指针每轮只确定 result[pos] 这一个位置。

# 不能在相等时一次放入两个元素，否则容易出现：

# - pos 没有正确移动；
# - 同一个元素被重复使用；
# - left 和 right 没有正确更新；
# - 结果被后续数据覆盖。


# 6. 输出 result，不是 nums

# nums 只是平方后的中间结果，例如：

# [16, 1, 0, 9, 100]

# 真正排好序的结果保存在：

# result

# 因此最后应该输出 result。


# 时间复杂度：
# O(n)

# 原因：
# - 第一次循环平方所有元素：O(n)
# - 第二次双指针遍历所有元素：O(n)
# - 总时间复杂度为 O(n) + O(n) = O(n)


# 空间复杂度：
# O(n)

# 原因：
# 创建了长度为 n 的 result 数组。


# Python 常用模板：

# 读取一个整数：
# n = int(sys.stdin.readline())

# 读取一行整数数组：
# nums = list(map(int, sys.stdin.readline().split()))

# 创建长度为 n 的数组：
# result = [0] * n

# 输出空格分隔的整数：
# print(" ".join(map(str, result)))


# 以后使用 C++ 实现时可能用到：

# - vector<int> nums
# - vector<int> result(n)
# - 下标访问 nums[left]
# - cout 输出
# """
# ```
