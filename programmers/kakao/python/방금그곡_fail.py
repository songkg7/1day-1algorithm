# 2018 kakao blind recruitment
# level 2

# FIXME: 처음부터 #음들을 치환하여 해결했어야하는데 방향을 잘못 잡았다
# - 비효율적인 반복문도 포함되어 있으니 다시 풀어보자


import re

# m = "CC#BCC#BCC#BCC#B"
# musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]


def solution(m, musicinfos):
    answer = dict()

    for i in musicinfos:
        i = i.split(',')
        start_time = i[0]
        end_time = i[1]
        title = i[2]
        score = i[3]
        # print(start_time, end_time, title, score)

        # 음을 숫자로 치환
        score.replace()

        play_time = cal_time(start_time, end_time)
        play_song = play_score(play_time, score)

        regex = re.findall(m, play_song)
        if regex:
            answer[title] = play_time

        print(f'play_song = {play_song}')

    result = list(answer.items())[0][0]
    return result


def play_score(play_time, score):
    play_song = ''
    while play_time > 0:
        for melody in score:
            if play_time == 0:
                break
            play_song += melody
            if melody != '#':
                play_time -= 1
    return play_song


def cal_time(start, end):
    s = list(map(int, start.split(':')))
    e = list(map(int, end.split(':')))

    play_time = (e[0] * 60 + e[1]) - (s[0] * 60 + s[1])
    return play_time


print(solution(m, musicinfos))
