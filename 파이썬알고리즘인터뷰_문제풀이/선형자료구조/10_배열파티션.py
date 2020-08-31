input0=[1,4,3,2]
#정렬해서 짝수번 인덱스를 출력하는 것과 동일
input0.sort()
result=0
for i,n in enumerate(input0):
    if i%2==0:
        result+=n
print(result)

#파이썬 스럽게
print(sum(sorted(input0)[::2]))