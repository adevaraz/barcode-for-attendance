# import datetime obj
from datetime import datetime
import time
from search_students import search_student
import pandas as pd
import constants

'''
Function to compute whether a student is present, late, or absent
    Parameter: attendance time, class ID
    Returns: attendance status
'''
def compute_attendance_time(attendance_time, student_id):
    # attendance_time = raw_attendance_time.strftime("%H:%M:%S")
    day = get_day(attendance_time)
    class_id = search_student(student_id)

    if day != "Sabtu" and day != "Minggu":
        # Read data_matkul.xlsx
        # In order to read .xlsx file, please install xlrd (for Excel 2003 and Excel 2007)
        # or openpyxl (for Excel 2007+) first

        df = pd.read_excel(constants.DATA_MATKUL_LOC, sheet_name=class_id)

        today_subjects = df[(df["hari"] == day)]
        current_subject = get_current_subject(today_subjects, attendance_time.time())
        
        # If not in break time
        if current_subject != -1:
            raw_start = df.loc[(df["hari"] == day) & (df["Kode_MK"] == current_subject), ["jam_mulai"]]
            raw_end = df.loc[(df["hari"] == day) & (df["Kode_MK"] == current_subject), ["jam_selesai"]]

            start_time = raw_start.values[0][0]
            end_time = raw_end.values[0][0]

            if attendance_time.time() == start_time:
                print(attendance_time)
                print("Hadir tepat waktu")
            elif attendance_time.time() >= end_time:
                print("Telat banged woe dah beres kali")
            else:
                print(start_time)
                print(end_time)
                min_elapsed = minutes_difference(start_time, attendance_time.time())
                print("Terlambat " + str(min_elapsed) + " menit")
        else:
            print("Tidak ada mata kuliah berlangsung. Silahkan coba lagi saat mata kuliah sudah dimulai.")
    else:
        print("Tidak ada jadwal kuliah yang dapat dihadiri.")

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
    # Convert from datetime.time to datetime
    datetime_1 = datetime.combine(datetime.today(), time_1)
    datetime_2 = datetime.combine(datetime.today(), time_2)
    
    min_elapsed = abs((datetime_2 - datetime_1).total_seconds() / 60.0)
    return int(min_elapsed)

'''
Function to compute minutes difference
    Parameter: today all subjects, attendance time
    Returns: subject ID, -1 means currently is break
'''
def get_current_subject(today_subjects, time):
    for subject in today_subjects.values:
        start = subject[1]
        end = subject[2]

        if time >= start and time <= end:
            return subject[3]
        else:
            return -1

compute_attendance_time(datetime.now(), "181524007")