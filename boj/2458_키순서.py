from sys import stdin
stdin = open("input.txt","r")
input = stdin.readline

n,m = map(int,input().split())
INF=int(10e8)
graph = [[INF]*(n) for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    a,b=a-1,b-1
    graph[a][b]=1

for _ in graph:
    print(_)
print()
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for _ in graph:
    print(_)
print()
for g in graph:
    print(g.count(INF))