import requests
import json

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
import subprocess

root =tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open('icon.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#instructions
instructions = tk.Label(root, text = "What is your destiny?", font="FinkHeavy")
instructions.grid(columnspan=3, column=0, row=1)

#Function

#Get Sign
sign = input("Please Enter Your Zodiac Sign (Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius or Pisces): ")

#Get Horoscope Day of Choice
day = input("Please Enter Day of Choice: (Yesterday, Today, or Tomorrow): ")

#parameter for HTTP request
params = (

    ("sign", sign),
    ("day", day))


#make request
response = requests.post('https://aztro.sameerkumar.website/', params =params)
json = response.json()

#what to print
print("\nHoroscope for",json.get('current_date'), "\n")
print(json.get('description'), '\n')
print('Compatibility:',json.get('compatibility'))
print('Mood:', json.get('mood'))
print('Color:', json.get('color'))
print('Lucky Number:', json.get('lucky_number'))
print('Lucky Time:', json.get('lucky_time'),"\n")


#button
browse_text = tk.StringVar()
zodiac_btn = tk.Button(root, textvariable=browse_text, font="FinkHeavy", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Find Out")
zodiac_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
