# 운동
# 최단 경로
# 2021/07/23 8:57 오후

# FIXME: 미해결

import heapq
import sys
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())
nodes = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes[a].append((b, c))


def dijkstra(start):
    dist = {i: float('inf') if i != start else 0 for i in range(1, V + 1)}
    heap = [(0, start)]

    result = float('inf')

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if dist[cur_node] < cur_dist:
            continue

        for next_node, next_dist in nodes[cur_node]:

            # 시작점으로 돌아갈 수 있다면
            if next_node == start and result > dist[cur_node] + next_dist:
                result = dist[cur_node] + next_dist

            new_dist = next_dist + cur_dist
            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return result


cycle = []
for r in nodes.keys():
    d = dijkstra(r)
    if d != float('inf'):
        cycle.append(d)

print(min(cycle) if cycle else -1)

# ClearTime = 2021/07/23 9:53 오후 - 시간 초과
