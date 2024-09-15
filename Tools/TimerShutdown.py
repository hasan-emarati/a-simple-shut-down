from datetime import datetime
from dateutil.relativedelta import relativedelta
from persiantools.jdatetime import JalaliDate
import time
import os
from plyer import notification
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
        if current_hour == hour and current_minute == minute: # shut down the system in current time 
            notification.notify(
            title='Shutdowner ',
            message='Your system will shut down in 30 seconds',
            app_name='Shutdowner',  
            timeout=0 
            )
            total_seconds = 30  
            print(f'Shutdown your computer in {total_seconds} seconds')
            print("If you have given up on turning off the system, press Ctrl + C keys")
            while total_seconds:
                hours, rem = divmod(total_seconds, 3600)
                minutes, seconds = divmod(rem, 60)
                timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
                print(timer, end="\r")
                time.sleep(1)
                total_seconds -= 1
                if total_seconds == 0:
                    print("\nShutdown")
                    os.system("shutdown /s /t 10")
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
            if total_seconds == 0:
                # print("\nbom")
                print ("Shutdown")
                os.system("shutdown /s /t 10") 
                        