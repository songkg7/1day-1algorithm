from collections import deque

prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    que_prices = deque(prices)

    while que_prices :
        price = que_prices.popleft()
        up_time = 0
        for n in que_prices :
            up_time += 1
            if price > n :
                break
        answer.append(up_time)

    return answer

print(solution(prices))