import sys
sys.stdin = open("tmp_input.txt", "r")
N,K=map(int,input().split())
grad1=list()
grad2=list()
grad3=list()
grad4=list()
grad5=list()
grad6=list()
def div(sex,year):
    if year==1:
        grad1.append(sex)
    elif year==2:
        grad2.append(sex)
    elif year==3:
        grad3.append(sex)
    elif year==4:
        grad4.append(sex)
    elif year==5:
        grad5.append(sex)
    elif year==6:
        grad6.append(sex)
def count_room(grad): 
    n0=grad.count(0)
    n1=grad.count(1)
    room_0=(n0//K)+(n0%K)
    room_1=(n1//K)+(n1%K)
    return room_0+room_1
for _ in range(N):
    S,Y=map(int,input().split())
    div(S,Y)
print(count_room(grad1)+count_room(grad2)+count_room(grad3)
+count_room(grad4)+count_room(grad5)+count_room(grad6))
