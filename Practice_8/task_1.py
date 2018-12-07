from collections import Counter
import os.path

dir_list = ['/dir1/./dir0/dir0/../dir0/..', '/dir1/dir2/', '/dir1/dir2/', '/dir0/./dir2/./.', '/dir0/dir1/dir1/../.',
            '/dir2/dir2/../dir2/../dir0/dir0/.././dir0/..', '/dir1/dir1/../dir0/.', '/dir0/dir2/./.',
            '/dir2/dir2/../dir0/', '/dir0/dir2/.', '/dir0/./dir1/./.', '/dir2/./dir2/../dir0/dir0/..',
            '/dir1/./dir1/../dir2/dir2/../dir2/../dir2/..', '/dir1/./dir1/../dir1/../dir2/dir2/../.',
            '/dir0/dir0/../dir1/dir1/../.', '/dir1/dir1/../dir2/dir2/../dir2/../.', '/dir2/dir1/',
            '/dir2/dir1/./dir1/../dir1/..', '/dir1/./dir0/dir0/..', '/dir1/./dir0/./.',
            '/dir1/./dir1/../dir0/dir0/../dir0/../.', '/dir0/./dir0/../dir0/../dir2/', '/dir2/dir1/dir1/../dir1/..',
            '/dir1/dir0/', '/dir0/dir1/./dir1/..', '/dir2/././dir2/../dir1/.', '/dir2/dir2/../dir2/../dir2/../dir1/',
            '/dir2/././dir0/./.', '/dir0/./dir1/./.', '/dir2/./dir2/../dir2/../dir1/', '/dir2/./dir1/', '/dir1/dir0/',
            '/dir1/dir1/../dir2/./.', '/dir0/dir0/../dir1/dir1/.././.', '/dir0/dir2/.',
            '/dir1/dir1/../dir1/../dir1/../dir0/dir0/../.', '/dir2/dir2/../dir0/',
            '/dir2/./dir2/.././dir1/dir1/.././dir1/..', '/dir1/dir0/dir0/../dir0/../dir0/..',
            '/dir0/dir2/dir2/../dir2/..', '/dir2/dir2/../././dir1/././.', '/dir0/./dir0/../dir2/./.',
            '/dir0/dir1/dir1/../.', '/dir0/dir1/dir1/../dir1/..'
            ]


def count_unique_path(directories_list):
    """
    Normalizes paths and return number of unique paths
    :param directories_list: list with dirs
    :return: int number of unique
    """
    normalised_list = []
    for path in directories_list:
        normalised_list.append(os.path.abspath(path))
    return len(Counter(normalised_list).keys())


result = count_unique_path(dir_list)
print(result)


