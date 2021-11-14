# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json

#Get parameters from User

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



print("\nHoroscope for",json.get('current_date'), "\n")
print(json.get('description'), '\n')
print('Compatibility:',json.get('compatibility'))
print('Mood:', json.get('mood'))
print('Color:', json.get('color'))
print('Lucky Number:', json.get('lucky_number'))
print('Lucky Time:', json.get('lucky_time'),"\n")

