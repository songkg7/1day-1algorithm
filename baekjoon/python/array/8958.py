# OX 퀴즈
# 1차원 배열

T = int(input())
for _ in range(T):
    point = 0
    count = 0
    result = input()
    for a in result:
        if a == 'O':
            count += 1
            point += count
        else:
            count = 0
    print(point)
