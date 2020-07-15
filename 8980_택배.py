import sys
sys.stdin = open("input.txt", "r")
N,C=map(int,input().split())
M=int(input())
info=list()
truck=list()
capacity=0
for _ in range(M):
    info.append(list(map(int,input().split())))

for n in range(1+1):
    for t in info:
        if t[0]==n:
            capacity+=t[2]
            truck.append(t)
print(truck,capacity)


    