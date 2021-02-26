# import datetime obj
from datetime import datetime

def compute_time(attendance_time, class_id):
    # attendance_time = raw_attendance_time.strftime("%H:%M:%S")
    now = datetime.now()
    start_time = now.replace(hour=15, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=15, minute=28, second=0, microsecond=0)

    if attendance_time <= start_time:
        print("Hadir tepat waktu")
    elif attendance_time >= end_time:
        print("Telat banged woe dah beres kali")
    else:
        min_elapsed = attendance_time - start_time
        print("Terlambat ")
        print(min_elapsed)

compute_time(datetime.now(), "181101")