# 2019 kakao blind recruitment
# level 2

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


# 처음 방에 들어왔을 때 dictionary 형태로 아이디와 닉네임을 저장한다.
# 누군가 들어왔을 때 아이디값이 dict 에 키값으로 존재한다면 닉네임의 수정사항을 반영한다.

# 문자열은 공백으로 끊어서 처리한다.

def solution(record):
    cur_user = dict()
    result = []

    record = [i.split() for i in record]
    # print(record)

    for user in record:
        # 유저가 떠난건지 체크, 떠났다면 dict 에서 완전 삭제
        # if user[0] == 'Leave':
        #     del cur_user[user[1]]
        #     continue

        if user[0] == 'Enter' or user[0] == 'Change':
            cur_user[user[1]] = user[2]

        # 유저가 한번이라도 접속했던 유저인지 체크
        # if user[1] in cur_user:
            # 한 번이라도 접속했던 유저라면 닉네임을 수정했는지 체크
            # if user[0] == 'Change':
            #     cur_user[user[1]] = user[2]

        # else:  # 한 번도 접속한 적이 없는 유저라면 dict 에 저장
        #     cur_user[user[1]] = user[2]

    # message 저장
    for user in record:
        if user[0] == 'Enter':
            result.append(f'{cur_user.get(user[1])}님이 들어왔습니다.')
        elif user[0] == 'Leave':
            result.append(f'{cur_user.get(user[1])}님이 나갔습니다.')

    return result

    # for user in record:
    #     if user[0] == 'Enter':
    #         result.append(f'{cur_user.get(user[1])}님이 들어왔습니다.')

    # if user_id[0] == 'Enter' and user_id[1] not in cur_user:
    #     cur_user[user_id[1]] = record[0][2]
    #     result.append(f'{cur_user.get(user_id[1])}님이 들어왔습니다.')
    # elif user_id[0] == 'Enter' and user_id[1] in cur_user:
    #
    # elif user_id[0] == 'Leave':
    #     result.append(f'{cur_user.get(user_id[1])}님이 나갔습니다.')

    # print(cur_user)
    # print(result)

    # print(record)


print(solution(record))
