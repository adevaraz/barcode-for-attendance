# import datetime obj
from datetime import datetime
import pandas as pd
import constants

'''
Function to compute whether a student is present, late, or absent
    Parameter: attendance time, class ID
    Returns: attendance status
'''
def compute_attendance_time(attendance_time, class_id):
    # attendance_time = raw_attendance_time.strftime("%H:%M:%S")
    day = get_day(attendance_time)

    # Read data_matkul.xlsx
    # In order to read .xlsx file, please install xlrd (for Excel 2003 and Excel 2007)
    # or openpyxl (for Excel 2007+) first
    print(constants.DATA_MATKUL_LOC)
    d_file = pd.read_excel(constants.DATA_MATKUL_LOC, sheet_name=class_id)
    # TODO: itung selisih terkecil current time ke tiap matkul di current day buat tentuin current matkul
    print(d_file.iloc[3])

    now = datetime.now()
    start_time = now.replace(hour=14, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=15, minute=28, second=0, microsecond=0)

    if attendance_time <= start_time:
        print(attendance_time)
        print("Hadir tepat waktu")
    elif attendance_time >= end_time:
        print("Telat banged woe dah beres kali")
    else:
        min_elapsed = minutes_difference(start_time, attendance_time)
        print("Terlambat " + str(min_elapsed) + " menit")

'''
Function to convert date to day name in Indonesian
    Parameter: date
    Returns: day name in Indonesian
'''
def get_day(date):
    # source: https://www.codespeedy.com/how-to-find-day-name-from-date-in-python/
    day_name = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    return day_name[date.weekday()]

'''
Function to compute minutes difference
    Parameter: time_1, time_2
    Returns: min elapsed as integer
'''
def minutes_difference(time_1, time_2):
    min_elapsed = abs((time_2 - time_1).total_seconds() / 60.0)
    return int(min_elapsed)

compute_attendance_time(datetime.now(), "181101")