nums=[2,7,11,15]
target=18
#1 부루트포스 O(n^2)
for x in range(len(nums)):
    for y in range(x+1,len(nums)):
        if nums[x]+nums[y] == target:
            print(x,y)

#2 in을 이용한 탐색 -> 같은 시간복잡도 이지만 상수쪽이 더빠르게 된다. O(n^2)
for i,n in enumerate(nums): #인덱스랑 숫자로 반환
    complement = target -n

    if complement in nums[i+1:]:
        print(nums.index(n), nums[i+1:].index(complement) + (i+1))
             #n의 인덱스 , i+1~끝 까지중 complement의 인덱스


#3  첫 번째 수를 뺀 결과 키 조회 (가장 빠른방법) O(n)
nums_map={}
for i ,num in enumerate(nums):
    nums_map[num]=i
#타겟-첫번째 수 를 key로 조회
for i ,num in enumerate(nums):
    if target-num in nums_map and i!= nums_map[target-num]:
        print(nums.index(num),nums_map[target-num])
        break

#4 3을 최적화

nums_map={}
for i , num in enumerate(nums):
    if target-num in nums_map:
        print(nums_map[target-num],i)
        break
    nums_map[num]=i


