#
# Hash
# 2021/06/26 4:05 오후

# 장르 별로 가장 많이 재생된 노래 상위 두 곡 뽑기
# 전체 재생 정보가 저장된 딕셔너리

from collections import Counter

genres = ["classic", "pop", "classic", "classic", "pop", "jazz"]
plays = [500, 600, 150, 800, 2500, 100]


# data = {
#     0: ("classic", 500),
#     1: ("pop", 600)
# }

def solution(genres, plays):
    answer = []
    total_plays = {}
    data = {}
    for g in range(len(genres)):
        total_plays[genres[g]] = total_plays.get(genres[g], 0) + plays[g]
        data[g] = (genres[g], plays[g])

    # 많이 재생된 순서로 장르 정렬
    a = sorted(total_plays.items(), key=lambda x: -x[1])

    # 장르 내에서 많이 재생된 노래
    for g, c in a:
        # 상위 두 개까지만 가져오기
        b = sorted(filter(lambda x: x[1][0] == g, data.items()), key=lambda x: -x[1][1])[:2]
        for number, info in b:
            answer.append(number)

    return answer


print(solution(genres, plays))

# ClearTime = 2021/06/26 4:43 오후
