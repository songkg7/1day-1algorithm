# 더하기 사이클
# while
# 2021/06/06 9:32 오후

N = int(input())

cycle = 0

if N < 10:
    arr = [0, N]
else:
    arr = list(map(int, str(N)))

init = arr

arr = [arr[1], int(str(sum(arr))[-1])]
cycle += 1

while init != arr:
    arr = [arr[1], int(str(sum(arr))[-1])]
    cycle += 1

print(cycle)

# ClearTime = 2021/06/06 10:16 오후
