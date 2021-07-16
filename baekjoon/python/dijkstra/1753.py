# 최단 경로
# Dijkstra
# 2021/07/16 8:44 오후

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(graph, V, start):
    heap = [(0, start)]
    distance = defaultdict(int)

    while heap:
        dist, cur_node = heapq.heappop(heap)
        if cur_node not in distance:
            distance[cur_node] = dist
            for v, w in graph[cur_node]:
                update = dist + w
                heapq.heappush(heap, (update, v))

    for i in range(1, V + 1):
        if i == start:
            print('0')
        elif not distance[i]:
            print('INF')
        else:
            print(distance[i])


dijkstra(graph, V, K)
