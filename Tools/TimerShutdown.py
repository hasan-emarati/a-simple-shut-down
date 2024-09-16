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
        current_second = now.tm_sec

        if hours < 24 and minutes < 60 and seconds < 60:
            total_seconds = (hours - current_hour) * 3600 + (minutes - current_minute) * 60 + (seconds - current_second)

            if total_seconds < 0:
                print("The specified time has passed the current time.")
                return
            count = 0
            while total_seconds > 0:
                hours_left, rem = divmod(total_seconds, 3600)
                minutes_left, seconds_left = divmod(rem, 60)
                timer = '{:02d}:{:02d}:{:02d}'.format(hours_left, minutes_left, seconds_left)
                print(f"your computer Shutdown in {timer}", end="\r")
                time.sleep(1)
                total_seconds -= 1
                count += 1 
                if count == 1 :
                    notification.notify(
                    title='The system will shut down' ,
                    message=f'The system will shut down in {timer}.',
                    app_name='Shutdown Timer',
                    timeout=10
                    )                     

            notification.notify(
                title='The system will shut down' ,
                message='The system will shut down in 30 seconds.',
                app_name='Shutdown Timer',
                timeout=10
            )

            print("\nThe system will shut down in 30 seconds.")
            print("If you have given up on shutting down your system, press Ctrl + C")
            time.sleep(30)
            os.system("shutdown /s /t 10")

        else:
            print("The time entered is not valid.")

    def countdown(hours, minutes, seconds):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        now = time.localtime()
    
        new_hours, new_minutes = divmod(now.tm_min + minutes, 60)
        new_seconds = (now.tm_sec + seconds) % 60
        shutdown_hours = (now.tm_hour + hours + new_hours) % 24
        shutdown_minutes = (now.tm_min + minutes + (now.tm_sec + seconds) // 60) % 60

        Shutdown_Time = 'Shutdown in {:02d}:{:02d}:{:02d}'.format(shutdown_hours, shutdown_minutes, new_seconds)
        print(Shutdown_Time)
        
        notification.notify(
        title='a simple shutdown',
        message=f'your cumputer has {Shutdown_Time}',
        app_name='a simple shutdown',  
        timeout=0 
        )
        while total_seconds:
            hours, rem = divmod(total_seconds, 3600)
            minutes, seconds = divmod(rem, 60)
            timer = 'Timer  {:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            total_seconds -= 1
            if total_seconds == 0:
                # print("\nbom")
                print ("Shutdown completed")
                os.system("shutdown /s /t 10") 
                print ("Shutdown completed")
                        