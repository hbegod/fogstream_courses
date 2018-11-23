time_shift = 12 # time_shift хранит число дней сдвига
from datetime import datetime
from datetime import timedelta
now_date = datetime.now().date()
day_delta = timedelta(days=time_shift)
result_date = now_date + day_delta
print(now_date)
print(result_date)
result = result_date.isocalendar()[1]
print(result)
