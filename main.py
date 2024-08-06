
BACKGROUND_COLOR = "#B1DDC6"
import tkinter as tk
import pandas as pd
import random


try:
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")



#------Next Card-----#
def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background , image=card_front)
    flip_timer = window.after(3000,func=flip_card)


#------Flip Card-----#
def flip_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title , text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background , image=card_back)

#-------IS KNOWN---------#
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()



 
#--------UI SETUP---------#
window=tk.Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#3 saniye delay vermesini sağlıyor ve fonksiyona gidiyor süre bittikten sonra
flip_timer = window.after(3000, func=flip_card)

#Card_Front_Image 
canvas=tk.Canvas(width=800,height=526)

card_front =tk.PhotoImage(file="image/card_front.png")
card_back = tk.PhotoImage(file="image/card.back.png")

card_background = canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title= canvas.create_text(400,150,"French",font=("ariel",40,"italic"))
card_word = canvas.create_text(400,263,"word",font=("ariel",60 ,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#Buttons
check_image=tk.PhotoImage(file="image/right.png")
true_button=tk.Button(text=check_image , command=next_card)
true_button.grid(row=1,column=1)



cross_image=tk.PhotoImage(file="image/wrong.png")
false_button=tk.Button(text=cross_image,command=is_known)
false_button.grid(row=1,column=0)


next_card()

window.mainloop()