# 회의실 배정
# 탐욕법
# 백준 1931번

n = int(input())

conferences = [] # 회의들
count = 0 # 최대갯수

for _ in range(n):
    conferences.append(list(map(int, input().split())))

print(n)
print(conferences)

