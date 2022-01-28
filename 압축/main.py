# 프로그래머스 - 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684


alpha_dict = {chr(i): i - 64 for i in range(65, 91)}


def find_longest(msg):
    a = 1
    while a < len(msg) + 1 and msg[:a] in alpha_dict.keys():
        a += 1
    return a - 1


def solution(msg: str):
    answer = []
    # 슬라이싱을 위한 인덱싱
    while msg != "":
        next_idx = find_longest(msg)
        answer.append(alpha_dict[msg[:next_idx]])
        alpha_dict[msg[:next_idx + 1]] = len(alpha_dict) + 1
        msg = msg[next_idx:]
    return answer


print(solution("KAKAO"))
