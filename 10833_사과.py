N=int(input())
tmp=0
for _ in range(N):
    s,n = map(int,input().split())
    tmp+= n%s #남은사과수
print(tmp)