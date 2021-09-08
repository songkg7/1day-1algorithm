# TITLE: 이진수 연산
# CATEGORY: 문자열
# DATE: 2021/08/29 8:24 오후

A = int(input(), 2)
B = int(input(), 2)

mask = 2 ** 100_000 - 1

print(bin(A & B)[2:].zfill(100_000))
print(bin(A | B)[2:].zfill(100_000))
print(bin(A ^ B)[2:].zfill(100_000))
print(bin(A ^ mask)[2:].zfill(100_000))
print(bin(B ^ mask)[2:].zfill(100_000))

# TODO: 다시 풀기
