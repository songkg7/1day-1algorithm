# TITLE: 행복한지 슬픈지
# CATEGORY: 문자열
# DATE: 2021/09/03 7:19 오후

import re

s = input()
p_h = re.compile(r':-\)')
p_s = re.compile(r':-\(')

happy_count = len(p_h.findall(s))
sad_count = len(p_s.findall(s))

if happy_count == 0 and sad_count == 0:
    print('none')
elif happy_count == sad_count:
    print('unsure')
elif happy_count > sad_count:
    print('happy')
else:
    print('sad')

# ClearTime = 2021/09/03 7:27 오후
