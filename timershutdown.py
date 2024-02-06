import datetime
import os
import time


now= datetime.datetime.now().time()
hour=int(input('which hour?:'))
minute=int(input('which minute?:'))
set_time=str(datetime.time(hour,minute,1))
while True :
    now=datetime.datetime.now().strftime("%H:%M:%S")
    if now==set_time:
        os.system("shutdown /s /t 0")
        break
    time.sleep(1)
