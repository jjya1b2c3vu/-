from sys import stdin
stdin = open("input.txt","r")
input = stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]



for a in range(n):
    for b in range(n):
        if graph[a][b]=='Y':
            graph[a][b]=1
        else:
            graph[a][b]=0

for g in graph:
    print(g)

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
for g in graph:
    print(g)