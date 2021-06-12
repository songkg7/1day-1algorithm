# 프린터 큐
# queue
# 2021/05/25 11:21 오전

# TODO: 정리하기

from collections import deque

T = int(input())
for _ in range(T):
    printer = deque()
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))

    # M 번째 문서의 출력 순서를 알아내자
    # 프린터의 대기열 세팅
    for i in range(N):
        printer.append((priority[i], i))

    # 다 출력 될 때까지 루프
    count = 0
    while printer:
        doc = printer.popleft()
        if printer and doc[0] < max(printer)[0]:
            printer.append(doc)
        else:
            count += 1
            if M == doc[1]:
                print(count)
                break


