# TITLE: 모음의 개수
# CATEGORY: 문자열
# DATE: 2021/08/18 10:39 오후

s = input()
count = 0
for i in s:
    if i in 'aeiou':
        count += 1

print(count)

# ClearTime = 2021/08/18 10:40 오후
