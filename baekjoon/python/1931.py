# 회의실 배정
# 탐욕법

# 회의 시간이 짧은 회의들을 최대한 많이 선택하는 것이 정답에 가까워진다.

# TODO: 다시 풀고, 정리하기

n = int(input())

time = [[0] * 2 for _ in range(n)]
for i in range(n):
    s, e = map(int, input().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]
