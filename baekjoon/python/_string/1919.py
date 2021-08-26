# TITLE: 애너그램 만들기
# CATEGORY: 문자열
# DATE: 2021/08/26 4:57 오후

# 두 배열의 요소 중에서 한쪽에만 존재하는 문자를 찾는다

from collections import Counter

a = Counter(input())
b = Counter(input())

print((a.keys() ^ b.keys()))
print(sum(((a | b) - (a & b)).values()))

# ClearTime = 2021/08/26 5:16 오후
