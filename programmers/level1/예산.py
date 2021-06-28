#
#
# 2021/06/28 5:20 오후

def solution(d, budget):
    d = sorted(d)
    count = 0

    for i in d:
        if budget - i >= 0:
            budget -= i
            count += 1
        else:
            break
    return count
