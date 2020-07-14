import sys
sys.stdin = open("input.txt", "r")
box=[[0]*101 for x in range(101)]

N=int(input())
for n in range(1,N+1):
    y,x,h,w = map(int,input().split())
    for i in range(y,y+h):
        for j in range(x,x+w):
            box[i][j]=n
        
def count_x(BOX,n):
    result=0
    for x in BOX:
        result+=x.count(n)
    return result
for n in range(1,N+1):
    print(count_x(box,n))

         
