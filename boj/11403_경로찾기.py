from sys import stdin
stdin = open("boj/input.txt","r")
input = stdin.readline

n = int(input())
INF = int(1e9)
graph = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]= 1 if graph[a][b] or (graph[a][k] and graph[k][b]) else 0

for a in range(n):
    for b in range(n):
        print(graph[a][b],end=" ")
    print()