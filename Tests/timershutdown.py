# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# from persiantools.jdatetime import JalaliDate
# import time

# while True:
#     now = datetime.now()
#     jalali_date = JalaliDate(now.year, now.month, now.day)
    
#     print(f"shamsi  : {jalali_date.strftime('%a، %d %b %Y')}")
#     print(f"miladi  : {now.strftime('%A, %B %d, %Y')}")
#     print(f"Time    : {now.strftime('%H:%M:%S')}")
#     print("_______________________________________________________")
#     time.sleep(1)

import time

def countdown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    while total_seconds:
        hours, rem = divmod(total_seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

countdown(hours, minutes, seconds)