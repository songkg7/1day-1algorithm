# TITLE: 카드1
# CATEGORY: 자료구조
# DATE: 2021/09/17 8:44 오후

from collections import deque

N = int(input())
tomb = []
cards = deque([i for i in range(1, N + 1)])

while cards:
    tomb.append(cards.popleft())  # 위에서 한 장...
    cards.rotate(-1)  # 아래로 한 장...

print(*tomb)

# ClearTime = 2021/09/17 8:53 오후
