from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    with open("data/to_learn.csv", "r") as data:
        df = pd.read_csv(data)
        dict_language = df.to_dict('records')
except FileNotFoundError:
    with open("data/french_words.csv", "r") as data:
        df = pd.read_csv(data)
        dict_language = df.to_dict('records')


# ---------------------------- Methods ------------------------------------ #
def which_button(button):
    if button == 1:
        dict_language.remove(current_card)
        next_card()
    elif button == 0:
        next_card()
    with open("data/to_learn.csv", "w") as wdata:
        dfw = pd.DataFrame(dict_language)
        dfw.to_csv("data/to_learn.csv", index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_language)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(current_canvas, image=card_f)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(current_canvas, image=card_b)


# ---------------------------- UI Setup ------------------------------------ #
# Window
window = Tk()
window.title("Flashy-dashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Load Images
card_b = PhotoImage(file="images/card_back.png")
card_f = PhotoImage(file="images/card_front.png")
check_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
current_canvas = canvas.create_image(400, 265, image=card_f)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 265, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
known_button = Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: which_button(1))
known_button.grid(row=1, column=0)

unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: which_button(0))
unknown_button.grid(row=1, column=1)

next_card()

window.mainloop()
