logs=["dig1 8 1 5 1","let1 art can","dig2 3 6",
      "let2 own kit dig","let3 art zero"]
def sort_log(log:list)->list:
    digits=[]
    letters=[]
    for log in logs:
        if log.split()[1].isdigit(): #로그의 1번 index가 숫자로 변환가능 이면
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
    return letters+digits

print(sort_log(logs))