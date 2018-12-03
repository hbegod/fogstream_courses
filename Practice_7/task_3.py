import itertools
import collections

responses = [[{'hash': UUID('c9bf907e-4fc1-404f-bca1-2336f1c7d82e'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 9, 4, 20, 317522)},
              {'hash': UUID('1b3c498d-0ee0-4a9e-82bc-bcbbf2dd1beb'), 'log': 'STATUS2', 'time': datetime.datetime(2018, 11, 28, 5, 33, 20, 317558)},
              {'hash': UUID('bb80d8b0-8f53-49a9-ba0e-09fca64d463a'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 3, 48, 20, 317570)},
              {'hash': UUID('f382ae53-d693-4e84-a247-1c3fea153c62'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 8, 39, 20, 317580)},
              {'hash': UUID('c9bf907e-4fc1-404f-bca1-2336f1c7d82e'), 'log': 'STATUS3', 'time': datetime.datetime(2018, 11, 28, 9, 42, 20, 317591)}
              ],
             [
                 {'hash': UUID('b6c175f7-d3b5-4103-a79a-4448a8f26d16'), 'log': 'STATUS3', 'time': datetime.datetime(2018, 11, 28, 4, 59, 20, 317601)},
                 {'hash': UUID('a9a4bd9c-fc0b-4233-8209-734e70e95fb7'), 'log': 'STATUS3', 'time': datetime.datetime(2018, 11, 28, 5, 53, 20, 317612)},
                 {'hash': UUID('393bf353-3552-464e-a958-7462d7a5bd2d'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 4, 19, 20, 317682)},
                 {'hash': UUID('7bc2aeb6-f8ed-490a-bd82-c653730feac5'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 9, 17, 20, 317697)},
                 {'hash': UUID('8be850a4-dbcc-41c1-ab25-356b52d16b89'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 5, 4, 20, 317707)},
                 {'hash': UUID('34dc44f4-dec7-4286-aca7-aacf6bbb7688'), 'log': 'STATUS2', 'time': datetime.datetime(2018, 11, 28, 7, 35, 20, 317718)},
                 {'hash': UUID('1b3c498d-0ee0-4a9e-82bc-bcbbf2dd1beb'), 'log': 'STATUS3', 'time': datetime.datetime(2018, 11, 28, 5, 17, 20, 317728)},
                 {'hash': UUID('6d6dcf92-0500-451f-8d74-cc5c93872c29'), 'log': 'STATUS2', 'time': datetime.datetime(2018, 11, 28, 8, 21, 20, 317738)},
                 {'hash': UUID('a9a4bd9c-fc0b-4233-8209-734e70e95fb7'), 'log': 'STATUS2', 'time': datetime.datetime(2018, 11, 28, 8, 0, 20, 317749)},
                 {'hash': UUID('c9bf907e-4fc1-404f-bca1-2336f1c7d82e'), 'log': 'STATUS2', 'time': datetime.datetime(2018, 11, 28, 9, 36, 20, 317760)},
                 {'hash': UUID('c9bf907e-4fc1-404f-bca1-2336f1c7d82e'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 2, 27, 20, 317771)},
                 {'hash': UUID('c9bf907e-4fc1-404f-bca1-2336f1c7d82e'), 'log': 'STATUS1', 'time': datetime.datetime(2018, 11, 28, 3, 8, 20, 317781)},
                 {'hash': UUID('5648e44c-7d94-4c0d-819a-e602eccb4908'), 'log': 'STATUS2', 'time': datetime.datetime(2018, 11, 28, 10, 33, 20, 317792)}
             ]]


def sort_users(responses):
    return {'c9bf907e-4fc1-404f-bca1-2336f1c7d82e':'STATUS1', '1b3c498d-0ee0-4a9e-82bc-bcbbf2dd1beb':'STATUS2'}


result = sort_users(responses)