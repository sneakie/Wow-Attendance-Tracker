import tkinter
from pprint import pprint
import tkinter as tk
from tkinter import *
from tkinter import ttk
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


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

# Changing main window attributes
top.title("Voljin & Tonic Attendance")
top.geometry("1920x1080")
top.configure(bg="grey")


# dropdown menu option
dp_options = [
    "Accepted",
    "Absent",
    "Benched",
    "Vacation",
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
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

dp_name = [


]

dp_name_pos = [

]


# Dropdown command function (row, col in dp if changing)
def dp(status, p):
    print(status)
    print(p)
    sheet_instance.update_acell(p, status)
    return

# Name's of players in A Column
def label_name():
    row = 0
    for labelName in all_values:
        row += 1
        var = StringVar()
        label = Label(top, textvariable=var, font=("Helvetica 9 bold"), anchor="w", width=12)
        var.set(labelName[0])
        label.config(bg="lightgrey")
        label.grid(row=row)


# All the dates in row 0 (excluding A-G Column)
def label_date():
    column = 0
    for labelDate in all_values[0][7:29]:
        column += 1
        var = StringVar()
        label2 = Label(top, textvariable=var, relief=FLAT, font=("Helvetica 16 bold"), bg="lightgrey")
        var.set(labelDate)
        label2.grid(column=column, row=1)


# Function that fills the dp_name list with appropriate names from the Google sheet
def dp_row(p):
    row = sheet_instance.row_values(p)
    for pos in row[7:29]:
        dp_name.append(pos)


# function that creates dropdowns & names them correctly
def start():
    o = -1
    for i in range(2, 29):
        column = 0
        for letter in letter_List:
            pos = f"{letter}{i}"
            column += 1
            o += 1
            menu_op = StringVar()
            menu_op.set(dp_name[o])
            dropdown = OptionMenu(top, menu_op, *dp_options, command=lambda status=dp_options,
                                                                            p=pos: dp(status, p))
            dropdown.grid(column=column, row=i, pady=1, padx=1)
            dropdown.configure(font=("Helvetica 10 bold"), activebackground="Gray", activeforeground="Black", bg="Gray",
                               fg="Black", highlightthickness=0, width=7)
            if dp_name[o] == "Accepted":
                dropdown.config(bg="Green")
            elif dp_name[o] == "Absent":
                dropdown.config(bg="Red")
            elif dp_name[o] == "Vacation":
                dropdown.config(bg="cyan")
            elif dp_name[o] == "Benched":
                dropdown.config(bg="Orange")


# Actual code running
for i in range(2, 29):
    p = i
    dp_row(p)

label_date()
label_name()
start()


top.mainloop()
