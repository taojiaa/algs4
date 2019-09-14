import string

from random import shuffle
from src.sort.Selection import Selection


def sort_test(sort_class):
    array = list(string.ascii_lowercase)
    shuffle(array)
    sc = sort_class()
    sorted_array = sc.sort(array)
    return sc.is_sorted(sorted_array)


class Test:

    def test_selection_sort(self):
        assert sort_test(Selection)
