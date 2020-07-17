import sys
import copy
sys.stdin = open("input.txt", "r")
N,C=map(int,input().split())
M=int(input())
info=list()
truck=list()
capacity=0
result=0
for _ in range(M):
    info.append(list(map(int,input().split())))
info.sort()
for n in range(1,N+1):
    for t in truck[:]: #내리기
        if len(truck) is 0:
            break
        if t[1]==n:
            capacity-=t[2]
            result+=t[2]
            truck.remove(t)               
    for t in info:
        if n is N:
            break
        if t[0]==n: #짐 싣기
            capacity+=t[2]
            if capacity>C:
                t[2]=t[2]+(C-capacity)
                capacity=C
                if t[2]==0:
                    pass
                else:
                    truck.append(t)
                    
            else:
                truck.append(t)
                
    #print(truck,capacity,result)
print(result)
    



    