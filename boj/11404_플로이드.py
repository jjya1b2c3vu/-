from sys import stdin
from pprint import pprint
stdin = open("input.txt","r")
input = stdin.readline

n = int(input())
m = int(input())
INF = int(10e8)
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,v= map(int,input().split())
    if a==b:
        graph[a][b]=0
    else:
        graph[a][b]=min(graph[a][b],v)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a!=b:
                graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            else:
                graph[a][b]=0

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print(0,end=" ")
        else:
            print(graph[a][b],end=" ")
    print()