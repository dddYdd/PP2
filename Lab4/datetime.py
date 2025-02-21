from datetime import datetime, date, timedelta

current_datetime = datetime.now()
five_days_ago = current_datetime - timedelta(days=5)
print(current_datetime)
print(five_days_ago)

today_date = date.today()
yesterday = today_date - timedelta(days=1)
tomorrow = today_date + timedelta(days=1)
print(yesterday)
print(today_date)
print(tomorrow)

now_with_micro = datetime.now()
now_without_micro = now_with_micro.replace(microsecond=0)
print(now_with_micro)
print(now_without_micro)

date1 = datetime.now()
date2 = date1 - timedelta(days=2, hours=3)
difference = date1 - date2
seconds_diff = difference.total_seconds()
print(date1)
print(date2)
print(seconds_diff)
