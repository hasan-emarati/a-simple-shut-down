from datetime import datetime
from dateutil.relativedelta import relativedelta
from persiantools.jdatetime import JalaliDate
import time
import os
from pynput import keyboard

class TimeSelector : 
    def __init__ (self):
        print("Hello World")
        
    def Calendar(self): # In this function, we specify the system shutdown date along with the shutdown time on the calendar
        Now = datetime.Now()
        JalaliCalendar = JalaliDate(Now.year, Now.month, Now.day)
        Jalali_Date = {JalaliCalendar.strftime('%a، %d %b %Y')}
        MiladiDate = {Now.strftime('%A, %B %d, %Y')}
        Time = {Now.strftime('%H:%M:%S')}
        
    def BlackoutTime(self, hour , minute): # In this function, we only specify the shutdown time
        now = time.localtime()
        current_hour = now.tm_hour
        current_minute = now.tm_min
        if current_hour == hour and current_minute == minute:
            os.system("shutdown /s /t 10") 
            for i in range(11):
                if i == 0 :
                    print(f'Shutdown your computer in 10 seconds')
                    print("If you have given up on turning off the system, press ESC key")
                    time.sleep(1)
                print(f'Shutdown your computer in {i} seconds')
                time.sleep(1)
                if keyboard.Key.esc:
                    os.system("shutdown /a") 
                    print("System shutdown canceled")
        else:
            print(f"Current time: {current_hour}:{current_minute}")
            time.sleep(60)  
            
    def countdown(hours, minutes, seconds):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        while total_seconds:
            hours, rem = divmod(total_seconds, 3600)
            minutes, seconds = divmod(rem, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            total_seconds -= 1