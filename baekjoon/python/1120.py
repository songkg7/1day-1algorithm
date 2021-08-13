# 문자열
# 문자열
# 2021/08/13 8:19 오후

# TODO: 다시 풀기

A, B = input().split()

answer = []
for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count += 1
    answer.append(count)

print(min(answer))
