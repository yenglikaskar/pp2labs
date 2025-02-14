#1
from datetime import date, timedelta
today = date.today()
print("Today:", today)
new = today - timedelta(days = 5)
print("after 5 days ", new)


#2
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3
from datetime import datetime
now = datetime.now()
without = now.replace(microsecond = 0)
print("With:", now)
print("Without:", without)


#4
from datetime import datetime
def in_seconds(d1, d2):
    format = "%Y-%m-%d %H:%M:%S"
    dt1 = datetime.strptime(d1, format)
    dt2 = datetime.strptime(d2, format)
    difference = abs((dt2 - dt1).total_seconds())
    return difference

d1 = input("first date: ")
d2 = input("second date: ")

diff = in_seconds(d1, d2)
print(f"Difference {diff} seconds")
