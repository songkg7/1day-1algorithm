# 탐욕법
# 동전 0
# 백준 11047번
# Clear

n, target = map(int, input().split())

a = []
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)

i = 0
answer = 0

while target != 0:
    if target >= a[i]: # > 로 했다가 런타임 에러가 발생. 모든 동전이 target보다 값이 크거나 같다면?
        answer += target // a[i]
        target %= a[i]
        i += 1
    else:
        i += 1

print(answer)