import time
import os
from plyer import notification

def BlackoutTime(hours, minutes, seconds):
    now = time.localtime()
    count = 0
    current_hour = now.tm_hour
    current_minute = now.tm_min
    current_second = now.tm_sec
    
    if hours < 24 and minutes < 60 and seconds < 60:
        total_seconds = (hours - current_hour) * 3600 + (minutes - current_minute) * 60 + (seconds - current_second)
        
        if total_seconds < 0:
            print("The specified time has passed the current time.")
            return
        
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
        # os.system("shutdown /s /t 10")
    
    else:
        print("The time entered is not valid.")

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

BlackoutTime(hours, minutes, seconds)
