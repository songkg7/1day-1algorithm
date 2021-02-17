def solution(people, limit) :
    people.sort()
    cnt = 0
    minIndex = 0
    maxIndex = len(people)-1
    while minIndex <= maxIndex :
        cnt += 1 # 일단 배의 숫자는 늘리고
        if people[maxIndex] + people[minIndex] <= limit :
            minIndex += 1 # 무게 제한을 초과하지 않을 경우 다음 가벼운 사람을 태운다
        maxIndex -= 1 # 무거운 사람은 항상 탄다
    return cnt