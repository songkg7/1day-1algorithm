# 2018 kakao blind recruitment
# level 2

import math

str1 = 'FRANCE'
# str1 = 'handshake'
# str1 = 'aa1+aa2'
str2 = 'french'
# str2 = 'shake hands'
# str2 = 'AAAA12'


# answer = 16384

def solution(str1, str2):
    list1 = encode_list(str1)
    list2 = encode_list(str2)

    inter_list = []

    for s in list2:
        if s in list1:
            inter_list.append(s)
            list1.remove(s)

    # print(inter_list)

    join_list = list1 + list2

    # print(join_list)

    if len(list1) == 0 and len(list2) == 0:
        return 65536

    answer = math.floor(len(inter_list) / len(join_list) * 65536)
    return answer


def encode_list(string):
    str_list = []
    for s in zip(string[:-1], string[1:]):
        x = ''.join(s).lower()
        if x.isalpha():
            str_list.append(x)
    return str_list


print(solution(str1, str2))
