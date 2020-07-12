def result(number):
    if number<1:
        print("D")
        return 0
    if(tmp_a.count(number)>tmp_b.count(number)):
        print("A")
    elif(tmp_a.count(number)<tmp_b.count(number)):
        print("B")
    elif(tmp_a.count(number)==tmp_b.count(number)):
        number-=1
        result(number)
import sys
sys.stdin = open("tmp_input.txt", "r")
N=int(input(""))
for _ in range(N):
    tmp_a=list(map(int,input().split()))
    #print(tmp_a)
    tmp_b=list(map(int,input().split()))
    #print(tmp_b)
    tmp_a.pop(0)
    tmp_b.pop(0)
    result(4)
