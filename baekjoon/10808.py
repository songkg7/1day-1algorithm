# 알파벳 개수
# String
# 2021/08/13 6:11 오후

import string

count = {}

w = input()
lowercase = string.ascii_lowercase
for s in lowercase:
    count[s] = w.count(s)

print(*count.values())

# ClearTime = 2021/08/13 6:19 오후
