input_str="A man, a plan, acanal: Panama"

strs=[]
#문자열 공백제거하고 소문자화 시킴
for char in input_str:
    if char.isalnum():
        strs.append(char.lower())
#파이선 문자열 슬라이싱 기능 이용한 풀이
print("0",end=" ")      
if strs[::]==strs[::-1]:
    print("True")
else:
    print("False")

#pop mothod 이용한 풀이  O(n^2)
def is_palindrome(s:str) -> bool: 
    strs2=list()
    for char in s:
        if char.isalnum():
            strs2.append(char.lower())
    while len(strs2)>1:
        if strs2.pop(0)!=strs2.pop():
            return False
    return True

print("1",is_palindrome(input_str))

#Deque 자료형을 이용한 풀이(최적화) 리스트보다 5배빠름 O(n)
from collections import deque
def is_palindrome_2(s:str)->bool:
    #자료형데크로 선언
    strs3: deque = deque()

    for char in s:
        if char.isalnum():
            strs3.append(char.lower())
    while len(strs3)>1:
        if strs3.popleft() != strs3.pop(): #pop(0) 대신에 popleft()
            return False
    return True
print("2",is_palindrome_2(input_str))

# 정규식과 문자열 슬라이싱, 이게 젤빠름
import re
def is_palindrome_3(s:str)->bool:
    s=s.lower()
    #정규식을 이용한 불필요한 문자열 제거
    s=re.sub('[^a-z0-9]','',s)  #어떤의미인지 알아봐야함
    return s== s[::-1]
print("3",is_palindrome_3(input_str))
