arr=list()
for _ in range(10):
    temp=list(map(int,input().split()))
    arr.append(temp)
x,y=2,2
while(True):
    if arr[x-1][y-1]==2:
        arr[x-1][y-1]=9
        break
    arr[x-1][y-1]=9 #지나간 자취 색칠
    if arr[x-1][y-1+1]==0 or arr[x-1][y-1+1]==2: #오른쪽 통로
        y+=1 #오른쪽 한칸이동
    else: #오른쪽 벽
        if arr[x-1+1][y-1]==0 or arr[x-1+1][y-1]==2: #아래에 통로
            x+=1 #아래 한칸이동
        else: #오른쪽과 아래 벽
            break    
for a in arr:
    for x in a:
        print(x,end=' ')
    print()
