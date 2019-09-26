from src.string.tries import TST, TriesST

from .utils import frequency_counter, read_string_array


class TestTriesST:
    def test_contains(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        frequency_counter(tst, words)
        assert tst.contains('she')

    def test_size(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        frequency_counter(tst, words)
        assert tst.size() == 10

    def test_is_empty(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        assert tst.is_empty()
        frequency_counter(tst, words)
        assert not tst.is_empty()

    def test_get(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        frequency_counter(tst, words)
        assert tst.get('she') == 2

    def test_delete(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        frequency_counter(tst, words)
        tst.delete('she')
        assert tst.get('she') is None
        assert tst.size() == 9

    def test_keys_with_prefix(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        frequency_counter(tst, words)
        q = list(tst.keys_with_prefix('sh'))
        assert q == ['she', 'shells', 'shore']

    def test_keys_that_match(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        frequency_counter(tst, words)
        q = list(tst.keys_that_match('sh.'))
        assert q == ['she']

    def test_longest_prefix_of(self):
        words = read_string_array('files/shells.txt')
        tst = TriesST()
        frequency_counter(tst, words)
        assert tst.longest_prefix_of('shell') == 'she'
        assert tst.longest_prefix_of('shellsort') == 'shells'


class TestTST:
    def test_contains(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        frequency_counter(tst, words)
        assert tst.contains('she')

    def test_size(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        frequency_counter(tst, words)
        assert tst.size() == 10

    def test_is_empty(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        assert tst.is_empty()
        frequency_counter(tst, words)
        assert not tst.is_empty()

    def test_get(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        frequency_counter(tst, words)
        assert tst.get('she') == 2

    def test_delete(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        frequency_counter(tst, words)
        tst.delete('she')
        assert tst.get('she') is None
        assert tst.size() == 9

    def test_keys_with_prefix(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        frequency_counter(tst, words)
        q = list(tst.keys_with_prefix('sh'))
        assert q == ['she', 'shells', 'shore']

    def test_keys_that_match(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        frequency_counter(tst, words)
        q = list(tst.keys_that_match('sh.'))
        assert q == ['she']

    def test_longest_prefix_of(self):
        words = read_string_array('files/shells.txt')
        tst = TST()
        frequency_counter(tst, words)
        assert tst.longest_prefix_of('shell') == 'she'
        assert tst.longest_prefix_of('shellsort') == 'shells'
