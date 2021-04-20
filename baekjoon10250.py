# ACM 호텔

# T 는 테스트 케이스의 수
# H = 호텔의 층 수, W = 각 층의 방 수, N 번째 손님

# N을 H로 나눈 나머지가 배정된 방의 층 수 => 나머지가 0이라면?
# N을 H로 나눈 몫 + 1 이 배정된 방의 뒷자리 번호

# T = 2
# H, W, N = 30, 50, 72

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split(" "))

    X = N % H
    Y = N // H + 1

    if X == 0:
        X = H
        Y = N // H

    print(f'{X * 100 + Y}')
