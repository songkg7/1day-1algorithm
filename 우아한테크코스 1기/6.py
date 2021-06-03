# 콘서트 티켓팅
# 우아한 테크코스 1기
# 2021/06/03 11:35 오후

# 시간을 초단위로 바꾼 다음 60초 이상 접속을 유지했는지 체크한다.
# 먼저 접속한 유저가 떠나지 않았다면, 다른 유저가 요청을 보내도 접속할 수 없다.

from collections import deque

totalTicket = int(input())
logs = ["woni request 09:12:29",
        "brown request 09:23:11",
        "brown leave 09:23:44",
        "jason request 09:33:51",
        "jun request 09:33:56",
        "cu request 09:34:02"]

stack = deque()
for log in logs:

    if totalTicket == 0:
        break

    user_id, action, time = log.split()
    t = list(map(int, time.split(':')))
    second = sum([t[0] * 3600, t[1] * 60, t[2]])

    if action == "request":
        if not stack or second - stack[-1][-1] > 60:
            stack.append([user_id, action, second])
            totalTicket -= 1
    elif action == "leave":
        stack.pop()
        totalTicket += 1

stack = sorted(stack, key=lambda x: x[0])
result = [i[0] for i in stack]

print(result)

# ClearTime = 2021/06/04 12:17 오전
