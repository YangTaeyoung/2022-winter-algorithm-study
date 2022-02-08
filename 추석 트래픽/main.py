# 프로그래머스 - 추석트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676
import math


# import datetime
#
#
# def get_time(time):
#     return datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S.%f")
#
#
# def get_contained_count(start_time, ended_time, records: list):
#     cnt = 0
#     print(f"{get_time(start_time)} 부터 {get_time(ended_time)} 까지의 시간을 검사합니다.")
#     for record in records:
#         print(f"Case Checking {get_time(record[0])} ~ {get_time(record[1])}")
#         if record[0] <= start_time < record[1]:
#             print("Case 1 Detected")
#             cnt += 1
#         elif record[0] < ended_time <= record[1]:
#             print("Case 2 Detected")
#             cnt += 1
#         elif record[0] <= start_time < ended_time <= record[1]:
#             print("Case 3 Detected")
#             cnt += 1
#     return cnt
#
#
# def area_divide(start_time, ended_time):
#     return [(start_time - 1, start_time),
#             (start_time, start_time + 1),
#             (ended_time - 1, ended_time),
#             (ended_time, ended_time + 1)]
#
#
# def solution(lines: list):
#     time_records = list()
#     answer_dict = dict()
#     for line in lines:
#         line_splited = line.split()
#         ended_time = datetime.datetime.strptime(f"{line_splited[0]} {line_splited[1]}", "%Y-%m-%d %H:%M:%S.%f")
#         start_time = ended_time - datetime.timedelta(seconds=float(line_splited[-1][:-1]))
#         time_records.append((start_time.timestamp(), ended_time.timestamp()))
#     for time in time_records:
#         for area in area_divide(time[0], time[1]):
#             answer_dict[area] = get_contained_count(area[0], area[1], time_records)
#     return answer_dict[max(answer_dict, key=lambda x: answer_dict.get(x))]
#
#
# print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
# 테스트 케이스 지속적인 실패.. 푸는 것 포기


# 문제의 답안을 떠올리지 못해 인터넷에 있는 링크를 통해 학습하였음
# https://velog.io/@mrbartrns/%ED%8C%8C%EC%9D%B4%EC%8D%AC-1%EC%B0%A8%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A0%88%EB%B2%A83
# 해당 링크에서 답안을 확인함을 알림
# python코드
def solution(lines):
    answer = 0
    # 시작 시간 배열
    start_time = []
    # 끝 시간 배열
    end_time = []

    for t in lines:
        time = t.split(" ")
        # 시간 분리 # 여기까지는 timestamp로 구분했던 나와 같음.
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        # i번째는 현재 자신의 시작시간이고, i 이하는 그 이전의 시작시간이므로 카운트 할 필요가 없다.
        # 감탄한 부분 for문의 range를 잘 보면 i부터 두번째 for문이 시작함을 알 수 있음
        # end 시간이 정렬되어 있음을 이용한 것
        for j in range(i, len(lines)):
            # 확인하는 부분, 나는 해당 부분에서 3번의 비교가 필요했는데, 이분은 단 한번으로 끝냄, 인덱스 i의 조절 덕분
            # 즉 end[i]를 체크했다면 start[i]를 볼 필요가 없다는 뜻. 어쩌면 당연한 것..
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer


# 시간을 정수로 바꾸는 함수
def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


# 끝 시간을 기준으로 시작 시간을 구하는 함수
def get_start_time(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1
