# local_datetime хранит объект datetime
import pytz
from datetime import datetime
tz = pytz.timezone('UTC')
dt = datetime(year=2018, month=11, day=21, hour=7, second=53, microsecond=507)
local_datetime = dt.astimezone(tz)
my_time_variable = datetime(year=2018, month=11, day=22, hour=7)
result = datetime.combine(local_datetime.date(), my_time_variable.time(),local_datetime.tzinfo)

print(result)
print(local_datetime.timetz())

