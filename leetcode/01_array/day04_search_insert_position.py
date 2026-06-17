
# """
# Day 4：搜索插入位置

# 题目：
# 给定一个长度为 n 的严格升序整数数组 nums，以及一个目标值 target。

# 如果 target 已经存在于数组中，输出它的下标；
# 如果 target 不存在，输出它按照升序插入数组后应该处于的下标。

# 数组下标从 0 开始。

# 输入格式：
# 第一行输入两个整数：
# n target

# 第二行输入 n 个严格升序排列的整数：
# nums[0] nums[1] ... nums[n - 1]

# 输出格式：
# 输出一个整数，表示：
# 1. target 已经存在时的下标；
# 2. target 不存在时的插入位置。

# 样例输入 1：
# 4 5
# 1 3 5 6

# 样例输出 1：
# 2

# 样例输入 2：
# 4 2
# 1 3 5 6

# 样例输出 2：
# 1

# 样例输入 3：
# 4 7
# 1 3 5 6

# 样例输出 3：
# 4

# 样例输入 4：
# 4 0
# 1 3 5 6

# 样例输出 4：
# 0

# 约束：
# - 1 <= n <= 10000
# - -10000 <= nums[i] <= 10000
# - -10000 <= target <= 10000
# - nums 严格升序排列

# 要求：
# - 使用 Python
# - 自己处理 ACM 输入输出
# - 不使用 list.index()
# - 不使用 bisect 模块
# - 不真正执行插入操作
# - 核心查找算法时间复杂度达到 O(log n)

# 难度：Easy
# 标签：数组、二分查找、边界处理
# """

import sys


def main():
    # 读取第一行。
    #
    # 例如输入：
    # 4 5
    #
    # sys.stdin.readline() 读取到字符串：
    # "4 5\n"
    #
    # split() 后得到：
    # ["4", "5"]
    #
    # map(int, ...) 把每个字符串转换成整数。
    # list(...) 最终得到：
    # [4, 5]
    first_line = list(map(int, sys.stdin.readline().split()))

    # n 表示数组长度。
    n = first_line[0]

    # target 表示要查找或插入的目标值。
    target = first_line[1]

    # 读取第二行整数数组。
    #
    # 例如输入：
    # 1 3 5 6
    #
    # 最终得到：
    # nums = [1, 3, 5, 6]
    nums = list(map(int, sys.stdin.readline().split()))

    # 二分查找的左边界。
    left = 0

    # 二分查找的右边界。
    #
    # 数组长度为 n 时，最后一个合法下标是 n - 1。
    right = n - 1

    # 使用闭区间 [left, right]。
    #
    # 当 left == right 时，区间内仍然有一个元素需要检查，
    # 因此循环条件必须是 left <= right。
    while left <= right:
        # middle 必须在每一轮循环开始时重新计算。
        #
        # 因为 left 或 right 每轮都会发生变化，
        # 搜索区间改变后，中间下标也需要重新计算。
        #
        # 使用 // 整除，保证 middle 是整数下标。
        middle = (left + right) // 2

        # 如果中间值小于 target，
        # 说明 target 不可能位于 middle 或 middle 左侧。
        #
        # middle 这个位置已经确定不是答案，
        # 所以直接排除到 middle：
        # 新的左边界为 middle + 1。
        if nums[middle] < target:
            left = middle + 1

        # 如果中间值等于 target，
        # 说明已经找到目标，直接输出下标并结束 main()。
        elif nums[middle] == target:
            print(middle)
            return

        # 如果中间值大于 target，
        # 说明 target 应该位于 middle 左侧，
        # 或者插入到更靠左的位置。
        #
        # middle 这个位置已经确定不是答案，
        # 所以新的右边界为 middle - 1。
        else:
            right = middle - 1

    # 如果 while 循环结束，说明数组中不存在 target。
    #
    # 此时一定有：
    # right < left
    #
    # left 左边的元素都小于 target，
    # left 位置以及其右边的元素都大于 target。
    #
    # 因此 left 就是 target 应该插入的位置。
    print(left)


# __name__ 不是文件名。
#
# 当直接运行：
# python3 day04_search_insert_position.py
#
# 当前文件中的 __name__ 会被设置成 "__main__"，
# 因此下面的条件成立并调用 main()。
#
# 如果该文件被其他 Python 文件导入，
# main() 不会自动执行。
if __name__ == "__main__":
    main()


