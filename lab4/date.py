from datetime import date, timedelta
today = date.today()
print("Today:", today)
new = today - timedelta(days = 5)
print("after 5 days ", new)



yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


from datetime import datetime
now = datetime.now()
without = now.replace(microsecond = 0)
print("With:", now)
print("Without:", without)
