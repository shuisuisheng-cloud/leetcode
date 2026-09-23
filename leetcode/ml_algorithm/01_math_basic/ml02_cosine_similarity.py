"""
Day 11 - 题目 3:向量相似度计算

题目描述：

给定两个长度均为 n 的数值向量 A 和 B。

请计算这两个向量的相似度，计算公式为：

               A · B
similarity = -----------
              |A| |B|

其中：

A · B 表示两个向量对应位置元素乘积之和。

|A| 表示向量 A 的长度：
sqrt(a1^2 + a2^2 + ... + an^2)

|B| 同理。

如果 A 或 B 中任意一个向量的长度为 0,
规定输出：

0.000000

输入格式：

第一行输入整数 n。

第二行输入 n 个数，表示向量 A。

第三行输入 n 个数，表示向量 B。

输入数据可能为整数，也可能为小数。

输出格式：

输出一个浮点数，保留六位小数。


样例输入 1:

3
1 0 0
1 0 0

样例输出 1:

1.000000


样例输入 2:

2
1 0
0 1

样例输出 2:

0.000000


样例输入 3:

2
1 1
1 0

样例输出 3:

0.707107


样例输入 4:

3
0 0 0
1 2 3

样例输出 4:

0.000000


约束：

- 1 <= n <= 100000
- -10^6 <= A[i], B[i] <= 10^6

要求：

- 使用 Python
- 自己处理 ACM 输入输出
- 不使用 NumPy
- 可以使用 math 模块
- 自己完成计算
- 输出保留六位小数
"""

import sys
import math


def main():
    n=int(sys.stdin.readline().strip())
    nums1=list(map(float,sys.stdin.readline().split()))
    nums2=list(map(float,sys.stdin.readline().split()))
    i=0
    dot=0
    norm_a=0
    norm_b=0
    while i<n:
        dot=dot+nums1[i]*nums2[i]
        norm_a=norm_a+nums1[i]*nums1[i]
        norm_b=norm_b+nums2[i]*nums2[i]
        i+=1
    if norm_b==0 or norm_a==0:
        print(f"{0:.6f}")
        return
    sim=dot/math.sqrt(norm_a*norm_b)
    print(f"{sim:.6f}")

if __name__ == "__main__":
    main()