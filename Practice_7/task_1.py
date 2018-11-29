import itertools


data_list_iter = ('a', 'b', 'c')  # `data_list_iter` содержит генератор


result = dict(zip(itertools.count(start=0, step=2), data_list_iter))
