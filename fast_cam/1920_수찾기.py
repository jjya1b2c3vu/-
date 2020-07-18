N=int(input())
n=set(map(int,input().split()))
M=int(input())
m=set(map(int,input().split()))
for i in m:
    if i not in n:
        print('0')
    else:
        print('1')
#set 자료형을 이용해서 간단히 체크 가능

