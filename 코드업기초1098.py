w,h=map(int,input().split())
arr=[[0]*h for x in range(w)]
n=int(input())
for _ in range(n):
    l,d,x,y=map(int,input().split())
    for i in range(l):
        if d==0:
            arr[x-1][y-1+i]=1
        else:
            arr[x-1+i][y-1]=1
for a in arr:
    for x in a:
        print(x,end=' ')
    print()
