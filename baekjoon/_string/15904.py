# TITLE: UCPC 는 무엇의 약자일까?
# CATEGORY: 문자열
# DATE: 2021/08/25 8:06 오후

s = input()
words = ['U', 'C', 'P', 'C']

flag = True
for i in range(4):
    idx = s.find(words[i])
    if idx != -1:
        s = s[idx + 1:]
    else:
        flag = False
        break

print('I love UCPC' if flag else 'I hate UCPC')

# ClearTime = 2021/08/25 8:42 오후
