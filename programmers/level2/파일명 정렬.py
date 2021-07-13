#
# 2018 kakao blind recruitment
# 2021/07/13 6:08 오후

import re


def solution(files):
    p = re.compile(r"^(?P<head>\D+)(?P<number>\d{1,5})(?P<tail>.*)")
    return sorted(files, key=lambda x: (p.match(x).group("head").lower(), int(p.match(x).group("number"))))

# ClearTime = 2021/07/13 7:15 오후
