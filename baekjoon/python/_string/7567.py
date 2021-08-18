# TITLE: 그릇
# CATEGORY: 문자열
# DATE: 2021/08/18 4:24 오후

# stack, 마지막에 들어있는 괄호와 같다면 +5 다르다면 + 10 ❌
# 생각해보니 굳이 배열을 조작할 필요가 없다. 인덱스를 움직이면서 계산하자

dish = input()
height = 10
for i in range(1, len(dish)):
    if dish[i - 1] == dish[i]:
        height += 5
    else:
        height += 10

print(height)

# ClearTime = 2021/08/18 4:31 오후
