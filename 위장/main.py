# 프로그래머스 - 해시 - 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    cloth_dict = {}
    for cloth in clothes:
        if cloth_dict.get(cloth[1]):
            cloth_dict[cloth[1]].append(cloth[0])
        else:
            cloth_dict[cloth[1]] = [cloth[0]]
    for cloth in cloth_dict:
        answer *= len(cloth_dict[cloth]) + 1
    return answer-1