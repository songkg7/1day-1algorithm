# TITLE: 부스터
# CATEGORY: 카카오 코드 페스티벌 2018 예선
# DATE: 2021/08/19 3:51 오후

# TODO: 다시 도전

N, Q = map(int, input().split())


def is_move(a, b, hp):
    is_charged = True

    # 현재 남은 체력이 있는지? -> 없다면 부스터만으로 움직여야 한다
    if hp == 0:
        # 직선거리에 체크포인트가 존재하는지? -> 있다면 '가까운' 해당 체크포인트로 이동, 없다면 이동불가
        px = list(zip(*check_point.values()))[0]
        py = list(zip(*check_point.values()))[1]

        # if a in px or b in py:


# 체크포인트의 좌표
check_point = {}
for i in range(1, N + 1):
    x, y = map(int, input().split())
    check_point[i] = check_point.get(i, ()) + (x, y)

for _ in range(Q):
    A, B, HP = map(int, input().split())
    is_move(A, B, HP)
