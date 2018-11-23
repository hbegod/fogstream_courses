# local_datetime хранит объект datetime
import pytz
from datetime import datetime

tz = pytz.timezone('Etc/GMT-11')
tz_moscow = pytz.timezone('Europe/Moscow')
dt = datetime(year=2018, month=11, day=23, hour=15, minute=14, second=42, microsecond=437)
just_datetime = dt.astimezone(tz)
result = just_datetime.astimezone(tz_moscow)

print(just_datetime)
print(result)

