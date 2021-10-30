# 구명보트 (Greedy)

# 최대 2명씩밖에 탈 수 없고, 무게제한이 있다.
# 가벼운 사람을 고르게되면 무거운 사람을 골라야한다. (정렬?)

# 가장 가벼운 사람을 고르고 가장 무거운 사람을 합해서 limit에 걸리는지 확인
# 걸리면 가장 무거운 사람을 배열에서 제외하고 카운트 증가


# NOTE: 문제풀이
# 한 명을 선택한 후 몸무게 제한에 걸리지 않는 다른 사람을 찾는다.
# 찾는 결과가 끝나면 카운트를 하나 증가시키고 people 배열에서 제외한다
# 

people = [50, 50, 70, 80]
limit = 100

def solution(people, limit):
    count = 0
    people.sort()
    while len(people) > 0 :
        min = people[0]
        max = people[-1]

        if len(people) == 1:
            count += 1
            break

        if min + max > limit:
            del people[-1]
            count += 1
        else:
            del people[-1]
            del people[0]
            count += 1

    return count

print(solution(people, limit))