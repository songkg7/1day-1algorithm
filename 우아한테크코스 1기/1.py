# 출금
# 우아한 테크코스 1기
# 2021/06/03 10:19 오후

money = int(input())
answer = [0] * 9
monetary = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]

for idx, won in enumerate(monetary):
    if money >= won:
        answer[idx] = money // won
        money %= won

print(answer)

# ClearTime = 2021/06/03 10:30 오후
