#
#
# 2021/06/19 2:50 오후

import re

S = "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"
C = "Example"


def solution(S, C):
    s = re.compile(r"(?P<name>\w+\s+\w+-?\s*\w*)\s+<(?P<id>\w+.\w+)(?P<count>\d?)@\w+.com>")

    names = S.split(', ')
    print(names)
    result = []
    for name in names:
        split = name.split()
        if len(split) == 3:
            name = split[0] + ' ' + split[2]

        p = re.sub(r'(\w+)\s*(\w+)', name + ' <\\1.\\2@' + C.lower() + '.com>', name.lower().replace('-', ''))

        if p in result:
            r = s.sub(lambda x: str(int(x.group("count")) + 1), p)
            print(r)

        result.append(p)

    print(result)

    for i in result:
        print(s.search(i).group("name"))
        print(s.search(i).group("id"))

    # return result


print(solution(S, C))
