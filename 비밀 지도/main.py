# 프로그래머스 - 비밀지도 풀이
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 그냥 가끔 그럴 때가 있잖음.. 어떻게든 짧게 적고 싶어질 때
def solution(n, arr1, arr2):
    return [str(bin(arr1[i] | arr2[i]))[2:].zfill(n).replace("1", "#").replace("0", " ") for i in range(n)]