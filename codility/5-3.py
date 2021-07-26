#
# prefix sums
# 2021/07/26 1:15 오후

# 평균이 최소인 슬라이스의 위치 찾기

# Dynamic programming
# 0 에서부터 하나씩 더해가면서 합계를 저장한다.
# 끝에 도달하면 합계에서 배열의 앞부터 하나씩 빼면서 다시 구한다.
# 가장 작은 평균값일 때 시작 인덱스를 저장해놓는다.
# 최종적으로 시작 인덱스의 값을 리턴한다.
# ❌ 중간 범위를 구하지 못한다.

# for loop
# 2. 루프를 돌며 계산하기.
# 효율성을 통과하지 못할 것이라 예상되지만, 정답을 구할 수는 있는 방법.
# 결국 시간 제한을 통과하기 위해서 DP 와 같은 방법을 고려해야할 것으로 보인다.

import heapq

A = [4, 2, 2, 5, 1, 5, 8]


def solution(A):
    result = []

    for p in range(len(A)):
        for q in range(p + 1, len(A)):
            # print(f'시작 인덱스 = {p}')
            # print(f'마지막 인덱스 = {q}')
            s_j = 0
            for j in range(p, q + 1):
                s_j += A[j]
            # print(f'합계 = {s_j}')

            avg = s_j / (q - p + 1)
            # print(f'avg = {avg}')
            # print('----')
            heapq.heappush(result, (avg, p))

    a, idx = heapq.heappop(result)
    return idx


print(solution(A))

# ClearTime = 2021/07/26 2:22 오후 - 50%
