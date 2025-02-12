from datetime import date, timedelta
today = date.today()
print("Today:", today)
new = today - timedelta(days = 5)
print("after 5 days", new)
