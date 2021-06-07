# 수 묶기
# 탐욕법
# 백준 1744번

# 풀이 과정
# 수열을 배열에 담아 내림차순으로 정렬한 뒤
# 앞에서부터 두개의 숫자를 묶어서 곱한다. 결과를 answer에 더해간다.
# 만약 두 수를 곱한 뒤 나온 값이 음수거나 0 이라면 곱하지 않고 더한다.
# 배열이 계산을 해갈 때 0이 되는 구간이 중요한데, 음수끼리 곱하면 양수가 되므로
# 그 부분을 적절히 잘 계산해줘야한다.
import sys

# N = [5, 4, 3, 2, 1, 0, -1, -2, -3]
arr = [-1, 2, 1, 3]

arr.sort(reverse=True)
# print(N)

# 1번 풀이
# N = int(input())
# arr = sorted([int(sys.stdin.readline().strip()) for _ in range(N)], reverse=True)

answer = 0
i = 0
for _ in range(len(arr)):
    if i == len(arr):
        break
    else:
        if i + 1 == len(arr):
            answer += arr[i]
            break
        # if i == len(arr):
        #     break
        cur = arr[i]
        next = arr[i+1]
        if cur * next > 0:
            answer += cur * next
            i += 2
        else:
            answer += cur
            i += 1

print(answer)