import datetime as dt
from emailtesting import sendmail
import random as rd

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1 :
    with open("quotes.txt","r") as quotes:
        allquotes = quotes.readlines()
        quote = rd.choice(allquotes)
    sendmail(
        frm="gillolahemavardhanreddy@gmail.com", 
        to="balabittu1143@gmail.com", 
        subject="Monday Motivation", 
        body = quote
    )