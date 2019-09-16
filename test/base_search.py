import string

from .utils import ascii_generator, frequency_counter


def initiate(st_class):
    words = ascii_generator()
    st = st_class()
    frequency_counter(st, words)
    return st


class SortedSymbolTableTest:

    def test_contains(self, test_class):
        st = initiate(test_class)
        assert st.contains('z')

    def test_size(self, test_class):
        st = initiate(test_class)
        assert st.size() == 26

    def test_keys(self, test_class):
        st = initiate(test_class)
        assert st.keys() == list(string.ascii_lowercase)

    def test_get(self, test_class):
        st = initiate(test_class)
        assert st.get('a') == 1
        assert st.get('z') == 26

    def test_rank(self, test_class):
        st = initiate(test_class)
        assert st.rank('a') == 0
        assert st.rank('aa') == 1
        assert st.rank('z') == 25
        assert st.rank('zz') == 26

    def test_select(self, test_class):
        st = initiate(test_class)
        assert st.select(0) == 'a'
        assert st.select(3) == 'd'
        assert st.select(25) == 'z'

    def test_min(self, test_class):
        st = initiate(test_class)
        assert st.min() == 'a'

    def test_max(self, test_class):
        st = initiate(test_class)
        assert st.max() == 'z'

    def test_delete_min(self, test_class):
        st = initiate(test_class)
        st.delete_min()
        assert st.get('a') is None
        assert st.size() == 25

    def test_delete_max(self, test_class):
        st = initiate(test_class)
        st.delete_max()
        assert st.get('z') is None
        assert st.size() == 25

    def test_delete(self, test_class):
        st = initiate(test_class)
        st.delete('m')
        st.delete('z')
        assert st.get('m') is None
        assert st.get('z') is None
        assert st.size() == 24

    def test_floor(self, test_class):
        st = initiate(test_class)
        assert st.floor('m') == 'm'
        assert st.floor('mm') == 'm'

    def test_ceiling(self, test_class):
        st = initiate(test_class)
        assert st.ceiling('m') == 'm'
        assert st.ceiling('mm') == 'n'

    def test_range_keys(self, test_class):
        st = initiate(test_class)
        assert st.range_keys('a', 'z') == list(string.ascii_lowercase)
        assert st.range_keys('aa', 'ya') == list(string.ascii_lowercase)[1:-1]

    def test_range_size(self, test_class):
        st = initiate(test_class)
        assert st.range_size('a', 'z') == 26
        assert st.range_size('aa', 'ya') == 24

    def test_getitem(self, test_class):
        st = initiate(test_class)
        assert st.get('a') == st['a']

    def test_setitem(self, test_class):
        st = initiate(test_class)
        st['a'] = 26
        assert st.get('a') == 26


class UnSortedSymbolTableTest:

    def test_contains(self, test_class):
        st = initiate(test_class)
        assert st.contains('z')

    def test_size(self, test_class):
        st = initiate(test_class)
        assert st.size() == 26

    def test_keys(self, test_class):
        st = initiate(test_class)
        assert set(st.keys()) == set(list(string.ascii_lowercase))

    def test_get(self, test_class):
        st = initiate(test_class)
        assert st.get('a') == 1
        assert st.get('z') == 26

    def test_delete(self, test_class):
        st = initiate(test_class)
        st.delete('m')
        st.delete('z')
        assert st.get('m') is None
        assert st.get('z') is None
        assert st.size() == 24
