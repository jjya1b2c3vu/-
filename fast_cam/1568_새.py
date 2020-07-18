n=int(input())
cnt=0
left=n
k=0
while(left!=0):
    k+=1 
    if left<k:
        k=1  
    left-=k
    cnt+=1
print(cnt)