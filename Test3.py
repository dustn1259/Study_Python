import sys
sys.stdin=open("input3.txt","rt")
n, k=map(int, input().split())
a=list(map(int, input().split()))
res=set()
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])
res=list(res)#res list화하기
res.sort(reverse=True) #내림차순
print(res[k-1])
