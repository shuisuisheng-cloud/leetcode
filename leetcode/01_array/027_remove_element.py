import sys
def main():
    input=sys.stdin.readline().split()
    n=int(input[0])
    num=int(input[1])
    nums=list(map(int,sys.stdin.readline().split()))
    for a in nums:
        fast=0
        slow=0
        if a==num:
            nums=list.remove[fast]
        else:
            fast+=1
