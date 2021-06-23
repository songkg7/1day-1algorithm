# 회의실 배정
# Greedy
# 2021/06/23 1:00 오후

# 회의 시간이 짧은 회의들을 최대한 많이 선택하는 것이 정답에 가까워진다.

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

times.sort(key=lambda x: (x[1], x[0]))

count = 1
end = times[0][1]
for i in range(1, N):
    if times[i][0] >= end:
        count += 1
        end = times[i][1]

print(count)

# ClearTime = 2021/06/23 1:15 오후
