import itertools

data_list_iter = ('j', 's', 'f', 'y', 'd', 'q', 'o', 'k', 'f', 'i', 'f')  # `data_list_iter` содержит генератор

result = dict(zip(itertools.count(start=0, step=2), data_list_iter))
print(result, '\n')


