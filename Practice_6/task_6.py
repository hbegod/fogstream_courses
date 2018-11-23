from collections import defaultdict
from datetime import datetime
from collections import Counter
from collections import OrderedDict


history = [{'access_date': datetime(year=2018, month=11, day=23).date(), 'access_type': 'READ', 'file_id': 64},
           {'access_date': datetime(year=2018, month=11, day=19).date(), 'access_type': 'READ', 'file_id': 98},
           {'access_date': datetime(year=2018, month=11, day=20).date(), 'access_type': 'WRITE', 'file_id': 28},
           {'access_date': datetime(year=2018, month=11, day=23).date(), 'access_type': 'WRITE', 'file_id': 49},
           {'access_date': datetime(year=2018, month=11, day=25).date(), 'access_type': 'WRITE', 'file_id': 35},
           {'access_date': datetime(year=2018, month=11, day=19).date(), 'access_type': 'WRITE', 'file_id': 3},
           {'access_date': datetime(year=2018, month=11, day=19).date(), 'access_type': 'WRITE', 'file_id': 7},
           {'access_date': datetime(year=2018, month=11, day=26).date(), 'access_type': 'CREATE', 'file_id': 81},
           {'access_date': datetime(year=2018, month=11, day=22).date(), 'access_type': 'CREATE', 'file_id': 13},
           {'access_date': datetime(year=2018, month=11, day=26).date(), 'access_type': 'CREATE', 'file_id': 39},
           {'access_date': datetime(year=2018, month=11, day=24).date(), 'access_type': 'CREATE', 'file_id': 83},
           {'access_date': datetime(year=2018, month=11, day=23).date(), 'access_type': 'WRITE', 'file_id': 85},
           {'access_date': datetime(year=2018, month=11, day=19).date(), 'access_type': 'READ', 'file_id': 59},
           {'access_date': datetime(year=2018, month=11, day=22).date(), 'access_type': 'CREATE', 'file_id': 27},
           {'access_date': datetime(year=2018, month=11, day=26).date(), 'access_type': 'CREATE', 'file_id': 51},
           {'access_date': datetime(year=2018, month=11, day=19).date(), 'access_type': 'WRITE', 'file_id': 90},
           {'access_date': datetime(year=2018, month=11, day=21).date(), 'access_type': 'CREATE', 'file_id': 2}]


first_dict = defaultdict(list)
second_dict = {}
for file_access_obj in history:
    access_date, access_type = file_access_obj['access_date'], file_access_obj['access_type']
    first_dict[access_date].append(access_type)
for key, element in first_dict.items():
    second_dict.setdefault(key, dict(Counter(element)))
ordered_dict = OrderedDict(sorted(second_dict.items(), key=lambda t: t[0]))
result = ordered_dict
