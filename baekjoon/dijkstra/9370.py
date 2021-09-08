# 미확인 도착지
# 최단 경로 응용
# 2021/07/17 3:24 오후

import sys
import heapq


def dijkstra(start):
    dist = {i: float('inf') if i != start else 0 for i in range(1, n + 1)}

    heap = [(0, start)]

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if dist[cur_node] < cur_dist:
            continue

        for next_node, d in nodes[cur_node]:
            new_d = cur_dist + d
            if dist[next_node] > new_d:
                dist[next_node] = new_d
                heapq.heappush(heap, (new_d, next_node))
    return dist


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
    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    answer = []

    # 중간 경로
    for goal in candidates:
        sh1 = s_[h] + h_[g] + g_[goal]
        sg1 = s_[g] + g_[h] + h_[goal]

        if sh1 != float('inf') or sg1 != float('inf'):  # 목적지에 도달할 수 없는 경우 제외
            if sh1 == s_[goal] or sg1 == s_[goal]:
                answer.append(goal)

    answer.sort()

    print(*answer)

# ClearTime = 2021/07/17 4:50 오후 - 시간 초과
# ClearTime = 2021/07/17 5:47 오후
