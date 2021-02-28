# import datetime obj
from datetime import datetime
import pandas as pd

'''
Function to compute whether a student is present, late, or absent
    Parameter: attendance time, class ID
    Returns: attendance status
'''
def compute_attendance_time(attendance_time, class_id):
    # attendance_time = raw_attendance_time.strftime("%H:%M:%S")
    print(get_day(attendance_time))



    now = datetime.now()
    start_time = now.replace(hour=15, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=15, minute=28, second=0, microsecond=0)

    if attendance_time <= start_time:
        print(attendance_time)
        print("Hadir tepat waktu")
    elif attendance_time >= end_time:
        print("Telat banged woe dah beres kali")
    else:
        min_elapsed = attendance_time - start_time
        print("Terlambat ")
        print(min_elapsed)

'''
Function to convert date to day name in Indonesian
    Parameter: date
    Returns: day name in Indonesian
'''
def get_day(date):
    # source: https://www.codespeedy.com/how-to-find-day-name-from-date-in-python/
    day_name = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    return day_name[date.weekday()]

compute_attendance_time(datetime.now(), "181101")