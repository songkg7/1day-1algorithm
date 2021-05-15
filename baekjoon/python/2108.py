# 통계학
# 정렬

# 산술평균, 중앙값, 최빈값. 범위 구하기

N = int(input())

numbers = sorted([int(input()) for _ in range(N)])

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
average = round(sum(numbers) / N)
print(average)

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
median = numbers[round(N / 2)]
print(median)

# 최빈값(mode) ; N개의 수들 중 가장 많이 나타나는 값
modes = sorted(numbers, key=lambda x: numbers.count(x), reverse=True)
if len(modes) == 1:
    print(modes[0])
else:
    for mode in modes:
        if mode > modes[0]:
            print(mode)
            break

# 범위 : N의 수들 중 최댓값과 최솟값의 차이
print(abs(numbers[0]) + numbers[-1] if len(numbers) > 1 else 0)
