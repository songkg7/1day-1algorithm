# 평균
# 1차원 배열

N = int(input())
grade = list(map(int, input().split()))

M = max(grade)
new_grade = map(lambda x: x / M * 100, grade)

avg = sum(new_grade) / N
print(avg)
