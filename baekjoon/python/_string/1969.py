# TITLE: DNA
# CATEGORY: 문자열
# DATE: 2021/08/22 9:36 오후

# 가장 유사도가 높은 DNA 배열 찾기
# 즉 각 글자 순서에서 가장 많은 글자를 찾는 것

from collections import Counter

N, M = map(int, input().split())
dna = [input() for _ in range(N)]

s = zip(*dna)
result = []
for i in s:
    common = sorted(Counter(i).most_common(), key=lambda x: (-x[1], x[0]))
    result.append(common[0][0])

count = 0
for i in dna:
    count += len(list(filter(lambda x: x[0] != x[1], zip(i, result))))

print(''.join(result))
print(count)

# ClearTime = 2021/08/22 9:59 오후
