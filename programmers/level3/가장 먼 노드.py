# 
# graph
# 2021/07/17 4:53 오전

from collections import deque

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


def solution(n, vertex):
    nodes = {}
    for v1, v2 in vertex:
        nodes[v1] = nodes.get(v1, []) + [(v2, 1)]
        nodes[v2] = nodes.get(v2, []) + [(v1, 1)]
    dist = {i: float('inf') if i != 1 else 0 for i in range(1, n + 1)}

    que = deque([1])

    while que:
        cur_node = que.popleft()
        for next_node, d in nodes[cur_node]:
            if dist[next_node] > dist[cur_node] + d:
                dist[next_node] = dist[cur_node] + d
                que.append(next_node)

    return len(list(filter(lambda x: x[1] == max(dist.values()), dist.items())))


print(solution(n, vertex))

# ClearTime = 2021/07/17 5:08 오전
