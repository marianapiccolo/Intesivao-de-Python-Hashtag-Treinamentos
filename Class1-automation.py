#!/usr/bin/env python
# coding: utf-8

"""

*Python Intensive*

Class 1: 

Problem: Sales report that needs to be sent to a board daily. This task it's repetitive and not adds value to the process.
Solution: Create an automation code for data analysis and elaboration of reports.
The information that will feed our code will be given referring to sales of various products from different stores.

Drive with classes and files:
https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga

Libraries:
Pyautogui - allows us to create code that simulates that we are using the computer.
Pyperclip: Allows you to copy and paste via Python. 
Time: Makes code development easier involving time, waiting time, etc...;
Pandas: Data analysis.

IDE: Jupyter Notebook

Steps:
Step 1: Enter into the company system (drive link).
Step 2: Browse the system and find database.
Step 3: Download the database.
Step 4: Import the database into Python.
Step 5: Calculate the indicators. Valor Final = Final value.
Step 6: Send an email to the manager with the report.


Course given by: https://www.hashtagtreinamentos.com/

"""

#!pip install pyautogui
#!pip install pyperclip

import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1


# Step 1: Enter into the company system (drive link)

pyautogui.hotkey("ctrl", "t") #hotkey simulates the keys I pressed # ctrl + t = open a new tab
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga") #when there is special character. Copy = store the value of the variable in memory
pyautogui.hotkey("ctrl", "v") 
pyautogui.press("enter")

time.sleep(5) #wait 5 seconds


# Step 2: Browse the system and find database
#it's necessary to find the position of the button on the screen using the command pyautogui.position() and then place them in x and y

pyautogui.click(x=579, y=451, clicks=2)
time.sleep(2)

# Step 3: Download the database

pyautogui.click(x=532, y=582) # click on the file
pyautogui.click(x=1624, y=288) # click on 3 points
pyautogui.click(x=1255, y=897) # click on download
time.sleep(5)

# Step 4: Import the database into Python

df = pd.read_excel(r'location on the computer where the file was downloaded')
display(df)
# r' indicates that the text is a raw string. That is, without special characters

# Step 5: Calculate the indicators. Valor Final = Final value. 

revenue = df['Valor Final'].sum()
quantity_of_products = df['Quantidade'].sum()

# Step 6: Send an email to the manager with the report

#1) OPEN the gmail;
pyautogui.hotkey('ctrl', 't')
pyautogui.write("mail.google.com")
pyautogui.press('enter')
time.sleep(5)

#2) Click on WRITE (new e-mail);
pyautogui.click(153,319)
time.sleep(1)

#3) write the RECIPIENT;
pyautogui.write("email@gmail.com") # fill in the e-mail
time.sleep(1)

#4) Selectc the SUBJECT field;
pyautogui.press('tab') # 2X. Switch to subject field
pyautogui.press('tab')
subject = "Yesterday's Sales Report"
pyperclip.copy(subject) 
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

#5) Selectthe field BODY OF E-MAIL and write the e-email using the bookmarks calculated;

#(:) indicates that there will be a formatting. (,) indicates that the separator thousands will be COMMA. 
# (.2f) indicates that the place separator decimals will be POINT and will be 2 decimal places.

pyautogui.press('tab')
text = f"""
Dears, good morning!
Yesterday's turnover was: ${revenue:,.2f} 
The quantity of products was: ${quantity_of_products:,}

Sincerely,
Mariana"""

#6) SEND e-email;
pyperclip.copy(text)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')

#Finished!

# find mouse position
#time.sleep(5) #wait 5 seconds
#pyautogui.position() #position of my computer

