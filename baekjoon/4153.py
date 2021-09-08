# 직각삼각형
# 기본수학 2

# 직각삼각형은 가장 긴 변의 길이의 제곱이 나머지 변의 길이 제곱을 합한 것과 같다.


while True:
    length = list(map(int, input().split()))
    if sum(length) == 0:
        break

    length = sorted(length)
    a = length[0]
    b = length[1]
    c = length[2]

    print("right") if c ** 2 == (a ** 2) + (b ** 2) else print("wrong")
