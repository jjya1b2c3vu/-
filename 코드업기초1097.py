arr0=list()
for _ in range(19):
    temp=list(map(int,input().split()))
    arr0.append(temp)
k = int(input())
for _ in range(k):
    x,y=map(int,input().split())
    for i in range(19):
        if(arr0[x-1][i]==0):arr0[x-1][i]=1
        else: arr0[x-1][i]=0
    for j in range(19):
        if(arr0[j][y-1]==0):arr0[j][y-1]=1
        else:arr0[j][y-1]=0
for x in arr0:
    for y in x:
        print(y,end=" ")
    print()

