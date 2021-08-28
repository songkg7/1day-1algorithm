# 1day-1algorithm

하루 최소 1개 이상의 알고리즘 문제를 풀며 기록합니다.

- JavaScript, Python을 사용합니다.

#### 문제를 해결해나가는 과정 및 풀이는 다음 블로그에 업로드 됩니다.

https://songkg7.tistory.com/

## Commit Convention

커밋 메세지는 최대한 짧고 간결하게 작성한다.

- convention: Flatform < Category > TITLE - {simple message}

ex) Solve: Codility < DFS > lesson 5-2

ex) Solve: BOJ < Brute Force > 블랙잭

- Refactor: 가독성 또는 성능 개선을 위한 코드 리팩토링의 경우
- Solve: 문제를 클리어했을 경우 최초 1회
- Retry: 제대로 이해하지 못했거나, 스스로 풀지 못한 문제를 다시 도전한 경우 (Clear와 관련 없음)
- Fail: 문제를 해결하지 못했지만, 과정을 기록하기 위해 커밋하는 경우
- Docs: 주석 및 문서 수정의 경우

## 코딩테스트에 자주 쓰이는 내용 모음

## heap - 힙 ✔️

```python
import heapq  # 기본은 min-heap, max-heap 사용시 -값 넣기

lst = [1, 2, 3]
heapq.heapify(lst)
# 빈 배열은 push시 자동으로 힙으로 됨
empty = []
```

#### 💡 삽입 / 제거 / 조회

```python
heapq.heappop(my_list)
heapq.heappush(my_list, -1)
my_list[0]
```

<hr>

## queue - 큐 ✔️

```python
from collections import deque

que = deque([1, 2, 3])
```

#### 💡 원소 중간 삽입

```python
que.insert(i, num)
```

#### 💡 삽입 / 제거 / 조회

```python
que.append(item)
que.popleft()
que[0]
```

<hr>

## counter ✔️

```python
import collections

my_list = ["a", "a", "b", "b", "c"]
collections.Counter(my_list)
# Counter({'a': 2, 'b': 2, 'c': 1})
```

<hr>

## itertools ✔️

```python
import itertools
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import chain
```

<hr>

### 💡 permutations - 순열

```python
permutations(range(1, 10), 3)
permutations(lst)
```

### 💡 combinations - 조합

```python
combinations('ABC', 2)
```

### 💡 product - 중복순열

```python
product(range(1, n1 + 1), range(1, n2 + 1), range(1, n3 + 1))
or_not = [(0, 500), (0, 1500)]
list(product(*or_not))
# [(0,0), (0,1500), (500,0), (500,1500)]
```

### 💡 chain - flatten(2차배열 ->1차배열)

```python
itertools.chain(*board)
chain(*board)
```

<hr>

## dictionary - 해시 ✔️

#### 💡 get

```python
my_dict['total']
my_dict.get('total', 0)
```

#### 💡 제거 - pop : 키가 없는 경우 default 리턴

```python
my_dict.pop('홍길동', 180)
```

#### 💡 탐색

```python
dict.items()
dict.keys()
dict.values()
```

#### 💡 그래프 셋팅 :  get 사용

```python
nodes = {}
for v1, v2 in edge:
    nodes[v1] = nodes.get(v1, []) + [v2]
    nodes[v2] = nodes.get(v2, []) + [v1]
```

#### 💡 그래프 셋팅 with dist :  get 사용

```python
nodes = {}
for v1, v2, d in road:
    nodes[v1] = nodes.get(v1, []) + [(v2, d)]
    nodes[v2] = nodes.get(v2, []) + [(v1, d)]
```

#### 💡 그래프 셋팅 거리 초기화

```python
dist = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}
```

<hr>

## defaultdict ✔️

```python
from collections import defaultdict

dict1 = defaultdict(set)
dict2 = defaultdict(list)
dict3 = defaultdict(int) -> 0
으로
셋팅
```

#### 💡 그래프 셋팅 :  defaultdict 사용

```python
from collections import defaultdict

nodes = defaultdict(list)
for v1, v2 in edge:
    nodes[v1].append(v2)
    nodes[v2].append(v1)
```

<hr>

## set - 셋 ✔️

#### 💡 삽입 / 제거

```python
my_set.add(3)
my_set.remove(3)
```

#### 💡 include

```python
if 3 in my_set:
    print('3 있음')
if 3 not in my_set:
    print('3 없음')
```

#### 💡 합집합, 교집합, 차집합

```python
set1 | set2
set1.update(set2)
set1 - set2
set1 & set2
```

<hr>

## bisect ✔️

```python
from bisect import bisect_left, bisect_right
```

#### 💡 최소값 바로 왼쪽 (최소값 들어갈 index)

