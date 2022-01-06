# 프로그래머스 - 다트게임 문제
# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult: str):
    operator_dict = {
        "S": (lambda x: x), "D": (lambda x: x ** 2),
        "T": (lambda x: x ** 3), "#": (lambda x: x * (-1)),
        "*": (lambda x: x * 2)
    }
    current_num = 0
    answer = []
    i = 0
    while i <= len(dartResult):
        if i == len(dartResult):
            answer.append(current_num)
            break
        elif (ch := dartResult[i]).isnumeric():
            answer.append(current_num)
            if (ch2 := dartResult[i:i + 2]).isnumeric():
                ch = ch2
                i += 1
            current_num = int(ch)
        else:
            current_num = operator_dict[ch](current_num)
            if ch == '*':
                answer[len(answer) - 1] = operator_dict[ch](answer[len(answer) - 1])
        i += 1
    return sum(answer)
