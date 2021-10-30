N = int(input())
rope = [int(input()) for _ in range(N)]

rope.sort(reverse=True) # 내림차순 정렬

# weights = []
weights = [(rope[idx] * (idx + 1)) for idx in range(N)]

# for idx in range(N):
#     weights.append(rope[idx] * (idx + 1))

print(max(weights))
