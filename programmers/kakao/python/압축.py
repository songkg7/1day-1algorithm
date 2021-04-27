# 2018 kakao blind recruitment
# level 2

import string

msg = 'KAKAO'


# answer = [11, 1, 27, 15]

# msg = 'TOBEORNOTTOBEORTOBEORNOT'


# answer = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]


def solution(msg):
    answer = []

    # init, 사전 생성
    alpha = string.ascii_uppercase
    alpha_dict = {}
    for idx in range(len(alpha)):
        alpha_dict[idx + 1] = alpha[idx]

    print(alpha_dict)

    # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
    while len(msg) > 0:
        w = ''
        for i in range(len(msg) + 1):
            if msg[:i] in alpha_dict.values():
                w = msg[:i]

        idx = get_idx(alpha_dict, w)

        msg = msg.replace(w, '', 1)

        if len(msg) != 0:
            c = msg[0]
            new_idx = get_last_idx(alpha_dict) + 1
            alpha_dict[new_idx] = w + c

        answer.append(idx)

    return answer


def get_idx(dictionary, alpha):
    return list(dictionary.values()).index(alpha) + 1


def get_last_idx(dictionary):
    return list(dictionary.keys())[-1]


print(solution(msg))
