# TITLE: 인형들
# CATEGORY: 카카오 코드 페스티벌 예선
# DATE: 2021/08/19 2:47 오후

import math

N, K = map(int, input().split())
nums = list(map(int, input().split()))

result = []

for k in range(K, N + 1):
    for i in range(N - k + 1):
        selected = nums[i:i + k]

        m = sum(selected) / len(selected)  # 평균
        s = sum(map(lambda a: (a - m) ** 2, selected)) / len(selected)  # 분산

        answer = round(math.sqrt(s), 11)  # 표준 편차
        result.append(abs(answer))

print(min(result))

# ClearTime = 2021/08/19 3:24 오후
