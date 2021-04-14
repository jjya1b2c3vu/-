def solve_maze(g, start, red , blue):
    qu = []           # 기억 장소 1: 앞으로 처리해야 할 이동 경로를 큐에 저장
    done = set()      # 기억 장소 2: 이미 큐에 추가한 꼭짓점들을 집합에 기록(중복 방지)
 
    qu.append(start)   # 출발점을 큐에 넣고 시작
    done.add(start)    # 집합에도 추가
 
    while qu:          # 큐에 처리할 경로가 남아 있으면
        p = qu.pop(0)  # 큐에서 처리 대상을 꺼냄
        i,j = p[-1]      # 큐에 저장된 이동 경로의 마지막 문자가 현재 처리해야 할 꼭짓점
        if v == red:  # 처리해야 할 꼭짓점이 도착점이면(목적지 도착!)
            return p   # 지금까지의 전체 이동 경로를 돌려주고 종료
        for x in g[i][j]: # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done:     # 아직 큐에 추가된 적이 없는 꼭짓점을
                qu.append(p + x)  # 이동 경로에 새 꼭짓점으로 추가하여 큐에 저장하고
                done.add(x)       # 집합에도 추가

from sys import stdin
from pprint import pprint
stdin = open("swea/input.txt","r")
input = stdin.readline
n,m = map(int,input().split())
print(n,m)
maze = [list(input().rstrip()) for _ in range(n)]
pprint(maze)
start,red,blue=(),(),()
for i in range(m):
    for j in range(n):
        if maze[i][j]=='O':
            start = (i,j)
        if maze[i][j]=="R":
            red = (i,j)
        if maze[i][j]=="B":
            blue = (i,j)
print(start,red,blue)

solve_maze(maze,start,red,blue)

