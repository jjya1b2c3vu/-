from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
stdin = open("input.txt","r")

input = stdin.readline
M,N,K = map(int,input().split())
mat = [[0]*N for _ in range(M)]

List = []
for _ in range(K):
    temp = list(map(int,input().split()))
    List.append(temp)

for x1,y1,x2,y2 in List:
    for i in range(y1,y2):
        for j in range(x1,x2):
            mat[M-1-i][j]=1

def dfs(y,x):
    if y<0 or x<0 or y>=M or x>=N:
        return [False,0]
    global cnt
    if visited[y][x]==0:
        visited[y][x]=1
        cnt+=1
        dfs(y-1,x)
        dfs(y,x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return [True,cnt]
    return [False,0]
import copy
visited = copy.deepcopy(mat)
ans=0
S_list = []
for i in range(M):
    for j in range(N):
        cnt=0
        flag, S =dfs(i,j)
        if flag == True:
            ans+=1
            S_list.append(S)
print(ans)
print(*sorted(S_list))
