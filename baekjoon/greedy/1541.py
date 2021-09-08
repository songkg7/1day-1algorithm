# 잃어버린 괄호
# 탐욕법
# 2021/06/01 2:43 오후

# TODO: 정리하기

formula = input().split('-')

# + - 계산은 순서를 뒤집어도 같다.
# 즉, - 뒤에 있는 숫자 중 가장 큰 숫자를 찾아서, 더하기를 한 후, 원래 식에다가 합해준다.

s = 0
for i in formula[0].split('+'):
    s += int(i)

for i in formula[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)

# ClearTime = 2021/06/01 3:04 오후
