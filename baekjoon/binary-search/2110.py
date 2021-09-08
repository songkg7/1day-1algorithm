# 공유기 설치
# Binary Search
# 2021/06/21 10:32 오후

# TODO: 다시 풀기

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

# N, C = 5, 3
# house = [1, 2, 8, 4, 9]

house.sort()

start = 1
end = house[-1] - house[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid:
            count += 1
            old = house[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
