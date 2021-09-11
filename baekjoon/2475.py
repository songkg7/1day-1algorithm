# TITLE: 검증수
# CATEGORY: 수학
# DATE: 2021/09/11 10:07 오후

nums = map(int, input().split())
result = sum(map(lambda x: x ** 2, nums)) % 10

print(result)

# ClearTime = 2021/09/11 10:09 오후
