# 프로그래머스 - 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

# 2글자씩 쪼개서 리스트로 반환하는 함수
def split_2words(p: str):
    result = list()
    for i in range(len(p) - 1):
        if (ch := p[i:i + 2]).isalpha():
            result.append(ch)
    return result


# 다중 집합의 교집합, 합집합 구하는 함수
# 잘 정리된 링크가 있어 사용
# https://codingpractices.tistory.com/48
def list_union(a: list, b: list):
    a1 = a.copy()
    a2 = a.copy()
    for i in b:
        if i not in a1:
            a2.append(i)
        else:
            a1.remove(i)
    return a2


def list_intersaction(a: list, b: list):
    result = []
    for i in b:
        if i in a:
            a.remove(i)
            result.append(i)
    return result


def solution(str1: str, str2: str):
    a = split_2words(str1.upper())
    b = split_2words(str2.upper())
    union = list_union(a, b)
    intersaction = list_intersaction(a, b)

    if union:
        return int((len(intersaction) / len(union)) * 65536)
    else:
        return 65536
