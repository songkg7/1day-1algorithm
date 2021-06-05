# 윤년
# if
# 2021/06/06 7:56 오전

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)

# 아래 코드로도 가능
# print(1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0)

# ClearTime = 2021/06/06 8:01 오전
