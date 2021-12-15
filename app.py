import requests
import json

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root =tk.Tk()
root.title('Fortune Teller')

canvas = tk.Canvas(root, width=550, height=300)
canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open('icon.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#instructions
instructions = Label(root, text = "What is your destiny?", font="FinkHeavy")
instructions.grid(columnspan=3, column=0, row=1)

#area
canvas = tk.Canvas(root, width=600, height=200)
canvas.grid(columnspan=3)

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

def content(json):
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
    #parameter for HTTP request
    params = (
    ("sign", sign),
    ("day", day))
    #make request
    response = requests.post('https://aztro.sameerkumar.website/', params =params)
    json = response.json()
    #what to print
    #print("\nHoroscope for",json.get('current_date'), "\n")
    #print(json.get('description'), '\n')
    #print('Compatibility:',json.get('compatibility'))
    #print('Mood:', json.get('mood'))
    #print('Color:', json.get('color'))
    #print('Lucky Number:', json.get('lucky_number'))
    #print('Lucky Time:', json.get('lucky_time'),"\n")

    #text box
    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, content(json))
    text_box.grid(column=1, row=5)

#button
button = Button(root,  text='Tell Me', bg ='#af7ac5', font=40, command=lambda:get_horoscope(sign.get(), day.get()))
button.grid(column=1,row=4)





root.mainloop()
