# 스택/큐
# level 2

# 우선순위 큐를 구현해야하는 문제
# enumerate 활용


from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    # print(queue)
    # print(max(queue)[0])
    while len(queue):
        # 맨 앞에 있는 문서 하나를 대기 목록에서 꺼냄
        item = queue.popleft()
        if queue and max(queue)[0] > item[0]:
            # 우선 순위가 더 높은 문서가 존재한다면 맨 뒤로 다시 넣음
            queue.append(item)
        else:
            # 우선순위가 더 높은 문서가 없다면 인쇄 => answer += 1
            answer += 1
            # 요청한 인쇄 문서 차례가 되면 그동안 인쇄했던 문서들의 개수를 리턴
            if item[1] == location:
                break

    return answer


# priorities = [2, 1, 3, 2]
priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
