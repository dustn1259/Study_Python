import sys
sys.stdin=open("input4.txt", "r")
N=int(input())
a=list(map(int, input().split()))
avg=round(sum(a)/n)
min=21470000000
for idx, x in enumerate(a):
     tmp =abs(x-avg)
     if tmp<min:
         min=tmp
         grade=x
         res=idx+1
     elif diff==min:
         if x>grade: #i>=grade라면 제일큰게 출력
             grade=x
             res=idx+1

print(avg,res)
