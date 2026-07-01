# """
# Day 6：有效的字母异位词

# 题目：
# 给定两个只包含小写英文字母的字符串 s 和 t，
# 判断 t 是否是 s 的字母异位词。

# 字母异位词是指：
# 两个字符串中每种字母出现的次数完全相同，
# 但字母的排列顺序可以不同。

# 输入格式：
# 第一行输入字符串 s。
# 第二行输入字符串 t。

# 输出格式：
# 如果 t 是 s 的字母异位词，输出 true；
# 否则输出 false。

# 输出必须使用小写字母。

# 样例输入 1：
# anagram
# nagaram

# 样例输出 1：
# true

# 样例输入 2：
# rat
# car

# 样例输出 2：
# false

# 样例输入 3：
# aacc
# ccac

# 样例输出 3：
# false

# 样例输入 4：
# listen
# silent

# 样例输出 4：
# true

# 约束：
# - 1 <= len(s), len(t) <= 50000
# - s 和 t 只包含小写英文字母

# 要求：
# - 使用 Python
# - 自己处理 ACM 输入输出
# - 不使用 sorted()
# - 不使用 collections.Counter
# - 可以使用 Python 字典
# - 核心算法尽量达到 O(n)

# 难度：Easy
# 标签：字符串、哈希表、字符计数
# """

import sys


def main():
    s=sys.stdin.readline().strip()
    t=sys.stdin.readline().strip()
    d={}
    if len(s) != len(t):
        print("false")
        return
    for serial_data in s:
        if serial_data in d:
            d[serial_data]=d[serial_data]+1
        else:
            d[serial_data]=1
    for data in t:
        if data in d:
            d[data]=d[data]-1
            if d[data]<0:
                print("false")
                return
        else:
            print("false")
            return
    print("true")
        
        



if __name__ == "__main__":
    main()