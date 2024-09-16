import customtkinter as ctk
import time

# تنظیمات اولیه CustomTkinter
ctk.set_appearance_mode("dark")  # حالت تیره شبیه ویندوز 10
ctk.set_default_color_theme("blue")  # تم رنگی مشابه ویندوز 10

# ایجاد پنجره اصلی
root = ctk.CTk()
root.geometry("400x300")
root.title("Shutdown Timer")

# انیمیشن ساده برای دکمه
def animate_button(button):
    for i in range(0, 11):
        button.place_configure(rely=0.5 + i*0.01)
        root.update()
        time.sleep(0.02)

# قاب برای عنوان
frame_title = ctk.CTkFrame(master=root)
frame_title.pack(pady=20, padx=20, fill="both", expand=True)

# عنوان اپلیکیشن
label_title = ctk.CTkLabel(master=frame_title, text="Shutdown Timer", font=("Arial", 24, "bold"))
label_title.pack(pady=12, padx=10)

# ایجاد ورودی ساعت، دقیقه و ثانیه
frame_time = ctk.CTkFrame(master=root)
frame_time.pack(pady=10, padx=10, fill="both", expand=True)

label_hour = ctk.CTkLabel(master=frame_time, text="Hours:", font=("Arial", 14))
label_hour.grid(row=0, column=0, padx=10, pady=10)
entry_hour = ctk.CTkEntry(master=frame_time, width=50)
entry_hour.grid(row=0, column=1, padx=10)

label_minute = ctk.CTkLabel(master=frame_time, text="Minutes:", font=("Arial", 14))
label_minute.grid(row=0, column=2, padx=10, pady=10)
entry_minute = ctk.CTkEntry(master=frame_time, width=50)
entry_minute.grid(row=0, column=3, padx=10)

label_second = ctk.CTkLabel(master=frame_time, text="Seconds:", font=("Arial", 14))
label_second.grid(row=0, column=4, padx=10, pady=10)
entry_second = ctk.CTkEntry(master=frame_time, width=50)
entry_second.grid(row=0, column=5, padx=10)

# تابع شروع تایمر
def start_timer():
    hours = entry_hour.get()
    minutes = entry_minute.get()
    seconds = entry_second.get()
    print(f"Timer set for {hours}:{minutes}:{seconds}")
    animate_button(button_start)

# دکمه‌ها با انیمیشن
frame_buttons = ctk.CTkFrame(master=root)
frame_buttons.pack(pady=20, padx=10, fill="both", expand=True)

button_start = ctk.CTkButton(master=frame_buttons, text="Start Timer", command=start_timer, corner_radius=15, fg_color="#3B8ED0")
button_start.grid(row=0, column=0, padx=10)

button_stop = ctk.CTkButton(master=frame_buttons, text="Stop Timer", corner_radius=15, fg_color="#D33F49")
button_stop.grid(row=0, column=1, padx=10)

# دکمه خروج
button_exit = ctk.CTkButton(master=root, text="Exit", command=root.quit, corner_radius=15)
button_exit.pack(pady=10)

root.mainloop()
