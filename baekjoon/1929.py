# 에라토스테네스의 체
# 기본수학 2

m, n = map(int, input().split())
a = [False, False] + [True] * (n - 1)
prime = []

for i in range(2, n + 1):
    if a[i]:
        prime.append(i)
        for j in range(2 * i, n + 1, i):  # range 의 3번째 인자는 값만큼 건너뛰면서 루프를 진행한다.
            a[j] = False

for num in prime:
    if num >= m:
        print(num)
