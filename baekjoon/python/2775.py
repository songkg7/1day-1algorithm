# 부녀회장이 될테야

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # k층의 n호의 인원수는 k-1층의 n호와 k층의 n-1호의 인원수를 합한 것과 같다.
    # 문제에서 각 14층 14호까지의 제한이 있으므로 그냥 표를 채워버리고 뽑는 것이 나을 듯 하다.

    floor = [[0 for j in range(14)] for i in range(15)]
    for i in range(15):
        floor[i][0] = 1
    for h in range(14):
        floor[0][h] = h + 1
    for i in range(1, 15):
        for j in range(1, 14):
            floor[i][j] = floor[i][j - 1] + floor[i - 1][j]

    print(floor)

    print(floor[k][n - 1])


# print(k)
# print(v)

#
# people = [i for i in range(1, n + 1)]
# print(people)
#
# # 1층일 때
# first_floor = [sum(people[:i]) for i in people]
# print(first_floor)
#
# # 2층일때
# second_floor = [sum(first_floor[:i]) for i in range(1, len(first_floor) + 1)]
# print(second_floor)
#
# # 3층일때
# third_floor = [sum(second_floor[:i]) for i in range(1, len(second_floor) + 1)]
# print(third_floor)


