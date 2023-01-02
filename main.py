from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIDGET_PADX = 20
WIDGET_PADY = 20
reps = 1
countdown = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(countdown)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_secs)
        reps += 1
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_secs)
        reps += 1
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_secs)
        reps += 1
        check_marks.config(text="✔" * int(reps / 2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global countdown
    minutes = int(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        countdown = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=50, bg=YELLOW)

# tomato image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1, padx=WIDGET_PADX, pady=WIDGET_PADY)

# timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 38, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=0)

# reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=2)

# check mark
check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_marks.grid(row=4, column=1)

window.mainloop()
