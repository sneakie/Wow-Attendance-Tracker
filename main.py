import tkinter
from tkinter import *
import gspread
import os
from tkinter import ttk
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import tkinter as tk
import json
import string
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
# access the json key you downloaded earlier
credentials = ServiceAccountCredentials.from_json_keyfile_name("PythonSheetsTestKey.json", scopes)
# authenticate the JSON key with gspread
file = gspread.authorize(credentials)
# open sheet
sheet = file.open("PythonAppTest")
sheet_instance = sheet.sheet1
# list with data
all_values = sheet_instance.get_all_values()
rows = sheet_instance.get()

top = tk.Tk()

# dropdown menu option
dp_options = [
    "Accepted",
    "Absent",
    "Benched",
    "Planned Absence"
]
# List used for Position variable
letter_List = [
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    # "P",
    # "Q",
    # "R",
    # "S",
    # "T",
    # "U",
    # "V",
    # "W",
    # "X",
    # "Y",
    # "Z"
]


def dp(row, col):
    position = col+str(row)
    sheet_instance.update_acell(position, "trimmus is cute")
    return


def position(position):
    for letter in letter_List:
        position = letter
        return


def label_name():
    row = 0
    for label_name in all_values:
        row += 1
        var = StringVar()
        label = Label(top, textvariable=var, font=25)
        var.set(label_name[0])
        label.grid(row=row)
        # print(label_name[0])


def label_date():
    column = 0
    # var = StringVar()
    # var.set(rows[0][7:14])
    for label_date in all_values[0][7:25]:
        column += 1
        var = StringVar()
        label2 = Label(top, textvariable=var, relief=RAISED, font=25)
        var.set(label_date)
        label2.grid(column=column, row=1)

        # label_date[0][7:14]
        # print(all_values[0][7:14])
        # print(rows[0][7:14])


# Maybe useless variables
number = 2

# function that creates buttons
def start():
    for i in range(2, 8):
        column = 0
        for letter in letter_List:
            column += 1
            mybutton = Button(top, height=2, width=5, text=f"{letter}{i}", command=lambda row=i, col=letter: dp(row, col))
            mybutton.grid(column=column, row=i, pady=3, padx=2)


label_date()
label_name()
start()
print("debug for git 3")
top.mainloop()
