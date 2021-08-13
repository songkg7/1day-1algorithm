# 단어공부
# 문자열

from collections import Counter

word = input().upper()
if len(word) == 1:
    print(word)
else:
    x = Counter(word).most_common()
    print('?' if x[0][1] == x[1][1] else x[0][0])
