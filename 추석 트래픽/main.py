# 프로그래머스 - 추석트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676
import math
import datetime


def get_time(time):
    return datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S.%f")


def get_contained_count(start_time, ended_time, records: list):
    cnt = 0
    print(f"{get_time(start_time)} 부터 {get_time(ended_time)} 까지의 시간을 검사합니다.")
    for record in records:
        print(f"Case Checking {get_time(record[0])} ~ {get_time(record[1])}")
        if record[0] <= start_time < record[1]:
            print("Case 1 Detected")
            cnt += 1
        elif record[0] < ended_time <= record[1]:
            print("Case 2 Detected")
            cnt += 1
        elif record[0] <= start_time < ended_time <= record[1]:
            print("Case 3 Detected")
            cnt += 1
    return cnt


def area_divide(start_time, ended_time):
    return [(start_time - 1, start_time),
            (start_time, start_time + 1),
            (ended_time - 1, ended_time),
            (ended_time, ended_time + 1)]


def solution(lines: list):
    time_records = list()
    answer_dict = dict()
    for line in lines:
        line_splited = line.split()
        ended_time = datetime.datetime.strptime(f"{line_splited[0]} {line_splited[1]}", "%Y-%m-%d %H:%M:%S.%f")
        start_time = ended_time - datetime.timedelta(seconds=float(line_splited[-1][:-1]))
        time_records.append((start_time.timestamp(), ended_time.timestamp()))
    for time in time_records:
        for area in area_divide(time[0], time[1]):
            answer_dict[area] = get_contained_count(area[0], area[1], time_records)
    return answer_dict[max(answer_dict, key=lambda x: answer_dict.get(x))]


print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
