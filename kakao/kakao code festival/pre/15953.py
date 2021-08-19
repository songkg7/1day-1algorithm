# TITLE: 상금 헌터
# CATEGORY: 카카오 코드 페스티벌 예선
# DATE: 2021/08/19 2:26 오후

first_festival = {
    1: (1, 500_0000),
    2: (3, 300_0000),
    3: (6, 200_0000),
    4: (10, 50_0000),
    5: (15, 30_0000),
    6: (21, 10_0000)
}

second_festival = {
    1: (1, 512_0000),
    2: (3, 256_0000),
    3: (7, 128_0000),
    4: (15, 64_0000),
    5: (31, 32_0000)
}

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    pay = 0
    if a != 0:
        for k, v in first_festival.items():
            if v[0] >= a:
                pay += v[1]
                break

    if b != 0:
        for k, v in second_festival.items():
            if v[0] >= b:
                pay += v[1]
                break

    print(pay)

# ClearTime = 2021/08/19 2:46 오후
