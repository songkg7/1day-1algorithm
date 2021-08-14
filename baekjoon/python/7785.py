# 회사에 있는 사람
# 문자열
# 2021/08/14 12:16 오전

# 현재 상태가 enter 인 사람만 사전의 역순으로 출력하기

def main():
    n = int(input())
    company = dict()
    for _ in range(n):
        name, status = input().split()

        company[name] = status

    answer = list(filter(lambda x: x[1] == 'enter', company.items()))
    for p, s in sorted(answer, reverse=True):
        print(p)


if __name__ == '__main__':
    main()

# ClearTime = 2021/08/14 12:27 오전
