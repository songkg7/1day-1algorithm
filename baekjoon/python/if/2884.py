# 알람 시계
# if
# 2021/06/06 8:06 오전

H, M = map(int, input().split())
result = []

if H == 0:
    H = 24
time = H * 60 + M - 45

result.append(0 if time // 60 == 24 else time // 60)
result.append(time % 60)

print(*result)

# ClearTime = 2021/06/06 8:24 오전
