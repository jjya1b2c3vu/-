nums=[-1,0,1,2,-1,-4]
#1. 브루트포스 O(n^3) 타임아웃
nums.sort()
print(1,nums)
result=[]
for i in range(len(nums)-2):
    if i>0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1,len(nums)-1):
        if j>i+1 and nums[j] == nums[j-1]:
            continue
        for k in range(j+1,len(nums)):
            if k>j+1 and nums[k]==nums[k-1]:
                continue
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i],nums[j],nums[k]])
print(result)

#2. two 포인터를 이용한 합
nums.sort()
print(2,nums)
result=[]
for i in range(len(nums)-2):
    if i>0 and nums[i] == nums[i-1]:
        continue
    left,right=i+1,len(nums)-1
    while left<right:
        sums=nums[i]+nums[left]+nums[right]
        if sums<0:
            left+=1
        elif sums>0:
            right-=1
        else:
            result.append([nums[i],nums[left],nums[right]])

            while left<right and nums[left] == nums[left+1]:
                left +=1
            while left>right and nums[right]==nums[right-1]:
                right-=1
            left +=1
            right -=1
print(result)