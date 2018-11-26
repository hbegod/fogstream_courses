import pytz
from datetime import datetime

# local_datetime хранит объект datetime

tz = pytz.timezone('Etc/GMT-11')
dt = datetime(year=2018, month=11, day=23, hour=15, minute=14, second=42, microsecond=437)
just_datetime = dt.astimezone(tz)


def convert_datetime_to_moscow_tz(datetime_input):
    tz_moscow = pytz.timezone('Europe/Moscow')
    return datetime_input.astimezone(tz_moscow)


result = convert_datetime_to_moscow_tz(just_datetime)

print(result)

