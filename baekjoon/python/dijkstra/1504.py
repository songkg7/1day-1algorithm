# 특정한 최단 경로
# Dijkstra
# 2021/07/16 11:25 오후

import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

nodes = {}
for a, b, c in road:
    nodes[a] = nodes.get(a, []) + [(b, c)]
    nodes[b] = nodes.get(b, []) + [(a, c)]

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(root, goal):
    dist = {i: float('inf') if i != root else 0 for i in range(1, N + 1)}

    heap = [(dist[root], root)]

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        # dict key error 방지
        if not nodes.get(cur_node, []):
            continue

        for next_node, d in nodes[cur_node]:
            if dist[next_node] > dist[cur_node] + d:
                dist[next_node] = dist[cur_node] + d
                heapq.heappush(heap, (dist[next_node], next_node))

    return dist[goal]


path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

result = min(path1, path2)
print(result if result < float('inf') else -1)

# ClearTime = 2021/07/17 12:19 오전
