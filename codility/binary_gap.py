# binary gap
# lesson 1
# 2021/06/10 7:42 오후

# 스택, 0 이나오면 스택에 쌓아가다가 다른 숫자가 나왔을 때 0의 개수를 다른 배열에 저장하고 스택을 초기화한다.

N = 32


def solution(N):
    s = str(bin(N))[3:]
    stack = []
    count = [0]
    for i in s:
        if int(i) == 0:
            stack.append(i)
        else:
            count.append(len(stack))
            stack = []

    return max(count)


print(solution(N))

# ClearTime = 2021/06/10 7:55 오후
