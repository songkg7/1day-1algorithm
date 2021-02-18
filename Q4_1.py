# 설탕 배달 - 탐욕법 (백준)

# 봉지는 3킬로그램과 5킬로그램 두 종류 
# 정확하게 N킬로그램을 만들 수 없다면 -1 을 출력.

#  반복문으로 체크해보자
print("입력값을 입력하세요")
n = int(input())

def solution(n) :
    count = 0

    while n > 0 :
        if n < 3 or n == 4:
            count = -1
            break

        if n % 5 == 0:
            count += n // 5
            break
        
        elif n % 3 == 0:
            n -= 3
            count += 1
        else:
            n -= 5
            count += 1
    
    return count

print(solution(n))
# Clear