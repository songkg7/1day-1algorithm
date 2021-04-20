import sys

input = sys.stdin.readline

case = int(input())

for _ in range(case):
    h, w, n = map(int, input().split())

    room = n // h + 1
    floor = n % h
    if floor == 0:
        floor = h
        room -= 1

    print(f'{floor * 100 + room}')

