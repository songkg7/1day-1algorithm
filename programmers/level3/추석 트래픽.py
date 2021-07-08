#
# 2018 kakao blind recruitment
# 2021/07/08 1:38 오후

# 1. 응답시작시간이 빠른 순서대로 deque 에 담는다.
# 2. 다음 로그가 들어올 때, deque 에 이미 있는 로그의 완료시간이 들어오는 로그의 응답시작시간보다 1초 이상 빠른지 체크
# 3. 1초 이상 빠르다면 해당 로그는 deque 에서 제거
# 4. 로그가 deque 에 입력될 때마다 count 를 체크한다. count 가 높아질 때 갱신한다.

# !: 응답완료시간을 기준으로 계산해본다.

import re
import datetime as dt


def solution(lines):
    dateformat = "%Y-%m-%d %H:%M:%S.%f"
    p = re.compile(r'(?P<datetime>\d+-\d+-\d+\s\d{2}:\d{2}:\d{2}.\d+)\s(?P<second>\d+.*\d*)s$')

    server = []

    count = 1

    while lines:
        n = lines.pop()
        next_datetime = p.match(n).group("datetime")
        next_second = p.match(n).group("second")

        # 다음 로그 table
        next_end_time = dt.datetime.strptime(next_datetime, dateformat)
        next_start_time = next_end_time - dt.timedelta(seconds=float(next_second) - 0.001)

        server.append((next_start_time, next_end_time))

    # 최대값 저장
    max_range = server[0][1]

    # 실행시작시간 기준으로 정렬
    sort_server = sorted(server, key=lambda x: x[0])

    for i in range(len(sort_server)):
        for j in range(2):
            start_range = sort_server[i][j]

            if start_range < max_range:
                end_range = start_range + dt.timedelta(seconds=0.999)

                target_log = list(filter(lambda x: start_range <= x[1] and end_range >= x[0], sort_server))

                if count < len(target_log):
                    count = len(target_log)

    return count

# ClearTime = 2021/07/08 4:13 오후
