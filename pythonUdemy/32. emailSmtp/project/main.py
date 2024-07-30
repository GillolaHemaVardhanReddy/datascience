# --------------------------------------------- IMPORTS ------------------------------------------------ #
import pandas as pd
import datetime as dt
import random as rd
from emaillogic import sendmail

# ------------------------------------------ LETTER SELECTION ------------------------------------------ #
def selectletter():
    num = rd.randint(1,3)
    return f"letter_{num}.txt"

# ------------------------------------------ CSV SELECTION ------------------------------------------ #
file = pd.read_csv("birthdays.csv")
birthdays = file.to_dict(orient="records")
date = dt.datetime.now()
month = date.month
day = date.day
for item in birthdays:
    name = item["name"]
    email = item["email"]
    if day == item["day"] and month == item["month"] :
        lettername = selectletter()
        with open("./letter_templates/"+lettername,"r+") as letter:
            content = letter.read()
            content = content.replace("[NAME]",name)
            sendmail(
                frm="gillolahemavardhanreddy@gmail.com", 
                to=email, 
                subject="Birthday wishes",
                body = content
            )