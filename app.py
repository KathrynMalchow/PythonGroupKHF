import requests
import json
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#start GUI
root =tk.Tk()
root.title('Fortune Teller')

#area of GUI
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('icon.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#caption
instructions = Label(root, text = "What is your destiny? Select your Zodiac Sign and Day of Choice", font="Harrington")
instructions.grid(columnspan=3, column=0, row=1)

#dropdown list for zodiac sign
data_sign={
     "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
}

sign = tk.StringVar()
sign.set("Zodiac Sign")

s = OptionMenu(root, sign, *data_sign)
s.grid(column=1, row=2)

#dropdown list for day options
data_day={
     "Yesterday", "Today", "Tomorrow"
    }

day = tk.StringVar()
day.set("Day")

d = OptionMenu(root, day, *data_day)
d.grid(column=1, row=3)

#function to format response
def content(json):
    """Calls aspects of horoscope from API and formats them into an answer
    Args:
        get_horoscope function variable
    Returns:
        final_sr horoscope paragraph
    """
    date = json.get('current_date')
    descr = json.get('description')
    compat = json.get('compatibility')
    mood = json.get('mood')
    color = json.get('color')
    number = json.get('lucky_number')
    time = json.get('lucky_time')

    final_sr = 'Horoscope for: %s \nFortune: %s \nCompatibility: %s \nMood: %s \nLucky ''Color: %s \nLucky ''Number: %s \nLucky ''Time: %s' % (date, descr, compat, mood, color, number, time)

    return final_sr

#use API as function
def get_horoscope(sign, day):
    """Sends an HTTP resquest to Aztro API
    Args:
        params
        request.post url
        response.json
    Returns:
        variable named json that represents user's selection of sign and day
    """
    #parameter for HTTP request
    params = (
    ("sign", sign),
    ("day", day))
    #make request
    response = requests.post('https://aztro.sameerkumar.website/', params =params)
    json = response.json()


    #text box
    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, content(json))
    text_box.grid(column=1, row=5)

#button
button = Button(root,  text='Tell Me', bg ='#af7ac5', font="Harrington", height=2, width=10, command=lambda:get_horoscope(sign.get(), day.get()))
button.grid(column=1,row=4)


#end GUI
root.mainloop()
