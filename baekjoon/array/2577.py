# 숫자의 개수
# 1차원 배열

# NOTE: str.count() 를 활용해서 푸는 것도 가능

from collections import Counter

A, B, C = [int(input()) for _ in range(3)]
word = Counter(list(str(A * B * C)))

for i in range(10):
    print(word[str(i)])
