import sys
n=int(sys.stdin.readline())
arr=list()
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
for x in sorted(arr):
    print(x)