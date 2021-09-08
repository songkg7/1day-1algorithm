# TITLE: 가장 많은 글자
# CATEGORY: 문자열
# DATE: 2021/08/26 5:33 오후

import sys
from collections import Counter

words = ''

while True:
    s = sys.stdin.readline()
    if not s:
        break
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    words += s

result = sorted(Counter(words).most_common(), key=lambda x: (-x[1], x[0]))
answer = filter(lambda x: x[1] == result[0][1], result)
answer = list(map(lambda x: x[0], answer))
print(''.join(answer))

# ClearTime = 2021/08/26 6:00 오후
