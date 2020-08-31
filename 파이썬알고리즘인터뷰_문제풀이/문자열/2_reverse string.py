#전통적인 방식  two pointer
def reverse_string(s:list)->None:
    left,right = 0 ,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
input_str=["a","b","c","e","d","f","g"]
reverse_string(input_str)
print("1",input_str)

#pysonic way
input_str2=["a","b","c","e","d","f","g"]
def reverse_string2(s:list)->None:
    s.reverse()
reverse_string2(input_str2)
print("2",input_str2)

#슬라이싱
s=["a","b","c","e","d","f","g"]
s=s[::-1] #이 방식이 오류가 나는 플랫폼도 있다
#s[:]=s[::-1] #이렇게 하면 되는 경우가 있으니 테스트가 가능하다면 미리 테스트
print("3",s)