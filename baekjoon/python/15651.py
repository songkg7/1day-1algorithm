# N과 M (3)
# 백트래킹

def DFS(L):
    if L == M:
        for x in res:
            print(x, end=' ')
        print()
    else:
        for i in range(1, N + 1):
            res[L] = i
            DFS(L + 1)


N, M = map(int, input().split())
res = [0] * M
DFS(0)
