#
#
# 2021/07/15 6:59 오후

import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0

    flag = True
    while flag:
        min1 = heapq.heappop(scoville)
        if not scoville and min1 < K:
            count = -1
            break

        if min1 < K:
            min2 = heapq.heappop(scoville)
            result = min1 + (min2 * 2)
            count += 1
            heapq.heappush(scoville, result)
        else:
            heapq.heappush(scoville, min1)
            flag = False

    return count


print(solution(scoville, K))

# ClearTime = 2021/07/15 7:20 오후
