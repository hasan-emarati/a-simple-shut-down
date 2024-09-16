from datetime import datetime
from dateutil.relativedelta import relativedelta
from persiantools.jdatetime import JalaliDate
import time

def countdown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    now = time.localtime()
    Shutdown_Time = 'Shutdown in {:02d}:{:02d}:{:02d}'.format(now.tm_hour  + hours, now.tm_min + minutes , now.tm_sec + seconds)
    print(Shutdown_Time)
    # print(f"shutdown in {now + total_seconds}")
    while total_seconds:
        hours, rem = divmod(total_seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        timer = 'Timer  {:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
        if total_seconds == 0:
            print("\nbom")
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

countdown(hours, minutes, seconds)
