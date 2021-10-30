# Clear
import sys # input보다 속도가 빠르다

T = int(input()) # 테스트의 갯수

for _ in range(T):

    N = int(input()) # 지원자의 숫자

    # 서류 점수 순위를 오름차순으로 정렬
    emp1 = sorted([list(map(int, sys.stdin.readline().strip().split()))
                for _ in range(N)],
                key = lambda x: x[0])

    cnt = 1 # 최종합격자의 인원수, 한명도 통과하지 못하는 경우는 없다
    min = emp1[0][1] # 서류 점수 1위의 면접 순위를 저장한 후 비교

    for i in range(1, N):
        if emp1[i][1] < min:
            min = emp1[i][1] # 지금까지 만난 가장 좋은 면접 순위를 저장
            cnt += 1
    
    print(cnt)
