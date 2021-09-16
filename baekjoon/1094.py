# TITLE: 막대기
# CATEGORY: 수학
# DATE: 2021/09/16 10:02 오후

x = int(input())

sticks = [64]
answer = 0
count = 0
while answer < x != 64:
    half_stick = sticks.pop()
    half_stick //= 2
    if half_stick >= x:
        sticks.append(half_stick)
    else:
        sticks.append(half_stick)
        sticks.append(half_stick)
    if answer + half_stick <= x:
        answer += half_stick
        count += 1

if x == 64:
    print(1)
else:
    print(count)

# ClearTime = 2021/09/16 10:42 오후

# NOTE: 다른 풀이
# print(bin(int(input())).count("1"))
