# 미확인 도착지
# 최단 경로 응용
# 2021/07/17 3:24 오후

import sys
import heapq


def dijkstra(start, end):
    dist = {i: float('inf') if i != start else 0 for i in range(1, n + 1)}

    heap = [start]

    while heap:
        cur_node = heapq.heappop(heap)

        if not nodes[cur_node]:
            continue

        for next_node, d in nodes[cur_node]:
            if dist[next_node] > dist[cur_node] + d:
                dist[next_node] = dist[cur_node] + d
                heapq.heappush(heap, next_node)

    return dist[end]


T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    nodes = {}
    candidates = []

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        nodes[a] = nodes.get(a, []) + [(b, d)]
        nodes[b] = nodes.get(b, []) + [(a, d)]

    for _ in range(t):
        x = int(sys.stdin.readline())
        candidates.append(x)

    # g h 를 지나서 가는 길이 스타트 지점부터 두개의 목적지까지 가는 최소 경로와 같다면 정답에 포함
    result = []
    for i in range(len(candidates)):
        result.append(dijkstra(s, candidates[i]))

    answer = []

    # 중간 경로
    gh = dijkstra(g, h)

    for i in range(len(result)):
        sh1 = dijkstra(s, h) + gh + dijkstra(g, candidates[i])
        sg1 = dijkstra(s, g) + gh + dijkstra(h, candidates[i])

        if min(sh1, sg1) in result:
            answer.append(candidates[i])

    answer.sort()

    print(*answer)

# ClearTime = 2021/07/17 4:50 오후 - 시간 초과
