# 2018 kakao blind recruitment

from collections import deque

cache_size = 2
_cities = ["Jeju", "Pangyo", "NewYork", "newyork"]


# answer = 50

def solution(cacheSize, cities):
    cache_hit = 0
    cache_miss = 0
    cache = []

    # 중복제거가 아니라 대소문자 구분만 하지 않도록 해야한다.
    cities = [city.lower() for city in cities]
    # print(cities)

    if cacheSize == 0:
        cache_miss += len(cities) * 5
        return cache_miss

    # 뒤에 넣고 앞에서 뺀다
    while cities:
        city = cities.pop(0)
        if city in cache:
            cache.append(city)
            cache_hit += 1
            if len(cache) > cacheSize:
                cache.pop(cache.index(city))
        else:
            cache.append(city)
            cache_miss += 5
            if len(cache) > cacheSize:
                cache.pop(0)

    return cache_hit + cache_miss


print(solution(cache_size, _cities))
