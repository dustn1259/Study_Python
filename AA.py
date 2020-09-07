import sys
sys.stdin=open("input.txt", "rt") #read file
n, k=map(int, input().split())
j=0
for i in range(1,n+1):
    if n%i==0:
        j=j+1
    if k==j:
        print(j)
        break
else:
    print("-1")
