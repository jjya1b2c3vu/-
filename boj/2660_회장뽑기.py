from sys import stdin
stdin = open("input.txt","r")
input = stdin.readline

n = int(input())
INF=int(100)
graph= [[INF]*n for _ in range(n)]
flag=True
while(flag):
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        flga=False
        break
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for a in range(n):
    graph[a][a]=0

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

ans=[]
for i in range(n):
    ans.append(max(graph[i]))

#정답 출력
president = min(ans)
print(president,ans.count(president))
for j in range(n):
    if ans[j]== president:
        print(j+1,end=" ")
print()