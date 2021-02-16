# 주식 가격

price = [1, 2, 3, 2, 3]

# return = [4, 3, 1, 1, 0]

# NOTE: 문제풀이
# 반복문을 돌면서 각각의 인덱스의 값을 서로 비교한다.
# 한 번이라도 작은 값이 나온다면 반복을 멈춘후 인덱스값의 차이를 배열에 담는다
# 차이값이 담긴 배열을 리턴해준다.

# 맨 처음 pop 한 값을 저장해 놓은 후, 연속적으로 pop하면서 초기값보다 작은 값이 나온다면
# pop된 갯수를 구한다. 마지막 값의 경우 배열에 남은 값이 없으므로 0 을 리턴

def solution(price):
    answer = []
    for i in range(len(price)):
        print(i)
        answer.append(0) # 기본값 세팅
        for j in price[i + 1:]:
            if price[i] <= j:
                answer[i] += 1
            else:
                answer[i] = 1
                break;

            # if price[i] < j:
            #     time += 1
            #     answer.append(time)
            #     break
            # else:
            #     time += 1

    print(answer)

solution(price)