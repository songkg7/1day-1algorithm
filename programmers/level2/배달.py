# 
#
# 2021/07/16 7:06 오후

# TODO: 다시 풀기

from collections import deque

N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3


def solution(N, road, K):
    nodes = {}
    dist = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}
    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]

    que = deque([1])

    while que:
        cur_n = que.popleft()
        for next_n, d in nodes[cur_n]:
            if dist[next_n] > dist[cur_n] + d:
                dist[next_n] = dist[cur_n] + d
                que.append(next_n)

    print(nodes)
    print(dist)

    return len([True for dist in dist.values() if dist <= K])


print(solution(N, road, K))
