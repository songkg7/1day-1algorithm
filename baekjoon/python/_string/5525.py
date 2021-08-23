# TITLE: IOIOI
# CATEGORY: 문자열
# DATE: 2021/08/23 7:55 오후

# 찾으면 인덱스를 2 만큼 이동 -1 나올 때까지

N = int(input())
M = int(input())
S = input()

P = 'I' + 'OI' * N  # N = 1

count = 0

idx = 0
while True:
    find = S.find(P, idx)
    if find > 0:
        idx = find + 2
        count += 1
    else:
        break

print(count)

# ClearTime = 2021/08/23 8:17 오후 - 50%
