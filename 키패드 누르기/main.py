# 프로그래머스 키패드 누르기 문제 풀이
# 링크: https://programmers.co.kr/learn/courses/30/lessons/67256

# 각 번호별 좌표값을 저장하는 딕셔너리
key_pad = {
    "1": (0, 0, "L"), "2": (0, 1, "M"), "3": (0, 2, "R"),
    "4": (1, 0, "L"), "5": (1, 1, "M"), "6": (1, 2, "R"),
    "7": (2, 0, "L"), "8": (2, 1, "M"), "9": (2, 2, "R"),
    "*": (3, 0, "L"), "0": (3, 1, "M"), "#": (3, 2, "R")
}


# 각 번호 사이의 거리를 반환하는 함수
def get_distance(num1: str, num2: str):
    return abs(key_pad[num1][0] - key_pad[num2][0]) + abs(key_pad[num1][1] - key_pad[num2][1])


def solution(numbers: list, hand: str):
    answer = []
    # 초기 손 위치 세팅
    hand_dict = {
        "L": "*",
        "R": "#"
    }

    # 버튼을 누름에 따라 L혹은 R 출력하게 설정
    for num in numbers:
        if key_pad[str(num)][2] == "M":
            if get_distance(hand_dict['L'], str(num)) == get_distance(hand_dict['R'], str(num)):
                answer.append(hand[0].upper())
                hand_dict[hand[0].upper()] = str(num)
            elif get_distance(hand_dict['L'], str(num)) < get_distance(hand_dict['R'], str(num)):
                answer.append("L")
                hand_dict["L"] = str(num)
            else:
                answer.append("R")
                hand_dict["R"] = str(num)
        else:
            answer.append(key_pad[str(num)][2])
            hand_dict[key_pad[str(num)][2]] = str(num)

    return "".join(answer)
