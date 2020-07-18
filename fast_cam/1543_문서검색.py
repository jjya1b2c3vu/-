import sys
sys.stdin=open("fast_cam/input.txt", "r")
text=input()
search=input()
i=0
cnt=0
while(i+len(search) <= len(text)):
    if text[i:i+len(search)]==search:
        cnt+=1
        i+=len(search)
    else:
        i+=1
print(cnt)

    
