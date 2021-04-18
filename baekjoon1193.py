# 분수찾기

# 1 2 3 4 5 개의 순서로 대각 방향으로 늘어난다
# 14번째 분수를 찾으려면 갯수가 10 이상 15 이하인 대각방향 중 하나이다.
# 홀짝을 이용하여 분모와 분자의 증감 방향을 정할 수 있다.

X = int(input())

totalLine = 0
temp = 0
while X > totalLine:
    temp += 1
    totalLine += temp

a = 1
b = temp
n = totalLine - X

if b % 2 != 0:
    print(f'{a + n}/{b - n}')
else:
    print(f'{b - n}/{a + n}')
