# https://www.acmicpc.net/problem/5532
import sys
from math import ceil

sys.stdin = open("input.txt")
###

days_of_vacation = int(input()) # 20
korean_total_page = int(input()) # 25
math_total_page = int(input()) # 30

korean_page_per_day = int(input()) # 6
math_page_per_day = int(input()) # 8

def days_of_playing(days_of_vacation, korean_total_page, math_total_page, korean_page_per_day, math_page_per_day):
    korean_study_day = ceil(korean_total_page / korean_page_per_day)
    math_study_day = ceil(math_total_page / math_page_per_day)

    result = days_of_vacation - int(max(korean_study_day, math_study_day))
    return result # 15

print(days_of_playing(days_of_vacation, korean_total_page, math_total_page, korean_page_per_day, math_page_per_day))
