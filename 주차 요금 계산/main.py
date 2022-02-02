# 프로그래머스 - 주차요금 계산
# https://programmers.co.kr/learn/courses/30/lessons/92341


import math


# 시간을 계산하는 함수
def get_time_as_minute(time_list: list):
    time = 0
    if len(time_list) % 2:  # 입차만 있고 출차는 없는 경우
        time_list.append("23:59")  # 출차를 23:59로 가정함
    for i in range(len(time_list) // 2):
        time_1_splited = list(map(int, time_list[i * 2].split(':')))
        time_2_splited = list(map(int, time_list[i * 2 + 1].split(':')))
        time += time_2_splited[1] - time_1_splited[1] + (time_2_splited[0] - time_1_splited[0]) * 60
    return time


# 구한 시간(분)을 기준으로 요금을 산정하는 함수
def get_fee(time_as_minute: int, fees):
    if time_as_minute < fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((time_as_minute - fees[0]) / fees[2]) * fees[3]


def solution(fees, records):
    infos = {}
    result_dict = {}
    # 레코드 분류 (1차): infos[차량번호] = [출발시각1, 도착시각1, 출발2, 도착2 ...]
    for record in records:
        # 문자열을 쪼갬
        record_splited = record.split()
        if infos.get(record_splited[1]):
            infos[record_splited[1]].append(record_splited[0])
        else:
            infos[record_splited[1]] = list()
            infos[record_splited[1]].append(record_splited[0])
    # 레코드 분류 (2차): result_dict[차량 번호]: 총 주차시간
    for car_num in infos:
        result_dict[car_num] = get_time_as_minute(infos[car_num])
    return [get_fee(result_dict[car_num], fees) for car_num in sorted(result_dict.keys())]


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
