import sys

# arr = [-1, 2, 1, 3]
numbers = [-1, 2, 1, 3]

positive = [] # positive number, 양수
negative = [] # negative number, 음수

result = 0

for num in numbers:
    if num > 1:
        positive.append(num)
    elif num <= 0: # 0은 음수와 곱하면 결과가 최댓값이 된다.
        negative.append(num)
    else: # 1만 통과, 1은 무조건 더한다.
        result += num

positive.sort(reverse=True) #양수는 큰 수끼리 곱하고
negative.sort() # 음수는 작은 수끼리 곱한다.

# TODO: 두 수씩 묶어서 더하는 과정을 추가해야한다.
i = 0
for _ in positive:
    # if i >= len(positive) - 1:
    #     break
    result += positive[i] * positive[i+1]
    i += 2

j = 0
for _ in negative:
    # if j >= len(negative) - 1:
    #     break
    result += negative[j] * negative[j+1]
    j += 2

print(positive)
print(negative)
print(result)
    # 0, 1이 존재하는지 체크 후 있다면 결과값에 더하고 없으면 넘어간다.