# 전화번호 목록
# 문자열
# 2021/08/13 8:40 오후

# TODO: 다시 풀기

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for s in string:
            if s not in cur_node.child:
                cur_node.child[s] = Node(s)
            cur_node = cur_node.child[s]

        cur_node.data = string

    def search_prefix(self, string):
        cur_node = self.head

        for s in string:
            cur_node = cur_node.child[s]

        if cur_node.child:
            return False
        else:
            return True


t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    nums = []
    for _ in range(n):
        num = input()
        nums.append(num)
        trie.insert(num)

    flag = True
    nums.sort()
    for num in nums:
        if not trie.search_prefix(num):
            flag = False
            break

    print("YES" if flag else "NO")
