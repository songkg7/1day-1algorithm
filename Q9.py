# 로프
# 탐욕법
# 백준 2217번

N = int(input())
limit = [int(input()) for _ in range(N)]

index = 0
nextIdx = 0
weights = [] # 병렬로 연결된 로프들이 견딜 수 있는 무게가 저장
while index != N:
    # print(f'index = {index}')
    for i in range(nextIdx, len(limit)):
        rope = [] # 선택한 로프를 담을 배열, index가 증가하고 다시 들어올 때 초기화
        for j in range(nextIdx, i + 1):
            # print(f'limit[j] = {limit[j]}')
            rope.append(limit[j])
        
        rope.sort()
        result = rope[0] * len(rope) # 병렬로 견딜 수 있는 무게
        weights.append(result) # 최대 무게를 구하기 위해 배열에 담아둔다.

    nextIdx += 1
    index += 1
weights.sort()
# print(weights)
print(weights[-1])

# index = 0
# nextIdx = 0
# weights = [] # 병렬로 연결된 로프들이 견딜 수 있는 무게가 저장
# while index != N:
#     # print(f'index = {index}')
#     for i in range(nextIdx, len(limit)):
#         rope = [] # 선택한 로프를 담을 배열, index가 증가하고 다시 들어올 때 초기화
#         for j in range(i + 1):
#             # print(f'limit[j] = {limit[j]}')
#             rope.append(limit[j])
        
#         rope.sort()
#         print(rope)
#         result = rope[0] * len(rope) # 병렬로 견딜 수 있는 무게
#         weights.append(result) # 최대 무게를 구하기 위해 배열에 담아둔다.

#     nextIdx += 1

#     index += 1

# weights.sort()
# print(weights)
# print(weights[-1])

