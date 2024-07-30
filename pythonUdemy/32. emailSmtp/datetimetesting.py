import datetime as dt

now = dt.datetime.now()
year = now.year
weekday = now.weekday()

# storing out specific date as object 
mybirthday = dt.datetime(year=2002, month=5, day=17, hour=8, minute=37)
print(mybirthday)