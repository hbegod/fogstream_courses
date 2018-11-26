from datetime import datetime

datetime_string = '17:34:12 21-11-2018'      # datetime_string хранит строку даты и времени


def convert_string_to_iso_datetime(string):
    my_datetime_var = datetime.strptime(string, '%H:%M:%S %d-%m-%Y')
    return my_datetime_var.isoformat()


result = convert_string_to_iso_datetime(datetime_string)
print(result)
