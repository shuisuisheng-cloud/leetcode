import sys
def main():
     a=sys.stdin.readline()
     part=a.split()
     nums=int(part[0])
     target=int(part[1])
     numslist=list(map(int, sys.stdin.readline().split()))
     left=0
     right=nums-1
     while left<=right:
          middle=(left+right)//2
          if numslist[middle]==target:
               print(middle)
               return
          elif numslist[middle]<target:
               left=middle+1
          else:
               right=middle-1
     print(-1)
if __name__=="__main__":
     main()