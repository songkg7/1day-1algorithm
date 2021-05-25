# AC
# queue
# 2021/05/25 1:02 오후

# FIXME: 시간초과

import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip()[1:-1][0::2]))

    status = True

    for f in p:
        if f == 'R':
            nums = nums[::-1]
        else:
            if nums:
                deque(nums).popleft()
            else:
                status = False
                break

    if status:
        print(str(list(nums)))
    else:
        print("error")
