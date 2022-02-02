# 프로그래머스 - 방금 그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683


from datetime import datetime

translation_note = {
    "C#": "H",
    "D#": "I",
    "F#": "J",
    "G#": "K",
    "A#": "L"
}


def r_pad_upgraded(pattern, num):
    pattern_list = list(pattern)
    for i in range(num - len(pattern)):
        pattern_list.append(pattern[i % len(pattern)])
    return ''.join(pattern_list)[:num]


def translation_lyric(lyric: str):
    for key in translation_note:
        lyric = lyric.replace(key, translation_note[key])
    return lyric


def solution(m: str, musicinfos: list):
    m = translation_lyric(m)
    candidate = dict()
    for musicinfo in musicinfos:
        music_start, music_end, title, lyrics = musicinfo.split(",")
        real_time = int((datetime.strptime(f"2021-01-28 {music_end}", "%Y-%m-%d %H:%M") - datetime.strptime(
            f"2021-01-28 {music_start}", "%Y-%m-%d %H:%M")).seconds // 60)
        real_lyric = r_pad_upgraded(translation_lyric(lyrics), real_time)
        if real_lyric.find(m) != -1:
            candidate[title] = real_time
    try:
        return max(candidate, key=candidate.get)
    except:
        return "(None)"


print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
