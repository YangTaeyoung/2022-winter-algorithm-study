# 프로그래머스 - 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3


class LruCache:
    def __init__(self, cache_size):
        self.cache_dict = dict()
        self.cache_size = cache_size
        self.time = 0

    def find_oldest(self):
        return max(self.cache_dict, key=self.cache_dict.get)

    def time_plus(self):
        for key in self.cache_dict:
            self.cache_dict[key] += 1

    def insert(self, elem):
        elem = elem.lower()
        if self.cache_size == 0:
            self.time += 5
            return
        # 캐시는 cacheSize만큼 쌓여있으나, elem에 해당하는 요소가 캐시에 없는 경우
        if elem not in self.cache_dict.keys():
            self.time += 5
            # 아직 캐시가 cacheSize만큼 쌓이지 않은 경우
            if len(self.cache_dict) == self.cache_size:
                self.cache_dict.pop(self.find_oldest())
        else:
            self.time += 1
        self.time_plus()
        self.cache_dict[elem] = 0


def solution(cacheSize, cities):
    cache = LruCache(cacheSize)
    for city in cities:
        cache.insert(city)

    return cache.time


print(solution(2, 	["Jeju", "Pangyo", "NewYork", "newyork"]))
