t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    count = 0  # 이동 횟수
    v = 1  # count 별 이동 가능한 거리
    m = 0  # 이동한 거리의 합
    while m < distance:
        count += 1
        m += v  # count 수에 해당하는 v를 더함
        if count % 2 == 0:  # count 가 2의 배수일 때,
            v += 1
    print(count)
