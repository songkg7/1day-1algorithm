# TITLE: 대칭 차집합
# CATEGORY: 자료구조
# DATE: 2021/09/05 11:36 오전

n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A ^ B))

# ClearTime = 2021/09/05 11:39 오전
