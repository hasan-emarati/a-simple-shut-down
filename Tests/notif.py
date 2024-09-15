from plyer import notification

notification.notify(
    title='Notification Title',
    message='This is the notification message!',
    app_name='Your App Name',  # Optional: نام برنامه‌ای که اعلان را می‌فرستد
    timeout=0 # Optional: زمان نمایش اعلان به ثانیه
)
