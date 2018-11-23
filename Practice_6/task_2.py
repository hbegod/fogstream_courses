# just_datetime хранит объект datetime
import pytz
import copy
from datetime import datetime
from datetime import timedelta


def get_datetime(datetime_obj):
    func_datetime_obj = copy.copy(datetime_obj)
    if func_datetime_obj.date() == datetime.now().date():
        delta = timedelta(days=1, hours=3, minutes=15)
        func_datetime_obj = func_datetime_obj - delta
    return func_datetime_obj

result = get_datetime(datetime.now())
print(result)




