# """
# Day 8：快乐数

# 题目：
# 对于一个正整数 n，重复执行以下操作：

# 1. 把 n 替换为它的每一位数字的平方和；
# 2. 继续对新得到的数字执行相同操作。

# 如果这个过程最终能够得到 1，
# 则称 n 为快乐数。

# 如果这个过程不断循环，并且永远无法得到 1，
# 则 n 不是快乐数。

# 输入格式：
# 输入一行，一个正整数 n。

# 输出格式：
# 如果 n 是快乐数，输出 true；
# 否则输出 false。

# 输出必须使用小写字母。

# 样例输入 1：
# 19

# 样例输出 1：
# true

# 样例输入 2：
# 2

# 样例输出 2：
# false

# 样例输入 3：
# 1

# 样例输出 3：
# true

# 样例输入 4：
# 7

# 样例输出 4：
# true

# 约束：
# - 1 <= n <= 2^31 - 1

# 要求：
# - 使用 Python
# - 自己处理 ACM 输入输出
# - 不提前写死任何结果
# - 可以使用 set 或 dict
# - 需要保证程序不会无限循环

# 难度：Easy
# 标签：哈希集合、循环检测、数学
# """

import sys

def get_next_number(number):
    total=0
    for serial_data in str(number):
        total=total+int(serial_data)*int(serial_data)
    return total
def main():
    n=int(sys.stdin.readline())
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        n=get_next_number(n)
    if n == 1:
        print("true")
    else:
        print("false")



if __name__ == "__main__":
    main()


# """
# Day 8 总结：快乐数

# 题型：
# 哈希集合、循环检测、数学

# 一、核心问题

# 对于正整数 n，不断计算它的各位数字平方和。

# 例如：

# n = 19

# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1

# 最终得到 1，因此 19 是快乐数。


# 二、为什么要拆出 get_next_number() 函数？

# get_next_number(number) 只负责完成一轮计算：

# 输入：
# 19

# 输出：
# 82

# 函数职责单一，主程序只需要负责：

# 1. 判断是否到达 1；
# 2. 判断是否出现循环；
# 3. 不断调用 get_next_number()。


# 三、一轮平方和的计算

# 把整数转换成字符串：

# str(number)

# 例如：

# 19 -> "19"

# 遍历字符串中的每个字符：

# for digit in str(number):

# 字符 digit 需要先转换为整数：

# int(digit)

# 然后平方并累加：

# total += int(digit) * int(digit)


# 四、为什么要使用 set？

# 非快乐数不会一直产生全新的数字，
# 而是最终进入一个重复循环。

# 例如某个过程中出现：

# 2 -> ... -> 4 -> ... -> 4

# 当数字 4 再次出现时，
# 说明之后的计算过程会重复之前的路径，
# 永远无法到达 1。

# 因此使用：

# seen = set()

# 保存已经出现过的数字。


# 五、循环条件

# while n != 1 and n not in seen:

# 含义：

# 只要当前数字：

# 1. 还没有变成 1；
# 2. 以前没有出现过；

# 就继续计算。

# 循环中：

# seen.add(n)
# n = get_next_number(n)


# 六、循环结束的两种情况

# 情况一：

# n == 1

# 说明最终到达 1，是快乐数：

# print("true")


# 情况二：

# n in seen

# 说明当前数字曾经出现过，
# 已经进入循环，不是快乐数：

# print("false")


# 七、为什么不能只写 while n != 1？

# 如果 n 不是快乐数，
# 计算过程可能永远循环。

# 只判断：

# while n != 1:

# 程序可能永远无法结束。

# 所以还必须判断：

# n not in seen


# 八、为什么不能写 seen = seen.add(n)？

# set.add() 会直接修改集合，
# 但它的返回值是 None。

# 错误：

# seen = seen.add(n)

# 执行后 seen 会变成 None。

# 正确：

# seen.add(n)


# 九、输入读取

# 题目只输入一个整数：

# n = int(sys.stdin.readline())

# 不需要 split()。

# 错误：

# n = int(sys.stdin.readline().split())

# 因为 split() 返回列表，
# 不能直接把整个列表传给 int()。


# 十、本题易错点

# 1. readline() 读取后忘记转换为 int；
# 2. 每轮平方和的 total 必须重新从 0 开始；
# 3. 字符数字需要使用 int() 转换；
# 4. set.add() 不能赋值回原集合；
# 5. 只判断 n != 1 会造成死循环；
# 6. 不要针对特定数字写死判断，例如 n == 4；
# 7. 应记录所有出现过的中间结果；
# 8. 输出必须是小写 true 或 false。


# 十一、时间复杂度

# 设每轮数字有 d 位，
# 计算一次各位平方和需要：

# O(d)

# 循环出现的中间状态数量设为 k，
# 总时间复杂度可以写为：

# O(k × d)

# 对于本题整数范围，中间结果会很快缩小，
# 实际状态数量有限。

# 在常见面试回答中，也可以说明：
# 算法对所有出现过的状态只处理一次。


# 十二、空间复杂度

# seen 集合保存已经出现过的中间结果。

# 空间复杂度：

# O(k)

# 其中 k 是计算过程中出现的不同状态数量。


# 十三、Python 常用模板

# 计算各位数字平方和：

# def get_next_number(number):
#     total = 0

#     for digit in str(number):
#         total += int(digit) * int(digit)

#     return total


# 使用集合检测循环：

# seen = set()

# while n != 1 and n not in seen:
#     seen.add(n)
#     n = get_next_number(n)


# 十四、以后使用 C++ 实现时

# 需要使用：

# unordered_set<int>

# 用于记录出现过的数字：

# unordered_set<int> seen;

# 判断是否出现过：

# seen.count(n)

# 加入集合：

# seen.insert(n)

# 拆分整数各位时，可以不用转换成字符串：

# digit = number % 10;
# number /= 10;

# 平方累加：

# total += digit * digit;


# 十五、面试表达

# 可以这样回答：

# 我先写一个函数计算整数各位数字的平方和，
# 然后不断更新当前数字。

# 如果最终得到 1，说明它是快乐数。

# 如果某个中间数字之前已经出现过，
# 说明之后会重复相同的计算路径，
# 已经进入循环，因此不是快乐数。

# 我使用哈希集合记录所有出现过的中间结果，
# 集合查询和插入的平均复杂度都是 O(1)。

# 空间复杂度取决于出现过的不同中间状态数量。
# """