# 캠핑
# 탐욕법
# 백준 4796번
# Clear

# 연속하는 P일 중 L일동안만 사용할 수 있다. 이제막 V일짜리 휴가를 시작했다.
# 최대 캠핑장을 이용할 수 있는 날짜를 구해라.
# L, P, V 를 순서대로 입력받는다
# 1 < L < P < V

# 풀이법
# 20일의 휴가 중 연속하는 8일 중 5일동안만 캠핑장을 사용할 수 있다고 할 때,
# 16일 중 10일동안만 캠핑장을 사용할 수 있게되며,
# 남은 4일은 모두 캠핑장을 사용할 수 있다.
# 이걸 식으로 표현하면 다음과 같다.
# result = (V // P) * L + (V % P) .

# Test ======================
# L, P, V = 2, 3, 9
# result = 14
# print((V // P) * L + (V % P))
# ===========================

i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 :
        break
    else:
        rest = min(V % P, L)
        result = (V // P) * L + rest
        print(f'Case {i}: {result}')
        i += 1

# cases = []
# while True:
#     case = list(map(int, input().split()))
#     if case[0] == 0:
#         break
#     cases.append(case)

# i = 1
# for case in cases:
#     L, P, V = case[0], case[1], case[2]

#     if V % P > L :
#         rest = L
#     else :
#         rest = V % P

#     result = (V // P) * L + rest
#     print(f'Case {i}: {result}')
#     i += 1

# print(case)




# print(V // P)
# print(V % P)
