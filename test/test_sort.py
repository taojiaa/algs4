import string

from random import shuffle
from src.sort.Selection import Selection
from src.sort.Insertion import Insertion, Shells
from src.sort.Merge import Merge, MergeBU, MergeX
from src.sort.Quick import Quick, QuickX


def sort_test(sort_class):
    array = list(string.ascii_lowercase) * 2
    shuffle(array)
    sc = sort_class()
    sorted_array = sc.sort(array)
    return sc.is_sorted(sorted_array)


class Test:

    def test_selection_sort(self):
        assert sort_test(Selection)

    def test_insertion_sort(self):
        assert sort_test(Insertion)

    def test_shells_sort(self):
        assert sort_test(Shells)

    def test_merge_sort(self):
        assert sort_test(Merge)

    def test_mergebu_sort(self):
        assert sort_test(MergeBU)

    def test_mergex_sort(self):
        assert sort_test(MergeX)

    def test_quick_sort(self):
        assert sort_test(Quick)

    def test_quickx_sort(self):
        assert sort_test(QuickX)
