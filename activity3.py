from datetime import datetime, timedelta

bday_date = datetime(1985, 7 ,30)
new_date = datetime.today() - bday_date
print (new_date.days)