# 프로그래머스 - 수식 최대화 문제
# https://programmers.co.kr/learn/courses/30/lessons/67257
import re


# 리스트에서 사용 가능한 index 함수가 찾지 못할 시 ValueError을 발생시키므로
# 찾지 못할 경우 -1을 반환하도록 수정
def find_list(li: list, tar):
    try:
        return li.index(tar)
    except ValueError:
        return -1


# 연산자 앞뒤 계산 후 계산 결과를 리스트에 집어넣고 리스트 반환
def calculate_1oper(exp: list, oper: str):
    while (oper_idx := find_list(exp, oper)) != -1:
        exp[oper_idx - 1] = str(eval(exp[oper_idx - 1] + exp[oper_idx] + exp[oper_idx + 1]))
        for _ in range(2):
            exp.pop(oper_idx)
    return exp


# 순한 맛
def solution(expression):
    # 연산자 *, +, - 를 기준으로 문자열을 쪼개어 리스트로 반환
    # python split의 경우 한 문자열을 기준으로 밖에 쪼갤 수 없음.
    expression = re.split('([-|+|*])', expression)
    # 연산자 리스트
    oper_list = ["*", "-", "+"]
    answer_list = []
    for oper1 in oper_list:
        for oper2 in oper_list:
            for oper3 in oper_list:
                if oper1 == oper2 or oper2 == oper3 or oper1 == oper3:
                    continue
                candidate = expression.copy()
                candidate = calculate_1oper(candidate, oper1)
                candidate = calculate_1oper(candidate, oper2)
                candidate = calculate_1oper(candidate, oper3)
                answer_list.append(abs(int(candidate[0])))
    return max(answer_list)


# 극한의 리스트 컴프리헨션 버전
def solution_2(expression):
    expression = re.split('([-|+|*])', expression)
    oper_list = ["*", "-", "+"]
    return max(
        [
            abs(int(calculate_1oper(calculate_1oper(calculate_1oper(expression.copy(), oper1), oper2), oper3)[0]))
            for oper1 in oper_list
            for oper2 in oper_list
            for oper3 in oper_list
            if oper1 != oper2 and oper2 != oper3 and oper1 != oper3
        ]
    )
