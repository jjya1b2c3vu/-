x=[1,2,3,4]
out=[]
p=1
for i in range(len(x)):
    out.append(p)
    p=p*x[i]
print(out)
p=1
for j in range(len(x)-1,0-1,-1):
    out[j]=out[j]*p
    p=p*x[j]
print(out)
