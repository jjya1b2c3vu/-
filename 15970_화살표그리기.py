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
for x in test.keys():
    if x is color:
