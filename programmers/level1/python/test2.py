import collections

_str = "abcdefg"

que_list = collections.deque(_str)

que_list.rotate(2)

print(list(que_list))

