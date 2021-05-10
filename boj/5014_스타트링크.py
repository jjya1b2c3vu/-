from sys import stdin
from collections import deque
stdin = open("input.txt","r")
input = stdin.readline

F, S, G, U, D = map(int,input().split())
visited = [False]*(F+1+D)
def bfs(x):
    qu = deque([])
    visited[x] = True
    qu.append(x)
    ans = []
    cnt=0
    while(qu):
        now = qu.popleft()
        if now==G:
            return cnt
        elif now<G:
            nx = now + U
            if 1<=nx<=F+U and visited[nx]==False:
                visited[nx] = True
                qu.append(nx)
                cnt+=1
        elif now>G:
            nx = now - D
            if 1<=nx<=F+D and visited[nx]==False:
                visited[nx] = True
                qu.append(nx)
                cnt+=1
    return -1

ans = bfs(S)
if ans == -1:
    print("use the stairs")
else:
    print(ans)

