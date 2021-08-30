# TITLE: 평균 점수
# CATEGORY: math
# DATE: 2021/08/30 7:03 오후

def up_score(n):
    if n < 40:
        return 40
    return n


score = [int(input()) for _ in range(5)]
score = map(up_score, score)

print(int(sum(score) / 5))

# ClearTime = 2021/08/30 7:11 오후
