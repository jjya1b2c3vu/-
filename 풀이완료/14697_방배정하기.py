(A,B,C,N)=tuple(map(int,input().split()))
result=0
for x in range(N):
    tmp1=A*x
    for y in range(N):
        tmp2=B*y
        for z in range(N):
            tmp3=C*z
            if(tmp1+tmp2+tmp3 == N):
                result=1
                break        
print(result)
