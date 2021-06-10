# RGB 거리
# DP
# 2021/05/25 11:31 오후

# ClearTime = 2021/05/26 12:05 오전

# re
#
# 2021/06/10 3:11 오후

N = int(input())
color = []
for _ in range(N):
    color.append(list(map(int, input().split())))

for i in range(1, N):
    color[i][0] += min(color[i - 1][1], color[i - 1][2])
    color[i][1] += min(color[i - 1][0], color[i - 1][2])
    color[i][2] += min(color[i - 1][0], color[i - 1][1])

print(min(color[-1][0], color[-1][1], color[-1][2]))

# ClearTime = 2021/06/10 3:20 오후
