# 평균은 넘겠지
# 1차원 배열

# TODO: 정리하기

C = int(input())
for _ in range(C):
    temp = list(map(int, input().split()))
    N = temp[0]
    grade = temp[1:]

    answer = len(list(filter(lambda x: x > sum(grade) / N, grade))) / N
    print("{:.3f}%".format(answer * 100))
