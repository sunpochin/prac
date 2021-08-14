from tkinter import *
from PIL import ImageTk, Image
import requests


def get_quote():
    #Write your code here.
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    print(quote)
    canvas.itemconfig(quote_text, text = quote)
    # return data

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
img1 = Image.open("background2.png")
background_img = ImageTk.PhotoImage(img1)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

img2 = Image.open("kanye.png")
kanye_img = ImageTk.PhotoImage(img2)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()