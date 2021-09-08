# 나이순 정렬
# 정렬

N = int(input())

members = sorted([input().split() + [str(i)] for i in range(N)], key=lambda x: (int(x[0]), int(x[2])))

for member in members:
    print(f'{member[0]} {member[1]}')
