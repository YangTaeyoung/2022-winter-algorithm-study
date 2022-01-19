# 프로그래머스 - 괄호 변환 문제
# https://programmers.co.kr/learn/courses/30/lessons/60058

# 괄호 문자를 뒤집는 함수
def reverse_ch(ch):
    if ch == "(":
        return ")"
    else:
        return "("


def reverse_p(p: str):
    reversed_p = list()
    for ch in p:
        reversed_p.append(reverse_ch(ch))
    return "".join(reversed_p)


# 올바른 괄호 문자열인지 체크하는 함수
def is_balanced(p: str):
    verified_stack = list()
    for ch in p:
        if ch == "(":
            verified_stack.append(ch)
        else:
            if not verified_stack:
                return False
            else:
                verified_stack.pop(-1)
    return True


# 문자열을 U,V로 나누는 함수
def divide_uv(p: str):
    parenthsis_dict = {
        "(": 0,
        ")": 0
    }
    for ch in p:
        parenthsis_dict[ch] += 1
        if parenthsis_dict["("] == parenthsis_dict[")"]:
            slice_idx = parenthsis_dict["("] + parenthsis_dict[")"]
            return p[:slice_idx], p[slice_idx:]  # u, v


def process(p):
    # Step 1
    if len(p) == 0:
        return p
    # Step 2
    u, v = divide_uv(p)

    # Step 3
    if is_balanced(u):
        # Step 3-1
        return u + process(v)
    # Step 4
    else:
        # Step 4-1      4-2       4-3         4-4
        return "(" + process(v) + ")" + reverse_p(u[1:-1])  # Step 4-5


def solution(p):
    return process(p)
