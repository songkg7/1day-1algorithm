# 덩치
# brute force

# 키와 몸무게를 각각 비교해서 둘 중에 순위가 높은 쪽이 등수

# 전원의 사이즈가 입력되면,
# 앞에서부터 하나씩 꺼내서 나머지 인원들의 사이즈와 비교한다.
# rank = 1 로 초기화
# 키와 몸무게가 가장 크다면 rank 를 출력, rank += 1

# 결과가 담긴 배열 result 를 출력

N = int(input())

size = []
for _ in range(N):
    size.append(tuple(map(int, input().split())))

for i in size:
    rank = 1
    for j in size:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end=' ')
