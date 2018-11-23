# local_datetime хранит объект datetime
import pytz
from datetime import datetime
tz = pytz.timezone('UTC')
dt = datetime(year=2018, month=11, day=21, hour=7, second=53, microsecond=507)
local_datetime = dt.astimezone(tz)


def combine_date_time(datetime_obj):
    my_time_variable = datetime(year=2018, month=11, day=22, hour=7)
    return datetime.combine(datetime_obj.date(), my_time_variable.time(), datetime_obj.tzinfo)


result = combine_date_time(local_datetime)

print(result)
print(local_datetime.timetz())

