# 단지번호붙이기
# 그래프 탐색
# 2021/06/12 9:48 오전

# TODO: 다시 풀기

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, str(input()))))

visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

num_list = []
nums = 0


def dfs(x, y):
    global nums
    nums += 1
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny)


for a in range(N):
    for b in range(N):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a, b)
            num_list.append(nums)
            nums = 0

print(len(num_list))
for n in sorted(num_list):
    print(n)
