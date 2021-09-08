# 정수 삼각형
# DP
# 2021/05/26 12:05 오전

# TODO: 다시 풀기

n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(t[i])):
        # 삼각형의 왼쪽 끝일 때
        if j == 0:
            t[i][j] += t[i - 1][j]
        # 삼각형의 우측 끝일 때
        elif j == i:
            t[i][j] += t[i - 1][j - 1]
        # 삼각형의 중간일 때는 위의 값들 중 큰 값을 더한다.
        else:
            t[i][j] += max(t[i - 1][j - 1], t[i - 1][j])

print(max(t[-1]))
