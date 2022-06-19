# IMPORTING LIBRARIES
import tkinter
import requests

# CONSTANTS
KANYE_API_ENDPOINT = "https://api.kanye.rest/"
KANYE_IMAGE = "images/kanye.png"
BACKGROUND_IMAGE = "images/background.png"


# GET QUOTE
def get_quote():
    response = requests.get(KANYE_API_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
    return


# UI SETUP
window = tkinter.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# CANVAS
canvas = tkinter.Canvas(width=300, height=414)
background_img = tkinter.PhotoImage(file=BACKGROUND_IMAGE)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="black",
)
canvas.grid(row=0, column=0)

# KANYE IMAGE BUTTON
kanye_img = tkinter.PhotoImage(file=KANYE_IMAGE)
kanye_button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
