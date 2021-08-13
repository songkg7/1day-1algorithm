# 30
# 문자열
# 2021/08/13 7:47 오후

# 모든 자릿수를 더했을 때 3의 배수여야하고 마지막 숫자가 0 이여야 한다.
# 오해의 소지가 있는 문제 지문

N = input()
N = sorted(N, reverse=True)
answer = 0

if '0' not in N:
    print(-1)
else:
    for i in N:
        answer += int(i)
    if answer % 3 != 0:
        print(-1)
    else:
        print(''.join(N))

# ClearTime = 2021/08/13 8:14 오후
