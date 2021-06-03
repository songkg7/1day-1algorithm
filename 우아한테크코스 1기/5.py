# 369 game
# 우아한 테크코스 1기
# 2021/06/03 9:56 오후

# 30, 13, 99, ...

number = int(input())


def clap(N):
    count = 0
    for i in range(1, N + 1):
        nums = str(i)
        for num in nums:
            if int(num) in [3, 6, 9]:
                count += 1
    return count


print(clap(number))

# ClearTime = 2021/06/03 10:06 오후
