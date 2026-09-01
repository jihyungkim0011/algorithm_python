import math


def replace_step(m):
    return m.replace("C#", "c").replace("D#", "d").replace("G#", "g").replace("A#", "a").replace("B#", "b")


def solution(m, musicinfos):
    m = replace_step(m)
    max_play_time = 0

    for musicinfo in musicinfos:
        start_time, end_time, name, melody = musicinfo.split(",")
        play_time = int(end_time[:2]) * 60 + int(end_time[3:]) - int(start_time[:2]) * 60 - int(start_time[3:])

        melody = replace_step(melody)
        melody_repeated_count = math.ceil(play_time / len(melody))
        melody_played = (melody * melody_repeated_count)[:play_time]

        if m in melody_played and play_time > max_play_time:
            return name
    return None

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos)) # "HELLO" 가 출력되어야 합니다.