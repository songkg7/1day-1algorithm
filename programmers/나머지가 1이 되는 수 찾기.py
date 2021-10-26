# TITLE:
# CATEGORY:
# DATE: 2021/10/26 9:09 오후

n = int(input())

answer = 0
for i in range(2, n):
    if (n - 1) % i == 0:
        answer = i
        break

print(answer)
