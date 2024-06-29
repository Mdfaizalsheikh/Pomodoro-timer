import tkinter as tk
import time 
from threading import Thread

def run_timer(label, minutes):
  total_seconds=minutes*60
  while total_seconds>0:
    mins, secs= divmod(total_seconds, 60)
    time_format= f"{min:2d}:{secs:2d}"
    label.config(text=time_format)
    root.update() 
    time.sleep(1)
    total_seconds -=1
  label.config(text="Time's up! ")

def Pomodoro ():
  work_label.config(text=" Work time")
  run_timer(timer_label, 25)
  break_label.config(text="Break Time")
  run_timer(timer_label, 5)

root= tk.Tk()
root.title("Pomodoro Timer")

timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

work_label = tk.Label(root, text="Work time", font=("Helvetica", 24))
work_label.pack(pady=10)

break_label = tk.Label(root, text="", font=("Helvetica", 24))
break_label.pack(pady=10)

start_button = tk.Button(root, text="Start", command=lambda: Thread(target=Pomodoro).start())
start_button.pack(pady=20)

root.mainloop()
