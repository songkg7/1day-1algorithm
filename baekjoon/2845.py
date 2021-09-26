# TITLE: 파티가 끝나고 난 뒤
# CATEGORY: 수학
# DATE: 2021/09/26 9:21 오후

L, P = map(int, input().split())
peoples = list(map(int, input().split()))

cal_people = L * P

result = map(lambda x: x - cal_people, peoples)
print(*result)

# ClearTime = 2021/09/26 9:37 오후
