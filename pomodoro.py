# pomodoro.py
#
# Python Bootcamp Day 28 - Pomodoro
# Usage:
#      The original technique has six steps:

# 1. Decide on the task to be done.
# 2. Set the pomodoro timer (typically for 25 minutes).
# 3. Work on the task.
# 4. End work when the timer rings and take a short break (typically 5–10
# minutes).
# 5. If you have fewer than three pomodoros, go back to Step 2 and repeat until
# you go through all three pomodoros.
# 6. After three pomodoros are done, take the fourth pomodoro and then take a
# long break (traditionally 20 to 30 minutes). Once the long break is finished,
# return to step 2.
#
# Marceia Egler November 27, 2021

from tkinter import *
import sys

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
TIMER = NONE


def pomodoro_gui():

    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer():
        global REPS
        window.after_cancel(TIMER)
        timer_label.config(text="Timer")
        checks.config(text="")
        canvas.itemconfig(timer_text, text="00:00")
        REPS = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def timer():
        global REPS
        REPS += 1
        work_sec = WORK_MIN * 1
        short_break_sec = SHORT_BREAK_MIN * 1
        long_break_sec = LONG_BREAK_MIN * 1

        if REPS == 8:
            timer_label.config(text="Break", fg=RED)
            countdown(long_break_sec)
        elif REPS % 2 == 0:
            timer_label.config(text="Break", fg=PINK)
            countdown(short_break_sec)
        else:
            timer_label.config(text="Work", fg=GREEN)
            countdown(work_sec)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def countdown(count):
        count_min = count // 60
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            global TIMER
            TIMER = window.after(1000, countdown, count - 1)
        else:
            timer()
            marks = ""
            work_sessions = REPS // 2
            for _ in range(work_sessions):
                marks += "✔"
            checks.config(text=marks)

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    canvas = Canvas(
        width=200,
        height=224,
        bg=YELLOW,
        highlightthickness=0,
    )
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(
        100, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold")
    )

    timer_label = Label(
        text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50)
    )

    start_button = Button(
        bg=YELLOW, relief="flat", overrelief="raised", command=timer
    )
    start_button_img = PhotoImage(file="button_start.png")
    start_button.config(image=start_button_img)

    checks = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)

    reset_button = Button(
        bg=YELLOW, relief="flat", overrelief="raised", command=reset_timer
    )
    reset_button_img = PhotoImage(file="button_reset.png")
    reset_button.config(image=reset_button_img)

    # Layout Grid

    timer_label.grid(column=1, row=0)
    canvas.grid(column=1, row=1)
    start_button.grid(column=0, row=2)
    checks.grid(column=1, row=2)
    reset_button.grid(column=2, row=2)

    window.mainloop()


def main():
    pomodoro_gui()


if __name__ == "__main__":
    sys.exit(main())
