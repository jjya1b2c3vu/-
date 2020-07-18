n=int(input())
m=list()
for _ in range(n):
    m.append(input())
ans=dict()
for x in m:
    if x not in ans.keys():
        ans[x]=1
    else:
        ans[x]+=1
target= max(ans.values())
arr=list()
for book,num in ans.items():
    if num == target:
        arr.append(book)
print(sorted(arr)[0])