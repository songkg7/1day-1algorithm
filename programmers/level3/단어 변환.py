#
# DFS & BFS
# 2021/06/25 1:37 오후

# 한 번에 한 개의 알파벳만 바꿀 수 있다.
# words 에 있는 단어로만 바꿀 수 있다.
# words 에 target 이 없다면 0을 return

# begin 과 한글자만 다른 단어를 찾아서 다음 목적지로 넣는다.
# 목적지에서 하나씩 꺼낼 때마다 방문한 것으로 보고, count 를 증가시킨다.

from collections import deque

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log"]


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = []

    while queue:
        n, count = queue.popleft()

        # queue 에서 target 이 등장한다면 저장된 count 를 return
        if n == target:
            return count

        visited.append(n)

        # 다른 부분 검사 후 목적지 추가
        for w in words:
            diff = 0
            for i in range(len(w)):  # 뮨제의 제한 조건: 모든 단어의 길이는 같다.
                if n[i] != w[i]:
                    diff += 1
            if diff == 1 and w not in visited:  # 다른 단어가 하나뿐이고 방문한 적이 없다면, 목적지에 설정, 전 노드의 카운트 + 1
                queue.append((w, count + 1))


print(solution(begin, target, words))

# ClearTime = 2021/06/25 2:15 오후
