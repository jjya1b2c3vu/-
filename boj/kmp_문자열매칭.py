def make_table(pattern):
    global table
    j = 0
    for i in range(1,len(pattern)):
        while(j>0 and pattern[i]!=pattern[j]):
            j= table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j

def KMP(string,pattern):
    global table
    j=0
    ans=0
    for i in range(len(string)):
        while(j>0 and string[i]!=pattern[j]):
            j = table[j-1]
        if string[i]==pattern[j]:
            if j==len(pattern)-1:
                # print("find",end=" ")
                # print(i-len(pattern)+2)
                ans+=1
                j=table[j]
            else:
                j+=1
    return ans

string = "baekjoon"
pattern = "aek"
table = [0] * len(pattern)
make_table(pattern)
print(KMP(string,pattern))
