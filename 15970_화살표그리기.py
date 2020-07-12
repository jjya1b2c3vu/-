test=dict()
'''
N=int(input("testcase: "))
for _ in range(N):
    a,b=map(int,input("a,b: ").split())
    test[a]=b
'''
test={0: 1, 1: 2, 3: 1, 4: 2, 5: 1}
print(test.keys())
color=1
cnt=0
for x in test.keys():
    temp=[]
    if test[x] is color:
        temp.append(x)
        temp_min=[]
        print(temp)
        l=len(temp)
        for y in temp:
            for z in temp:
                print(abs(y-z))
         