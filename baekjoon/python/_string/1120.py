# TITLE: 문자열
# CATEGORY: 문자열
# DATE: 2021/08/18 3:58 오후

# TODO: 다시 풀어보기

A, B = input().split()

m = 50
for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[j + i]:
            count += 1
    if m > count:
        m = count

print(m)

# ClearTime = 2021/08/18 4:17 오후
