# 정수 삼각형
# DP
# 2021/06/10 3:50 오후

n = int(input())
tri = [[0]]
for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(2, n + 1):
    for j in range(i):
        # 왼쪽 끝일 때
        if j == 0:
            tri[i][0] += tri[i - 1][0]
        # 오른쪽 끝일 때
        elif j == i - 1:
            tri[i][j] += tri[i - 1][-1]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[-1]))

# ClearTime = 2021/06/10 4:03 오후
