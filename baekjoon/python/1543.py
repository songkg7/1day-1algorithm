# 문서 검색
# 문자열
# 2021/08/14 12:44 오후

# loop 를 좀 더 효율적으로 실행시킬 수 있을 것 같다.

s = input()
word = input()

count = 0
while word in s:
    idx = s.find(word)
    s = s[idx+len(word):]
    count += 1

print(count)

# ClearTime = 2021/08/14 12:56 오후
