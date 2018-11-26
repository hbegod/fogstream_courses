from datetime import datetime
from datetime import timedelta

time_shift = 12  # time_shift хранит число дней сдвига


def shift_days(days):
    """
    Function adds days to now_date and return result as number of week in which result date was
    :param days:
    :return: number of week
    """
    now_date = datetime.now().date()
    day_delta = timedelta(days=days)
    result_date = now_date + day_delta
    return result_date.isocalendar()[1]


result = shift_days(time_shift)
print(result)

