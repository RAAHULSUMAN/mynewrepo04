import tkinter as tk
from datetime import datetime


def update_clock() -> None:
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%A, %B %d, %Y"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Clock")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

time_label = tk.Label(
    root,
    font=("Segoe UI", 48, "bold"),
    foreground="#ffffff",
    background="#1e1e1e",
)
time_label.pack(padx=32, pady=(24, 4))

date_label = tk.Label(
    root,
    font=("Segoe UI", 14),
    foreground="#bdbdbd",
    background="#1e1e1e",
)
date_label.pack(padx=32, pady=(0, 24))

update_clock()
root.mainloop()