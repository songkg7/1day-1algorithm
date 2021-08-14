# 베스트셀러
# 문자열
# 2021/08/14 2:03 오전

from collections import Counter

N = int(input())

books = [input() for _ in range(N)]

result = sorted(Counter(books).most_common(), key=lambda x: (-x[1], x[0]))
print(result[0][0])

# ClearTime = 2021/08/14 2:17 오전
