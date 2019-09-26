from src.string.sort_string import LSD, MSD, Quick3String

from .utils import read_string_array


class TestLSD:

    def test_sort(self):
        a = read_string_array('files/words.txt')
        lsd = LSD()
        sa = lsd.sort(a, 3)
        assert lsd.is_sorted(sa)


class TestMSD:
    def test_sort(self):
        a = read_string_array('files/shells.txt')
        msd = MSD()
        sa = msd.sort(a)
        assert msd.is_sorted(sa)


class TestQuick3String:
    def test_sort(self):
        a = read_string_array('files/shells.txt')
        q = Quick3String()
        sa = q.sort(a)
        assert q.is_sorted(sa)
