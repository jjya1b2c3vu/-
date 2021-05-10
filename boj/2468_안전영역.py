from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
stdin = open("input.txt","r")
input = stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
Max_high=0
for t in graph:
    temp=max(t)
    Max_high=max(Max_high,temp)

def dfs(x,y,high):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    #방문 하지 않음
    if visited[x][y]>=high:
        visited[x][y]=0
        #상,하,좌,우 탐색
        dfs(x-1,y,high)
        dfs(x,y-1,high)
        dfs(x+1,y,high)
        dfs(x,y+1,high)
        return True
    return False
ans=[]
import copy
for h in range(1,Max_high+1):
    result=0
    visited = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if dfs(i,j,h)==True:
                result+=1
    ans.append(result)
print(max(ans))