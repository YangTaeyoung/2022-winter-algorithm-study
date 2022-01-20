# 프로그래머스 - 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065


def solution(s: str):
    tuples = sorted(eval(s.replace("{", "[").replace("}", "]")), key=len)
    return [tuples[i][0] if i == 0 else list(set(tuples[i]).difference(set(tuples[i - 1])))[0] for i in range(len(tuples))]