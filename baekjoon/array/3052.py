# 나머지
# 1차원 배열

numbers = [int(input()) for _ in range(10)]

print(len(set(map(lambda x: x % 42, numbers))))

