# Fly me to the Alpha Centauri
# 기본수학 1

# 총 거리 d, 현재까지 이동한 거리 m, 현재 속도 v, 공간이동 횟수 n
# 현재 속도(v) >= 남은거리(d-m)/2 라면 속도를 줄여나가야한다.
# FIXME: 시간 초과, O(n)
# x, y = 45, 50

T = int(input())

for _ in range(T):
    x, y = list(map(int, input().split(' ')))
    d = y - x
    v = 0  # 현재 속도
    m = 0  # 현재까지 이동한 거리
    n = 0  # 공간이동 횟수

    while d-m > 0:
        if v > (d-m)/2 and d-m != 1:
            # 감속
            v -= 1
            m += v
            n += 1
        elif v == (d-m)/2 or d-m == 1:
            # 속도 유지
            m += v
            n += 1
        else:
            # 가속
            v += 1
            m += v
            n += 1

    print(n)
