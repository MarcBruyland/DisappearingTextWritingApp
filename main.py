from tkinter import *
YELLOW = "#f7f5dd"
timer = None
MAX_SECONDS_BEFORE_DELETE = 10


def key_pressed(event):
    reset_timer()

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    #lbl_Timer.config(text=str(MAX_SECONDS_BEFORE_DELETE))
    start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    count_down(MAX_SECONDS_BEFORE_DELETE)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    lbl_Timer.config(text=f"{count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        txt.delete("1.0", "end")
        reset_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Text writing app")
window.config(bg=YELLOW)
window.bind("<KeyPress>", key_pressed)

# Label
lbl = Label(window, text="Enter your text :", font=("Times New Roman", 15))
lbl.grid(row=0, column=0)

# Text Widget
txt = Text(window, width=200, height=25, padx=10, pady=10)
txt.grid(row=1, column=0)

# Label timer
lbl_Timer = Label(window, text=MAX_SECONDS_BEFORE_DELETE, font=("Times New Roman", 15))
lbl_Timer.grid(row=2, column=0)

start_timer()

window.mainloop()
