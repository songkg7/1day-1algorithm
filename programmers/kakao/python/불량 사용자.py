# 2019 카카오 겨울 인턴십

from itertools import permutations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned_id = ["fr*d*", "abc1**"]


# count = 0
# for user in user_id:
#     for banned in banned_id:
#         if len(user) == len(banned):
#             for i in range(len(banned)):
#                 if user[i] != banned[i] and banned[i] != '*':
#                     print(f'{user}는 {banned}와 일치하지 않습니다.')
#                     count += 1
#                     break
#
#                 print(f'{user}는 {banned}와 일치합니다.')
#
#
# print(count)

def isMatchId(ban_id, user_id):
    for i in range(len(ban_id)):
        if ban_id[i] == '*':
            continue
        elif ban_id[i] != user_id[i]:
            return False
    return True


def check(banned_ids, candidate_user):
    for i in range(len(banned_ids)):
        if len(banned_ids[i]) != len(candidate_user[i]):
            return False
        if isMatchId(banned_ids[i], candidate_user[i]) is False:
            return False
    return True


def solution(user_id, banned_id):
    ans = []

    for candidates in permutations(user_id, len(banned_id)):
        if check(banned_id, candidates) is True:
            candidates = set(candidates)
            # print(candidates)
            if candidates not in ans:
                ans.append(candidates)
    return len(ans)


print(solution(user_id, banned_id))
