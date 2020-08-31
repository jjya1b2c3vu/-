height=[0,1,0,2,1,0,1,3,2,1,2,1]

#투 포인터를 이용한 풀이
left,right=0,len(height)-1
vol=0
left_max=height[left]
right_max=height[right]

while left < right:
    left_max= max(height[left],left_max)
    right_max =max(height[right],right_max)
    if left_max<=right_max:
        vol+= left_max-height[left]
        left+=1
    else:
        vol+= right_max-height[right]
        right-=1
print(vol)

#스텍을 이용한 풀이 , 이해못함...
stack=[]
vol=0
i=0
print(stack and height[i]> height[stack[-1]])
