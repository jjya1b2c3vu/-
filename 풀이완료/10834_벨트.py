import sys
sys.stdin = open("input.txt", "r")
M=int(input())
vector=0
cycle=1
cnt=0
for _ in range(M):
    a,b,n=map(int,input().split())
    cycle = cycle//a*b
    if n==1:
        cnt+=1
        vector=1
    if cnt==2:
        cnt=0
        vector=0
print("{} {}".format(vector,cycle))