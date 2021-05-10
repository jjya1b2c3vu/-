from sys import stdin
from collections import deque
stdin = open("input.txt","r")
input = stdin.readline
R , C = map(int,input().split())
mat = [list(input().split()) for _ in range(R)]


for i in mat:
    print(i)

def bfs(a,b):
    qu = deque([])
    visited = [[0]*C for _ in range(R)]
    visited[a][b] = 1
    qu.append((a,b,fa,fb))
    while(qu):
        now_a,now_b = qu.popleft()
        for i,j in [(1,0),(0,1),(-1,0)(0,-1)]:
            nx_a,nx_b = now_a+i,now_b+j
            if mat[nx_a][nx_b]=='.' and visited[nx_a][nx_b]==0:
                qu.append((nx_a,nx_b))
                visited[nx_a][nx_b] = visited[now_a][now_b] + 1
            elif mat[nx_a][nx_b]=='#':
                pass
            elif mat[nx_a][nx_b]=='F':
                pass
        for i,j in [(1,0),(0,1),(-1,0)(0,-1)]:
            nx_fa,nx_fb = fa
            if mat[fa_i][fa_j]=='.':
                mat[fa_i][fa_j]='F'