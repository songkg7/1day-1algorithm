# 단어 뒤집기 2
# 문자열
# 2021/08/14 12:28 오전

# 태그 안의 내용은 뒤집지 말기
# 정규식을 만드는게 핵심

import re

p = re.compile(r'<[a-z\s\d]+>|[a-z\d\s]+')

s = input()

words = p.findall(s)

for i in range(len(words)):
    if words[i][0] == '<':
        continue
    else:
        tmp = list(map(lambda x: x[::-1], words[i].split(' ')))
        words[i] = ' '.join(tmp)

print(''.join(words))

# ClearTime = 2021/08/14 2:01 오전
