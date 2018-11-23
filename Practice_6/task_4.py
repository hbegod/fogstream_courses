datetime_string = '17:34:12 21-11-2018'      # datetime_string хранит строку даты и времени
from datetime import datetime
my_datetime_var = datetime.strptime(datetime_string, '%H:%M:%S %d-%m-%Y')
result = my_datetime_var.isoformat()
print(result)