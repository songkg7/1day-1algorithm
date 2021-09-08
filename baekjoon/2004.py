# 조합 0의 개수
# 정수론 및 조합론

# 정수의 범위가 '20억' 으로, 매우 큰 수가 들어오게 되면 팩토리얼 함수를 실행하는 순간 시간초과가 될 것이다.
# 다른 해결법을 찾아야한다.

N, M = map(int, input().split())


def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


print(count_number(N, 5))
print(count_number(M, 5))

print(min(count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5),
          count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)))
