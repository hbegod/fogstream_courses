from collections import defaultdict
from datetime import datetime
from collections import Counter
from collections import OrderedDict

simple = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

ordered = OrderedDict(sorted(simple.items(), key=lambda t: t[1]))
print(simple.items())
print(ordered.items())