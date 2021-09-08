# KMP는 왜 KMP일까?
# 문자열
# 2021/08/13 6:47 오후

# 1. 평범한 풀이
# 2. 정규식

import re

p = re.compile(r'[A-Z]')
s = input()

print(''.join(p.findall(s)))

# ClearTime = 2021/08/13 6:50 오후
