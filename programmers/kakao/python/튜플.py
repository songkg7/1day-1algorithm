# 2019 카카오 개발자 겨울 인턴십

def solution(s):
    s = s[2:-2].split('},{')

    set_list = []
    for i in s:
        arr = set(map(int, i.split(',')))
        set_list.append(arr)

    # print(sorted(set_list))
    set_list = sorted(set_list)

    answer = [list(set_list[0])[0]]
    for i in range(1, len(set_list)):
        x = set_list[i] - set_list[i - 1]
        answer.append(list(x)[0])

    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# result = [2, 1, 3, 4]


print(solution(s))
