# 2020 카카오 인턴십
# level 1

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "left"


# result = "LRLLLRLLRRL"

# 1,4,7 을 입력할 때는 왼손
# 3,6,9 를 입력할 때는 오른손
# 2,5,8,0 을 입력할 때는 가까운 손가락, 거리가 같다면 hand 의 방향


def solution(numbers, hand):
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    result = ""
    cur_lh = '*'
    cur_rh = '#'

    for num in numbers:
        if num in [1, 4, 7]:
            # print("L")
            result += "L"
            cur_lh = num
        elif num in [3, 6, 9]:
            result += "R"
            cur_rh = num
        else:
            curPos = key_dict[num]
            lPos = key_dict[cur_lh]
            rPos = key_dict[cur_rh]
            lDist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
            rDist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])

            if lDist > rDist:
                cur_rh = num
                result += "R"
            elif lDist < rDist:
                cur_lh = num
                result += "L"
            else:
                if hand == 'right':
                    cur_rh = num
                    result += "R"
                else:
                    cur_lh = num
                    result += "L"
    return result


print(solution(numbers, hand))
