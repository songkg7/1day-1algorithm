#
#
# 2021/06/24 3:50 오후

# TODO: 다시 풀기

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


def solution(tickets):
    tickets.sort(reverse=True)
    print(tickets)
    routes = {}
    for v1, v2 in tickets:
        routes[v1] = routes.get(v1, []) + [v2]

    print(routes)

    start = ['ICN']
    answer = []

    while start:
        top = start[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[top].pop())
    answer.reverse()
    return answer


print(solution(tickets))
