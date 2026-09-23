"""
Day 11 - 题目 2:括号是否合法

题目描述：

给定一个只包含以下字符的字符串 s:

( ) [ ] { }

判断这个字符串中的括号是否合法。

合法字符串必须同时满足：

1. 每一个左括号都能被相同类型的右括号关闭；
2. 括号关闭的顺序必须正确；
3. 每一个右括号都必须存在对应的左括号。

输入格式：

输入一行字符串 s。

输出格式：

如果括号字符串合法，输出：

true

否则输出：

false

输出必须使用小写字母。

样例输入 1:

()

样例输出 1:

true


样例输入 2:

()[]{}

样例输出 2:

true


样例输入 3:

(]

样例输出 3:

false


样例输入 4:

([)]

样例输出 4:

false


样例输入 5:

{[]}

样例输出 5:

true


样例输入 6:

]

样例输出 6:

false


样例输入 7:

((

样例输出 7:

false


约束：

- 1 <= len(s) <= 100000
- s 只包含 ()[]{} 六种字符

要求：

- 使用 Python
- 自己处理 ACM 输入输出
- 不使用外部库
"""

import sys


def main():
    s=sys.stdin.readline().strip()
    waiting=[]
    for char in s:
        if char in ("(","[","{"):
            waiting.append(char)
        else:
            if not waiting:
                print("false")
                return
            else:
                x=waiting.pop()
            if x=="[" and char !="]":
                print("false")
                return
            elif x=="(" and char !=")":
                print("false")
                return
            elif x=="{" and char !="}":
                print("false")
                return
    if waiting:
        print("false")
    else:
        print("true")


if __name__ == "__main__":
    main()