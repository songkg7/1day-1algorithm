# TITLE: 주사위 세개
# CATEGORY: 수학
# DATE: 2021/09/28 9:15 오후

from collections import Counter

dice = Counter(map(int, input().split()))

v = dice.most_common()
count = v[0][1]
w = v[0][0]
if count == 3:
    print(10000 + w * 1000)
elif count == 2:
    print(1000 + w * 100)
else:
    print(sorted(v, reverse=True)[0][0] * 100)

# ClearTime = 2021/09/28 9:45 오후
