# 듣보잡
# 문자열
# 2021/08/13 6:21 오후

N, M = map(int, input().split())
A = set()
B = set()

for _ in range(N):
    name = input()
    A.add(name)

for _ in range(M):
    name = input()
    B.add(name)

result = sorted(A & B)

print(len(result))
for i in result:
    print(i)

# ClearTime = 2021/08/13 6:36 오후
