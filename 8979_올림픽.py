import sys
sys.stdin = open("input.txt", "r")
N,country = map(int,input().split())
grad=dict()
cnt=1
for _ in range(N):
    c,g,s,b=map(int,input().split())
    grad[c]=[g,s,b]
for x in grad.keys(): 
    if (grad[country]<grad[x]):
            cnt+=1
print(cnt)