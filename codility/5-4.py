# PassingCars
# Prefix Sums
# 2021/07/27 6:43 오후

# 0을 꺼낸 인덱스보다 뒤에 있는 1의 개수 => 첫번째 페어의 수
# 두번째 0을 꺼냈을 때의 인덱스보다 뒤에 있는 1의 개수 => 두번째 페어의 수

# 효율성 개선을 위한 고민 1
# 1을 미리 카운트해놓은 숫자로 바꿔놓고 하면 어떨까?
# ex) [0, 3, 0, 2, 1]

arr = [0, 1, 0, 1, 1]


def solution(A):
    result = 0
    while 0 in A:
        A = A[A.index(0) + 1:]
        result += A.count(1)
    return result


print(solution(arr))

# ClearTime = 2021/07/27 6:59 오후 - 50%
