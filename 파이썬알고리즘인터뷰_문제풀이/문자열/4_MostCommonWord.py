paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]
# 정규식을 이용해서 전처리 (데이터 클렌징)
import re
words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split()
        if word not in banned]
print("클렌징:",words)

#default dict 자료형을 이용
import collections
counts=collections.defaultdict(int) #default dict을 써야 바로 +=1 가능
for word in words:
    counts[word]+=1
print("1:",max(counts,key=counts.get)) #딕셔너리.get 문법 알아봐야함.


# Counter 모듈을 이용
counts2=collections.Counter(words)
#print(counts2.most_common(1))
print("2:",counts2.most_common(1)[0][0])

