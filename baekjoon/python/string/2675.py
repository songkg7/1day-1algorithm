# 문자열 반복
# 문자열

T = int(input())
for _ in range(T):
    r, s = input().split()
    r = int(r)
    for i in s:
        print(f'{i*r}', end='')
    print()
