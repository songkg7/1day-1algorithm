# 거스름돈
# 탐욕법
# 백준 5585번
# Clear

n = int(input()) # 물건의 가격 = 타로가 지불할 돈

coin = [500, 100, 50, 10, 5, 1]
change = 1000 - n

count = 0
i = 0
while change != 0:
    if change >= coin[i]:
        count += change // coin[i]
        change %= coin[i]
        i += 1
    else:
        i += 1

print(count)
