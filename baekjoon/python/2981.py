# 검문
# 정수론 및 조합론

# FIXME: 시간초과, 입력으로 1,000,000,000 보다 작거나 같은 자연수가 들어온다. 범위가 매우 넓으므로 고려해야한다.

N = int(input())
nums = [int(input()) for _ in range(N)]

answer = []
for M in range(2, min(nums) + 1):
    result = set(map(lambda x: x % M, nums))
    if len(result) == 1:
        answer.append(M)

print(*answer)
