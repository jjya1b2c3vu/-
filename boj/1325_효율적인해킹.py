from sys import stdin
from collections import defaultdict
stdin = open("input.txt","r")
input = stdin.readline

n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    b,a = map(int,input().split())
    graph[a].append(b)

# def dfs(s):
#     visited[s] = 1
#     global cnt
#     for nx in graph[s]:
#         if visited[nx]==0:
#             visited[nx]= 1
#             cnt+=1
#             return dfs(nx)
#         else:
#             return
def dfs(s):
    global cnt
    stack = []
    visited = [0]*(n+1)
    visited[s] = 1
    stack.append(s)
    while(stack):
        now = stack.pop()
        for nx in graph[now]:
            if visited[nx]==0:
                cnt+=1
                visited[nx]=1
                stack.append(nx)
ans=[]
depth = []

for i in range(1,n+1):
    cnt = 0
    dfs(i)
    ans.append((i,cnt))
    depth.append(cnt)
Max = max(depth)

for i,ct in ans:
    if ct == Max:
        print(i,end=" ")
print()
