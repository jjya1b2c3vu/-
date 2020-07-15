#T=int(input())
T=100
A=5*60
B=60
C=10
a=T//A
T_=T-a*A
b=T_//B
T__=T_-b*B
c=T__//C

if A*a+B*b+C*c ==T:
    print(a,b,c)
else:
    print(-1)