#
# 2018 kakao blind recruitment
# 2021/07/14 3:10 오후

# # 이 붙은 음은 소문자로 처리해보자

melody = "CC#BCC#BCC#BCC#B"
music_infos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]


def convert(string):
    pitch = {
        "C#": "c",
        "D#": "d",
        "F#": "f",
        "G#": "g",
        "A#": "a",
    }
    for i in pitch.keys():
        find = string.find(i)
        if find >= 0:
            string = string.replace(i, pitch[i])
    return string


def solution(m, musicinfos):
    result = ()

    m = convert(m)

    for info in musicinfos:
        start, end, title, sheet = info.split(",")
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))

        # 시간 변환
        timer = 60 * (end_h - start_h) + (end_m - start_m)

        sheet = convert(sheet)

        sheet = (sheet * timer)[:timer]

        if m in sheet:
            if not result or timer > result[1]:
                result = (title, timer)

    if not result:
        return "(None)"

    return result[0]


print(solution(melody, music_infos))

# ClearTime = 2021/07/14 5:24 오후
