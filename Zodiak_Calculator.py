# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:28:08 2021

@author: Kathryn
"""

#make calculator

#find out birthdate

month = input("What month were you born? ")

day = int(input("What day were you born? "))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#sign = "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius" ,"Pisces"

if month in months:
    if month == "March":
        sign = "Pisces" if (day < 21) else "Aries"
    elif month == "April":
        sign = "Aries" if (day < 20) else "Taurus"
    elif month == "May":
        sign = "Taurus" if (day < 21) else "Gemini"
    elif month ==  "June":
        sign = "Gemini" if (day < 21) else "Cancer"
    elif month == "July":
        sign = "Cancer" if (day < 23) else "Leo"
    elif month == "August":
        sign = "Leo" if (day < 23) else "Virgo"
    elif month == "September":
        sign = "Virgo" if (day < 23) else "Libra"
    elif month == "October":
        sign = "Libra" if (day < 23) else "Scorpio"
    elif month == "November":
        sign = "Scorpio" if (day < 22) else "Sagittarius"
    elif month == "December":
        sign = "Sagittarius" if (day < 22) else "Capricorn"
    elif month == "January":
        sign = "Capricorn" if (day < 20) else "Aquarius"
    elif month == "February":
        sign = "Aquarius" if (day < 19) else "Pisces"

print ("Your zodiac sign is " + sign + ".")

input('Press ENTER to exit')