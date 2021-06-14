# 설탕 배달 - 탐욕법 (백준)

# 봉지는 3킬로그램과 5킬로그램 두 종류 
# 정확하게 N킬로그램을 만들 수 없다면 -1 을 출력.

# test (11) 통과하지 못함
print("입력값을 입력하세요")
n = int(input())

def solution(n) :
    count = 0

    if n % 5 == 0 :
        count = n // 5
        return count

    if n % 5 != 0 :
        if (n % 5) % 3 == 0:
            count = (n % 5) + (n % 5)//3
            return count

    if n % 5 != 0 and n % 3 == 0 :
        count = n // 3
        return count

    count = -1
    return count

print(solution(n))
