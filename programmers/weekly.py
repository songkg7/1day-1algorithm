#
# weekly Q1
# 2021/08/04 4:32 오후

def solution(price, money, count):
    total = [0] * (count + 1)

    for i in range(1, count + 1):
        total[i] = total[i - 1] + price * i

    if money > total[count]:
        return 0
    else:
        return total[count] - money
