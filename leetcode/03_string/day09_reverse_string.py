# ```python
# """
# Day 9：反转字符串

# 题目：
# 给定一个长度为 n 的字符串 s，
# 请将字符串中的字符顺序反转，并输出反转后的结果。

# 输入格式：
# 第一行输入一个整数 n。
# 第二行输入一个长度为 n 的字符串 s。

# 字符串只包含大小写英文字母和数字，不包含空格。

# 输出格式：
# 输出反转后的字符串。

# 样例输入 1：
# 5
# hello

# 样例输出 1：
# olleh

# 样例输入 2：
# 6
# Python

# 样例输出 2：
# nohtyP

# 样例输入 3：
# 1
# a

# 样例输出 3：
# a

# 样例输入 4：
# 6
# 123abc

# 样例输出 4：
# cba321

# 约束：
# - 1 <= n <= 100000
# - len(s) == n
# - s 只包含大小写英文字母和数字

# 要求：
# - 使用 Python
# - 自己处理 ACM 输入输出
# - 不使用 s[::-1]
# - 不使用 reversed()
# - 不使用 list.reverse()
# - 自己完成字符位置交换
# - 核心算法达到 O(n)

# 难度：Easy
# 标签：字符串、数组、双指针、原地修改
# """

import sys


def main():
    n=int(sys.stdin.readline())
    s=list(sys.stdin.readline().strip())
    left = 0
    right = n - 1

    while left < right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    print("".join(s))
if __name__ == "__main__":
    main()
    

#     """
# Day 9 总结：反转字符串

# 题型：
# 字符串、数组、双指针、原地修改


# 一、核心思路

# 字符串本身不能直接修改，因此先把字符串转换成字符列表：

# s = list(sys.stdin.readline().strip())

# 例如：

# "hello"

# 转换为：

# ["h", "e", "l", "l", "o"]

# 然后使用两个指针：

# left：从字符串左端开始
# right：从字符串右端开始

# 每一轮交换：

# s[left], s[right] = s[right], s[left]

# 交换后两个指针同时向中间移动：

# left += 1
# right -= 1


# 二、为什么使用 while left < right？

# 只要 left 还在 right 左边，
# 就说明两端还有字符需要交换。

# 当：

# left == right

# 说明字符串长度为奇数，
# 中间字符不需要与自己交换。

# 当：

# left > right

# 说明所有字符都已经完成交换。

# 因此循环条件是：

# while left < right:


# 三、Python 中如何交换两个元素？

# Python 支持同时赋值：

# s[left], s[right] = s[right], s[left]

# 例如：

# s = ["h", "e", "l", "l", "o"]

# left = 0
# right = 4

# 交换后：

# s = ["o", "e", "l", "l", "h"]

# 不需要额外定义临时变量。


# 四、为什么要把字符串转换成列表？

# Python 字符串是不可变对象。

# 不能直接写：

# s[0] = "o"

# 这会报错。

# 列表可以修改指定位置：

# chars[0] = "o"

# 所以先使用：

# s = list(text)

# 完成交换后，再把列表重新连接成字符串。


# 五、如何把字符列表重新转换成字符串？

# 交换完成后，s 仍然是列表：

# ["o", "l", "l", "e", "h"]

# 使用：

# "".join(s)

# 得到：

# "olleh"

# 这里前面的：

# ""

# 表示使用空字符串连接各个字符，
# 字符之间不会出现空格。

# 最后输出：

# print("".join(s))


# 六、为什么不能使用 map(str, ...)？

# 下面的写法虽然可以运行：

# s = list(map(str, sys.stdin.readline().strip()))

# 但是字符串中的每个元素本来就已经是字符串，
# 再次调用 str() 没有必要。

# 更清晰的写法是：

# s = list(sys.stdin.readline().strip())


# 七、ACM 输入模板

# 读取字符串长度：

# n = int(sys.stdin.readline())

# 读取字符串并转为字符列表：

# s = list(sys.stdin.readline().strip())

# 输出反转后的字符串：

# print("".join(s))


# 八、本题易错点

# 1. 第一行只有一个整数，不需要 split()

# 正确：

# n = int(sys.stdin.readline())

# 错误：

# n = int(sys.stdin.readline().split())


# 2. 使用 split() 读取字符串会得到单词列表

# 例如：

# list(map(str, "hello".split()))

# 得到的是：

# ["hello"]

# 而不是：

# ["h", "e", "l", "l", "o"]

# 正确方式：

# list("hello")


# 3. 字符串不能直接原地修改

# Python 字符串不可变，
# 需要先转换成列表。


# 4. right 的初值是 n - 1

# 长度为 n 的字符串，
# 合法下标范围是：

# 0 到 n - 1

# 所以：

# right = n - 1


# 5. 循环条件使用 left < right

# 不能使用：

# left <= right

# 虽然中间元素和自己交换通常不会报错，
# 但这是一次没有意义的操作。


# 6. 每轮交换后两个指针都必须移动

# left += 1
# right -= 1

# 如果忘记移动，程序会陷入死循环。


# 7. 输出时要使用 join()

# 直接：

# print(s)

# 会输出：

# ['o', 'l', 'l', 'e', 'h']

# 题目要求：

# olleh

# 所以需要：

# print("".join(s))


# 九、时间复杂度

# 双指针从字符串两端向中间移动。

# 每个字符最多参与一次交换，
# 循环大约执行 n / 2 次。

# 时间复杂度：

# O(n)


# 十、空间复杂度

# 在 Python 中，原始字符串需要转换成字符列表：

# s = list(...)

# 字符列表长度为 n，因此空间复杂度为：

# O(n)

# 如果题目本身直接提供可修改的字符数组，
# 那么双指针交换本身只使用 left 和 right，
# 额外空间复杂度可以认为是：

# O(1)


# 十一、为什么称为原地修改？

# 算法没有再创建一个新的反转结果数组，
# 而是直接交换字符列表 s 内部的位置。

# 因此相对于字符列表而言，
# 这是原地修改。

# 但在 Python ACM 输入中，
# 字符串转换为列表本身仍然需要 O(n) 空间。


# 十二、双指针通用模板

# left = 0
# right = len(data) - 1

# while left < right:
#     data[left], data[right] = data[right], data[left]
#     left += 1
#     right -= 1


# 十三、以后使用 C++ 实现时

# 字符串容器：

# string

# C++ 的 string 可以修改指定位置，因此不需要先转换成字符数组。

# 交换函数：

# swap(s[left], s[right]);

# 完整核心结构：

# int left = 0;
# int right = s.size() - 1;

# while (left < right) {
#     swap(s[left], s[right]);
#     left++;
#     right--;
# }

# 涉及的 STL / 标准库：

# string
# swap


# 十四、面试表达

# 如果面试官问本题思路，可以回答：

# 我使用左右双指针分别指向字符串首尾。

# 当 left 小于 right 时，
# 交换两个指针所指向的字符，
# 然后 left 向右移动，right 向左移动。

# 当两个指针相遇或交错时，
# 说明全部字符已经完成反转。

# 每个字符只处理一次，
# 所以时间复杂度是 O(n)。

# 双指针本身只使用常数个变量，
# 额外空间复杂度是 O(1)。

# 不过在 Python 中字符串不可变，
# 如果输入是字符串，需要先转换成字符列表，
# 因此整体空间复杂度为 O(n)。
# """
