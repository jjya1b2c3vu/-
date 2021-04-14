from sys import stdin
from pprint import pprint
stdin = open("boj/input.txt","r")
input = stdin.readline
N,M,K,X = map(int,input().split())

graph = [ [] for _ in range(N+1) ]

for _ in range(1,M+1):
    i,j = map(int,input().split())
    graph[i].append(j) 

visited = [-1]*(N+1)

from collections import deque
def bfs(v):
    qu = deque()
    qu.append(v)
    visited[v]=0
    cnt=0
    while(qu):
        now_node = qu.popleft()
        for next_node in graph[now_node]:
            if visited[next_node]==-1:
                qu.append(next_node)
                visited[next_node]=visited[now_node]+1
                
bfs(X)
ans=[]
for i,v in enumerate(visited):
    if v==K:
        ans.append(i)
if len(ans)==0:
    print(-1)
else:
    for a in sorted(ans):
        print(a)