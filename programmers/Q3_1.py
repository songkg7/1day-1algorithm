people = [70, 80, 50]
limit = 100

def solution(people, limit):
    count = 0
    while len(people) > 0 :
        maxWeight = max(people)
        minWeight = min(people)

        if len(people) == 1 :
            count += 1
            people.remove(maxWeight)
            break

        if maxWeight + minWeight > limit:
            count += 1
            people.remove(maxWeight)
        else:
            count += 1
            people.remove(maxWeight)
            people.remove(minWeight)

    return count

print(solution(people, limit))