# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 15:07:51 2025

@author: T-H Nguyen
"""

# install 2 modules datetime, playsound
# pip install pyttsx3: Text-To-Speech
# pip install datetime
# pip install playsound 



# import modules
import pyttsx3
import re
from datetime import datetime
from playsound import playsound

# Set bot
bot = pyttsx3.init()

# Choice of text alarm

options = {
    "1": "It's time to play the violin",
    "2": "It's time to do the homework",
    "3": "It's time to go to school",
    "4": "Personalize"
}

print("Choose an text_alarm :")
for key, value in options.items():
    print(f"{key}: {value}")

while True:
    choice = input("Enter the number of your choice : ")
    
    if choice in options:
        if choice == "4":
            text_alarm = input("Enter text alarm: ")
        else:
            text_alarm = options[choice]
        break
    else:
        print("Invalid choice, please try again.")

n = int(input("Enter the number of repetitions : ")) # Choice the number of repetitions

# Validate time format
def validate_time(alarm_time):
    pattern = r"^(0[1-9]|1[0-2]):([0-5][0-9]):([0-5][0-9])\s?(AM|PM)$"
    if not re.match(pattern, alarm_time):
        return "Invalid time format! Please use 'HH:MM:SS AM/PM'."
    return "ok"

# Set time alarm
while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    validate = validate_time(alarm_time.upper())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break
    
alarm_hour, alarm_min, alarm_sec = alarm_time[:2], alarm_time[3:5], alarm_time[6:8]

alarm_period = alarm_time[9:].upper()


while True:

    now = datetime.now()

    current_hour = now.strftime("%I")

    current_min = now.strftime("%M")

    current_sec = now.strftime("%S")

    current_period = now.strftime("%p")

    if (alarm_period, alarm_hour, alarm_min, alarm_sec) == (current_period, current_hour, current_min, current_sec):
        print("Wake Up!")
        for i in range (n):
            bot.say(text_alarm)
            bot.runAndWait()
        playsound('D:/TKL/8-Data science/1-Python/Exercices/alarme/rock_music_alarm.wav')
        break
