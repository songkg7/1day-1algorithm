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
mode = []
for i in numbers:
    value = (numbers.count(i), i)
    if value not in mode:
        mode.append(value)

mode = sorted(mode, reverse=True)
if len(mode) == 1:
    print(mode[0][1])
elif mode[0][0] > mode[1][0]:
    print(mode[0][1])
else:
    mode = sorted(mode, key=lambda x: x[1])
    print(mode[1][1])

# 범위 : N의 수들 중 최댓값과 최솟값의 차이
print(abs(numbers[0]) + numbers[-1] if len(numbers) > 1 else 0)

# test = sorted(candidates, key=lambda x: candidates.count(x))
# print(test)
