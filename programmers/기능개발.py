# 스택 / 큐
# level 2
from collections import deque

progresses = [93, 30, 55]
# progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 30, 5]
# speeds = [1, 1, 1, 1, 1, 1]


# return = [2,1]

# 각 배포마다 몇개의 기능이 배포되는지 => 몇개의 기능이 deque 되는지?

def solution(progresses, speeds):
    # deque_list = deque(progresses)
    # y = deque_list.popleft()
    # print(y)
    # print(deque_list)

    # 배포되는 날짜를 배열에다가 저장
    # 배열에 있는 같은 숫자들의 카운트를 새로 저장

    progress_que = deque(progresses)
    speeds_que = deque(speeds)
    answer = []
    days = []
    day_count = 1
    # for i in range(len(progresses)):
    #     while progresses[i] + (speeds[i] * day_count) < 100:
    #         day_count += 1
    #     days.append(day_count)

    while len(progress_que) > 0:
        x = progress_que.popleft()
        y = speeds_que.popleft()
        while x + (y * day_count) < 100:
            day_count += 1
        days.append(day_count)

    # print(days)
    # print(days.count(10))

    for i in days:
        answer.append(days.count(i))
        days.remove(i)

    return answer


print(solution(progresses, speeds))