# """
# 本题核心思想：

# 二分查找每一轮都通过 middle 判断目标在哪一半，
# 然后直接排除一半搜索区间。

# 搜索区间变化过程类似：

# n
# n / 2
# n / 4
# n / 8
# ...

# 因此核心查找算法的时间复杂度是 O(log n)。


# 为什么循环结束后的 left 是插入位置？

# 例如：

# nums = [1, 3, 5, 6]
# target = 2

# 二分结束时：

# right = 0
# left = 1

# 此时：
# - 下标 0 及其左边的元素小于 target；
# - 下标 1 及其右边的元素大于 target。

# 所以 target 应该插入下标 1。


# 再例如：

# nums = [1, 3, 5, 6]
# target = 7

# 循环结束时：

# left = 4
# right = 3

# 数组最后一个下标是 3，
# left = 4 表示 target 应该插入数组末尾。


# 再例如：

# nums = [1, 3, 5, 6]
# target = 0

# 循环结束时：

# left = 0
# right = -1

# left = 0 表示 target 应该插入数组开头。


# 本题易错点：

# 1. middle 必须放在 while 循环里面

# 错误思路：
# 只在循环开始前计算一次 middle。

# 原因：
# left 和 right 每轮都会改变，
# middle 也必须根据新的区间重新计算。


# 2. 中间下标必须使用 //

# 错误：
# middle = (left + right) / 2

# 原因：
# / 得到浮点数，例如 1.5，
# 浮点数不能作为列表下标。

# 正确：
# middle = (left + right) // 2


# 3. 左边界必须移动到 middle + 1

# 当：

# nums[middle] < target

# middle 已经确定不是答案，
# 所以应该：

# left = middle + 1

# 不能写：

# left = middle

# 否则在某些情况下 left 和 middle 相同，
# 搜索区间不会缩小，可能导致死循环。


# 4. 右边界必须移动到 middle - 1

# 当：

# nums[middle] > target

# middle 已经确定不是答案，
# 所以应该：

# right = middle - 1

# 不能写：

# right = middle

# 否则也可能导致搜索区间无法继续缩小。


# 5. 找到目标后要 return

# 只写：

# print(middle)

# 程序仍可能继续执行后面的代码。

# 因此应该：

# print(middle)
# return


# 6. 循环条件使用 left <= right

# 本题使用的是闭区间：

# [left, right]

# 当 left == right 时，
# 区间内仍然有一个元素需要判断。

# 所以应该使用：

# while left <= right


# 7. 找不到时输出 left

# 不需要真正调用 insert() 把 target 插入数组。

# 二分循环结束后的 left，
# 自然就是正确的插入位置。


# 复杂度分析：

# 核心查找时间复杂度：
# O(log n)

# 原因：
# 每一轮都排除当前搜索区间的一半。


# 额外空间复杂度：
# O(1)

# 原因：
# 查找过程中只使用了：

# left
# right
# middle

# 几个整数变量，没有创建与 n 成比例的辅助数组。


# 关于 ACM 输入：

# 读取 nums 本身需要读取 n 个元素，
# 因此如果把输入过程也算进整个程序，
# 总运行时间至少需要 O(n)。

# 但是面试中分析本题时，
# 通常分析核心二分查找算法：

# 时间复杂度：O(log n)
# 空间复杂度：O(1)


# Python 常用模板：

# 读取一行整数：
# values = list(map(int, sys.stdin.readline().split()))

# 读取 n 和 target：
# first_line = list(map(int, sys.stdin.readline().split()))
# n = first_line[0]
# target = first_line[1]

# 读取整数数组：
# nums = list(map(int, sys.stdin.readline().split()))

# 闭区间二分查找：
# left = 0
# right = n - 1

# while left <= right:
#     middle = (left + right) // 2

#     if nums[middle] < target:
#         left = middle + 1
#     elif nums[middle] == target:
#         ...
#     else:
#         right = middle - 1


# 以后使用 C++ 实现时可能用到：

# - vector<int> nums
# - nums[middle] 下标访问
# - int left
# - int right
# - int middle
# - cin 读取输入
# - cout 输出结果

# 这道题不需要额外使用复杂 STL 容器。
# 核心容器是 vector。
# """
# ```
