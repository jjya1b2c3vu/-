from sys import stdin
stdin = open("input.txt","r")
input = stdin.readline

n,m = map(int,input().split())
A = sorted(list(map(int,input().split())))
ans = 0
s,e = 0,len(A)-1
while(s<e):
    Sum = sum(A[s:e+1])
    print(Sum,s,e)
    if Sum == m:
        ans+=1
        s+=1
        e=len(A)-1
    elif Sum>m:
        e-=1
print(ans)
        