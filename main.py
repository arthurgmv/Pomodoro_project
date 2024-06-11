import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass  # Implemente a lógica de reinicialização aqui

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    pass  # Implemente a lógica do mecanismo de tempo aqui

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown():
    pass  # Implemente a lógica do mecanismo de contagem regressiva aqui

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=200, pady=150, bg=YELLOW)
title_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start")
start_button.grid(column=0, row=2)
reset_button = tk.Button(text="Reset")
reset_button.grid(column=2, row=2)
check_marks = tk.Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

#canvas.pack()

window.mainloop()
