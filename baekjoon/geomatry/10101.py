# TITLE: 삼각형 외우기
# CATEGORY: 기하학
# DATE: 2021/10/01 7:43 오후

scale = []
for _ in range(3):
    scale.append(int(input()))

if sum(scale) != 180:
    print("Error")
else:
    if len(set(scale)) == 3:
        print("Scalene")
    elif len(set(scale)) == 2:
        print("Isosceles")
    else:
        print("Equilateral")

# ClearTime = 2021/10/01 7:51 오후
