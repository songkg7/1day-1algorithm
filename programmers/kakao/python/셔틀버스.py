# 2018 kakao blind recruitment

import re
from collections import deque

# n, t, m = 1, 1, 5
n, t, m = 2, 10, 2
# n, t, m = 10, 60, 45
# timetable = ["08:00", "08:01", "08:02", "08:03"]
timetable = ["09:10", "09:09", "08:00"]


# timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
#              "23:59", "23:59", "23:59", "23:59"]


# answer = "09:00"

def solution(n, t, m, timetable):
    # 시간을 분단위로 변경
    con_waiting_time = 0
    waiting = []
    regex = re.compile('\D')
    for time in timetable:
        hour_min = regex.split(time)
        waiting.append(int(hour_min[0]) * 60 + int(hour_min[1]))

    waiting = sorted(waiting)  # 온 순서대로 세우기

    start_time = 540

    # 셔틀 운행 횟수만큼 반복
    # 만약 마지막 셔틀에 자리가 남는다면 콘은 그 셔틀의 도착시간에 대기열에 들어가면 된다.
    # 자리가 남지 않는다면
    # => 마지막에 줄을 서는 사람보다 1분만 빨리오게 하면 된다.
    for driving in range(n):
        # bus 최대 인원 설정
        bus = deque(maxlen=m)
        for _ in range(m):
            if not waiting:
                break
            if waiting[0] <= start_time:
                passenger_crew = waiting.pop(0)
                bus.append(passenger_crew)

        start_time += t
        print(bus)
        print(start_time)

    # 마지막 버스 남는 자리 체크 후 꽉 차있으면 콘의 도착 시간 설정
    if len(bus) == m:
        con_waiting_time = bus.pop() - 1
    else:  # 꽉 차있지 않으면 버스의 마지막 도착시간을 콘의 시간으로 설정
        con_waiting_time = start_time - t

    # formatting
    hour = con_waiting_time // 60
    minute = con_waiting_time % 60
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    answer = hour + ':' + minute

    return answer


# temp = [time.split(':') for time in timetable]

# 분단위 시간에서 -1 하면 콘이 도착해야하는 시간
# 버스는 9시부터 온다. (540분)


print(solution(n, t, m, timetable))
