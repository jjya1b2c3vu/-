buff={}
def fibo(x):
    if x in buff:
        return buff[x]
    if x==1 or x==2:
        buff[x]=1
        return 1
    else:
        buff[x]=fibo(x-1)+fibo(x-2)
        return buff[x]
def result(x):
    return 2*fibo(x)+2*fibo(x+1)
print(result(int(input())))
