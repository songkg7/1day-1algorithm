# TITLE: 셀프 넘버
# CATEGORY: 수학
# DATE: 2021/09/27 9:10 오후

# 생성자가 없는 숫자 = 셀프 넘버

nums = set([i for i in range(1, 10001)])
control = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    control.add(i)

for v in sorted(nums - control):
    print(v)

# ClearTime = 2021/09/27 9:49 오후
