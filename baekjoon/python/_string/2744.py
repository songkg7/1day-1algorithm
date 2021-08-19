# TITLE: 대소문자 바꾸기
# CATEGORY: 문자열
# DATE: 2021/08/19 4:30 오후

s = list(input())
for i in range(len(s)):
    s[i] = s[i].lower() if s[i].isupper() else s[i].upper()

print(''.join(s))

# ClearTime = 2021/08/19 4:37 오후