```python
bisect_left(lst, start)
```

#### 💡 최대값 바로 오른쪽 (최대값 들어갈 index)

```python
bisect_right(lst, end)
```

#### 💡 count_by_lange

```python
def count_by_lange(lst, start, end):
    return bisect_right(lst, end) - bisect_left(lst, start)
```

<hr>

## DELTA - 방향 ✔️

```python
DELTAS = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 오른쪽 왼쪽 위 아래
DELTAS = [(-1, 0, UP), (1, 0, DOWN), (0, 1, RIGHT), (0, -1, LEFT)]
DELTAS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
DELTAS = {'U': (-1, -1), 'D': (1, 0), 'R': (0, 1)}
NEXT = {'U': 'D', 'D': 'R', 'R': 'U'}
```

<hr>

## visitable - 탐색 범위 확인 ✔️

```python
def visitable(y, x, m, n):
    return 0 <= y < m and 0 <= x < n
```

<hr>

## 소수 ✔️

```python
N, primes = end_num, set()
prime_check = [False, False] + [True] * (N - 1)
for i in range(2, N + 1):
    if prime_check[i]:
        primes.add(i)
        prime_check[i * 2::i] = [False] * len(prime_check[i * 2::i])
```

<hr>

## 최소공배수 / 최대공약수 ✔️

#### 💡 최대공약수

```python
from fractions import gcd

gcd(6, 8)  # 2, deprecated
```

deprecated 되었으므로 math 사용을 권장한다.

```python
# new in version 3.5
import math

math.gcd(6, 8)
```

#### 💡 최소공배수

```python
import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


# new in version 3.9
# math 에 lcm 함수가 추가되었다.

math.lcm(15, 25)  # 75
```

<hr>

## 곱으로 나타내기 ✔️

```python
[(number // i, i) for i in range(1, int(number ** .5) + 1) if number % i == 0]
# number = 24 -> 곱해서 24가되는 경우
[(24, 1), (12, 2), (8, 3), (6, 4)]
```

<hr>

## 이분탐색 ✔️

#### 💡 최소값

```python
def impossible(n, middle, times):
    return sum([middle // x for x in times]) < n


def solution(n, times):
    left, right = 1, max(times) * n
    while left < right:
        middle = (left + right) // 2
        if impossible(n, middle, times):
            left = middle + 1
        else:
            right = middle
    return left
```

#### 💡 최대값

```python
def is_poss(middle, budgets, M):
    return M >= sum([min(middle, budget) for budget in budgets])


def solution(budgets, M):
    left, right = 1, max(budgets)
    while left < right:
        middle = (left + right + 1) // 2
        if is_poss(middle, budgets, M):
            left = middle
        else:
            right = middle - 1
    return right
```

<hr>

## sort ✔️

#### 💡 sort

```python
lst.sort()
dist.sort(reverse=True)
lst.sort(key=lambda x: (x * 4)[:4], reverse=True)
```

#### 💡 sorted

```python
sorted(lst)
sorted(lst, reverse=True)
sorted(answer, key=lambda x: (x[0], -x[1], x[2]))
```

<hr>

## count ✔️

#### 💡 요소 개수 세기

```python
lst.hit(0)
[*row, *col, *diag].count(n)
```

#### 💡 filter count

```python
filter = [item for item in items if 조건식]
len(filter)
```

<hr>

## 2차배열 ✔️

#### 💡 초기화 m * n 행렬

```python
board = [[0] * n for i in range(m)]
```

#### 💡 행열 뒤집기 (n*m)

```python
reversed = list(map(list, zip(*board)))
```

#### 💡 90도 회전

```python
def rotate90(arr):
    return list(zip(*arr[::-1]))
```

<hr>

## string ✔️

#### 💡 글자 replace

```python
query.replace('?', 'a')
```

#### 💡 기준으로 쪼개기

```python
s.split("},{")
```

#### 💡 join

```python
number = int(''.join(x))
```

#### 💡 string 갯수 단위로 쪼개기

```python
splited = [s[i:i + size] for i in range(0, LENGTH, size)]
# size = 3 : aabbaccc -> ['aab', 'bac', 'cc']
```

<hr>

## 정규식

```python
import re
```

#### 💡 찾기

```python
re.search("^" + pre + ".+", number)
re.findall(query, word)
lst = re.findall('\d+', s)
# ['2', '2', '1', '3', '4']
re.compile("(\D)")
```

<hr>

## 원형 선형으로 ✔️

```python
weak_point = weak + [w + n for w in weak]
```

<hr>

## math ✔️

```python
import math
```

#### 💡 ceil

```python
math.ceil(num / div)
```

#### 💡 factorial

```python
math.factorial(3)
```