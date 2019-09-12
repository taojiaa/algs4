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

    def test_delete_max(self):
        st = initiate(test_class)
        st.delete_max()
        assert st.get('z') is None
