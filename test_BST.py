import string
from random import shuffle

from search.BST import BST

test_class = BST


def file_reader(file_name='./test/test.txt'):
    words = []
    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                words.append(word)
    return word


def frequency_counter(st, words, min_len=0):
    for word in words:
        if len(word) < min_len:
            continue
        if st.contains(word):
            st.put(word, st.get(word) + 1)
        else:
            st.put(word, 1)


def ascii_generator():
    ascii_str = string.ascii_lowercase
    words = []
    for i, char in enumerate(ascii_str):
        words = words + [char] * (i + 1)
    shuffle(words)
    return words


def initiate(st_class):
    words = ascii_generator()
    st = st_class()
    frequency_counter(st, words)
    return st


class Test:

    def test_contains(self):
        st = initiate(test_class)
        assert st.contains('z')

    def test_size(self):
        st = initiate(test_class)
        assert st.size() == 26

    def test_keys(self):
        st = initiate(test_class)
        assert st.keys() == list(string.ascii_lowercase)

    def test_get(self):
        st = initiate(test_class)
        assert st.get('a') == 1
        assert st.get('z') == 26

    def test_rank(self):
        st = initiate(test_class)
        assert st.rank('a') == 0
        assert st.rank('aa') == 1
        assert st.rank('z') == 25
        assert st.rank('zz') == 26

    def test_min(self):
        st = initiate(test_class)
        assert st.min() == 'a'

    def test_max(self):
        st = initiate(test_class)
        assert st.max() == 'z'

    def test_delete_min(self):
        st = initiate(test_class)
        st.delete_min()
        assert st.get('a') is None
        assert st.size() == 25

    def test_delete_max(self):
        st = initiate(test_class)
        st.delete_max()
        assert st.get('z') is None
        assert st.size() == 25

    def test_delete(self):
        st = initiate(test_class)
        st.delete('m')
        st.delete('z')
        assert st.get('z') is None
        assert st.get('m') is None
        assert st.size() == 24

    def test_floor(self):
        st = initiate(test_class)
        assert st.floor('m') == 'm'
        assert st.floor('mm') == 'm'

    def test_ceiling(self):
        st = initiate(test_class)
        assert st.ceiling('m') == 'm'
        assert st.ceiling('mm') == 'n'

    def test_range_keys(self):
        st = initiate(test_class)
        assert st.range_keys('a', 'z') == list(string.ascii_lowercase)
        assert st.range_keys('aa', 'ya') == list(string.ascii_lowercase)[1:-1]

    def test_range_size(self):
        st = initiate(test_class)
        assert st.range_size('a', 'z') == 26
        assert st.range_size('aa', 'ya') == 24

    def test_getitem(self):
        st = initiate(test_class)
        assert st.get('a') == st['a']

    def test_setitem(self):
        st = initiate(test_class)
        st['a'] = 26
        assert st.get('a') == 26
