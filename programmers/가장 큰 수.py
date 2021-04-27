# 정렬
# level 2

numbers = [3, 30, 34, 5, 9]


# numbers = [6, 10, 2]
# result = "6210"

# TODO: lambda 에 대한 충분한 이해가 필요
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(num)))


print(solution(numbers))
