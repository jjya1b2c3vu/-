def solution(n,k,cmds):
    n_list = [ i for i in range(n)]
    s_list = list("O"*n)
    idx = k
    stack = []
    for cmd in cmds:
        c = cmd.split()
        if c[0]=="D":
            t = len(list(filter(lambda x: x>idx,stack)))
            idx += int(c[1])+t
        if c[0]=="U":
            t = len(list(filter(lambda x: x<idx,stack)))
            idx -= int(c[1])+t
        if c[0]=="C":
            s_list[idx]="X"
            stack.append(idx)
            idx+=1
            while(s_list[idx]=="X"):
                idx+=1
            if idx == n-1:
                idx-=1
        if c[0]=="Z":
            t = stack.pop()
            s_list[t]="O"
            
    return n_list,s_list


# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))



from collections import deque

MAX = float('inf')
def man_dist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)


def get_participant(board):
    participant = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'P':
                participant.append((i,j))
    return participant

move = [(0,1),(1,0),(0,-1),(-1,0)]
def check(board):
    participant = get_participant(board)
    n = len(participant)

    for i in range(1, n):
        for j in range(i):
            r1, c1 = participant[i]
            r2, c2 = participant[j]

            #거리가 2 초과일 때
            if man_dist(r1, c1, r2, c2) > 2:
                continue

            #거리가 1일 때
            queue = deque([])
            for dr, dc in move:
                nr, nc = r1 + dr, c1 + dc
                if 0 <= nr < 5 and 0 <= nc < 5:
                    if board[nr][nc] == 'X':
                        queue.append((nr,nc,True))
                    elif board[nr][nc] == 'P':
                        return False
                    else:
                        queue.append((nr,nc,False))

            #거리가 2일 때
            while queue:
                r, c, flag = queue.popleft()
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5:
                        if (nr, nc) == (r1,c1):
                            continue
                        if board[nr][nc] == 'P' and flag == False:
                            return False
    return True



def solution2(places):
    boards = []
    for place in places:
        boards.append(list(map(list, place)))

    res = [1 if check(board) else 0 for board in boards]
    return res


print(solution2([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))