from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
LANGUAGE = "German"
FILE_LANGUAGE = "german"

#----------------------------------------HANDLING DATA---------------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(f"data/{FILE_LANGUAGE}_words.csv")

to_learn = data.to_dict(orient="records")
word = {}

def new_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    canvas.itemconfig(card_image, image=flashcard_front_img)
    canvas.itemconfig(card_title, text=LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=word[LANGUAGE], fill="black")
    flip_timer = window.after(3000, func=flip_card)

#------------------------------------------FLIP CARD-----------------------------------------#
def flip_card():
    canvas.itemconfig(card_image, image=flashcard_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")
    
#--------------------------------------HANDLING CORRECT----------------------------------------#
def right_word():
    to_learn.remove(word)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_word()

#-----------------------------------------UI SETUP-------------------------------------------#
window = Tk()
window.title("Flashy Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#create flashcard canvas
canvas = Canvas(width=800, height=526)
flashcard_front_img = PhotoImage(file="images/card_front.png")
flashcard_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=flashcard_front_img)
card_title = canvas.create_text(400, 150, font=TITLE_FONT)
card_word = canvas.create_text(400, 263, font=WORD_FONT)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

#buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right_word)
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

new_word()

window.mainloop()
