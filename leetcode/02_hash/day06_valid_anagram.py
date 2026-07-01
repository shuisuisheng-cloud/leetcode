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

# ```python
# """
# Day 6 总结：有效的字母异位词

# 题型：
# 字符串、哈希表、字符计数

# 核心目标：
# 判断两个字符串中每一种字符出现的次数是否完全相同。

# 例如：

# s = "anagram"
# t = "nagaram"

# 虽然两个字符串的字母顺序不同，
# 但每个字符出现的次数相同，因此输出 true。


# 一、核心思路

# 使用字典 d 记录字符出现次数：

# 字符 -> 出现次数

# 第一步：
# 遍历字符串 s，把每个字符的次数加 1。

# 第二步：
# 遍历字符串 t，把对应字符的次数减 1。

# 如果遍历 t 时出现以下任意情况：

# 1. 当前字符不在字典中；
# 2. 当前字符的计数减到小于 0；

# 说明 t 不是 s 的字母异位词，输出 false。

# 如果所有字符都顺利处理完成，则输出 true。


# 二、为什么要先判断字符串长度？

# 如果：

# len(s) != len(t)

# 两个字符串包含的字符总数不同，
# 一定不可能是字母异位词。

# 例如：

# s = "ab"
# t = "a"

# 即使 t 中的字符都在 s 中，
# 字符总数仍然不同，因此直接输出 false。


# 三、为什么使用 strip()？

# sys.stdin.readline() 会保留输入行末尾的换行符：

# 例如输入：

# anagram

# 实际读取到的可能是：

# "anagram\\n"

# 使用：

# s = sys.stdin.readline().strip()

# 可以去掉行尾的换行符，
# 得到真正的字符串：

# "anagram"


# 四、建立字符计数字典

# 遍历字符串 s：

# for char in s:
#     if char in d:
#         d[char] += 1
#     else:
#         d[char] = 1

# 例如：

# s = "aacc"

# 最终字典为：

# {
#     "a": 2,
#     "c": 2
# }


# 五、使用字符串 t 抵消计数

# 遍历字符串 t：

# for char in t:
#     if char in d:
#         d[char] -= 1

#         if d[char] < 0:
#             print("false")
#             return
#     else:
#         print("false")
#         return


# 为什么需要检查字符是否存在？

# 例如：

# s = "rat"
# t = "car"

# 统计 s 后：

# {
#     "r": 1,
#     "a": 1,
#     "t": 1
# }

# 遍历 t 时遇到字符 "c"，
# 但字典中没有 "c"，
# 所以可以立即判断结果为 false。


# 为什么需要检查计数是否小于 0？

# 例如：

# s = "aacc"
# t = "ccac"

# 统计 s 后：

# {
#     "a": 2,
#     "c": 2
# }

# 遍历 t 时，字符 "c" 出现了 3 次。

# 第三次处理 "c" 后：

# d["c"] = -1

# 说明 t 中字符 "c" 的数量超过了 s，
# 所以结果为 false。


# 六、为什么所有检查通过后可以直接输出 true？

# 前面已经保证：

# len(s) == len(t)

# 随后又保证：

# 1. t 中每个字符都存在于 s 的计数字典中；
# 2. 没有任何字符的数量超过 s。

# 两个字符串总长度相同，
# 并且 t 没有缺少或增加任何字符，
# 所以它们一定是字母异位词。


# 七、ACM 输入输出模板

# 读取一行字符串并删除换行符：

# s = sys.stdin.readline().strip()

# 输出小写 true：

# print("true")

# 输出小写 false 并结束程序：

# print("false")
# return


# 八、本题易错点

# 1. 忘记使用 strip()

# 如果不去掉换行符，
# 字符串末尾可能多出 "\\n"，
# 干扰字符统计。


# 2. 直接拼接两个字符串再判断位置

# 把 s 和 t 拼接后，
# 再根据下标判断当前字符属于哪个字符串，
# 边界容易写错。

# 分成两个循环更加清晰：

# 第一个循环统计 s；
# 第二个循环检查 t。


# 3. 判断对象写错

# 第二个循环中当前字符变量是 data，
# 应判断：

# if data in d:

# 不能写：

# if data in t:

# 因为 data 本来就是从 t 中遍历出来的，
# 这个条件永远成立。


# 4. 使用了上一个循环的变量

# 第一个循环可能使用：

# serial_data

# 第二个循环使用：

# data

# 第二个循环中应操作：

# d[data]

# 不能继续使用：

# d[serial_data]


# 5. return False 不会自动输出

# 在 ACM 模式中：

# return False

# 只会结束函数，不会向终端输出 false。

# 应该写：

# print("false")
# return


# 6. 输出格式必须是小写

# 题目要求：

# true
# false

# 不能直接输出 Python 布尔值：

# True
# False


# 九、时间复杂度

# 假设：

# len(s) = n
# len(t) = n

# 第一次遍历 s：

# O(n)

# 第二次遍历 t：

# O(n)

# 总时间复杂度：

# O(n) + O(n) = O(n)


# 十、空间复杂度

# 使用字典保存不同字符的计数。

# 一般情况下：

# 空间复杂度为 O(k)

# 其中 k 是不同字符的数量。

# 本题只包含 26 个小写英文字母，
# 字典最多保存 26 个键。

# 因此也可以认为：

# 额外空间复杂度为 O(1)


# 十一、Python 常用模板

# 字符计数：

# count = {}

# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1


# 更简洁的 Python 写法：

# count[char] = count.get(char, 0) + 1

# 含义：

# 如果 char 已经存在，获取原计数；
# 如果不存在，默认从 0 开始。


# 十二、以后使用 C++ 实现时

# 字符串容器：

# string

# 哈希表：

# unordered_map<char, int>

# 统计字符：

# unordered_map<char, int> count;

# for (char ch : s) {
#     count[ch]++;
# }

# 检查字符：

# if (count.find(ch) == count.end()) {
#     // 字符不存在
# }

# 减少计数：

# count[ch]--;

# 由于本题只有 26 个小写字母，
# 也可以使用固定长度数组：

# vector<int> count(26, 0);

# 通过：

# ch - 'a'

# 把字符转换为 0 到 25 的下标。

# 例如：

# 'a' - 'a' = 0
# 'b' - 'a' = 1
# 'z' - 'a' = 25


# 十三、面试表达

# 如果面试官问本题思路，可以回答：

# 我使用哈希表统计第一个字符串中每个字符的出现次数，
# 然后遍历第二个字符串，将对应字符计数减一。

# 如果字符不存在，或者某个字符计数变成负数，
# 说明第二个字符串包含额外字符，直接返回 false。

# 由于提前判断了两个字符串长度相同，
# 如果第二次遍历全部完成，则说明每个字符的数量完全一致。

# 算法需要遍历两个字符串一次，
# 时间复杂度是 O(n)。

# 哈希表最多保存不同字符的数量，
# 一般空间复杂度是 O(k)；
# 本题字符集固定为 26 个小写字母，也可以视为 O(1)。
# """
# ```
