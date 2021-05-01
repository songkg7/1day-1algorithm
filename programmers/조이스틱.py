# 탐욕법
# level 2

# 오른쪽으로 이동하며 바꿀 때와 왼쪽으로 이동하며 이름을 바꿀 때

name = "JEROEN"


# return = 56

def solution(name):
    make_name = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    answer = 0
    idx = 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0:
            break
        left, right = 1, 1

        # 왼쪽으로 이동, A를 만날때까지
        while make_name[idx - left] == 0:
            left += 1

        # A 를 만날때까지 오른쪽으로 이동
        while make_name[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right
    return answer


print(solution(name))
