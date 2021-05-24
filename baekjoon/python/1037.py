# 약수
# 정수론과 조합론

# if N == 12, A = 2, 3, 4, 6

factor_cnt = int(input())
factor = list(map(int, input().split()))

print(min(factor) * max(factor))