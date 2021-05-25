# AC
# queue
# 2021/05/25 1:02 오후

# TODO: 정리하기

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    nums = input()[1:-1].split(',')

    # 뒤집는 과정 1차 필터링
    p = p.replace('RR', '')

    front, back, rev = 0, 0, 0
    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if rev % 2 == 0:
                front += 1
            else:
                back += 1

    if front <= n - back:
        nums = nums[front:n - back]
        if rev % 2 != 0:
            print('[' + ','.join(nums[::-1]) + ']')
        else:
            print('[' + ','.join(nums) + ']')
    else:
        print("error")

# ClearTime = 2:25 오후
