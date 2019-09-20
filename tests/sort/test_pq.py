import string
from random import shuffle

from src.sort.PQ import MaxPQ, MinPQ, IndexMinPQ


def initiate(test_class):
    array = list(string.ascii_lowercase) * 2
    shuffle(array)
    pq = test_class()
    for i in array:
        pq.insert(i)
    return pq


def initiate_index_val(test_class):
    dic = {25 - i: v for i, v in enumerate(string.ascii_lowercase)}
    pq = test_class(len(dic))
    for key, val in dic.items():
        pq.insert(key, val)
    return pq


class TestMaxPQ:

    def test_del_max(self):
        pq = initiate(MaxPQ)
        assert pq.del_max() == 'z'
        assert pq.size() == 26 * 2 - 1
        assert pq.del_max() == 'z'
        assert pq.del_max() == 'y'


class TestMinPQ:

    def test_del_min(self):
        pq = initiate(MinPQ)
        assert pq.del_min() == 'a'
        assert pq.size() == 26 * 2 - 1
        assert pq.del_min() == 'a'
        assert pq.del_min() == 'b'


class TestIndexMinPQ:

    def test_insert(self):
        pq = initiate_index_val(IndexMinPQ)
        assert pq.size() == 26
        assert pq.contains(25)
        assert not pq.contains(26)
        assert not pq.is_empty()

    def test_delete(self):
        pq = initiate_index_val(IndexMinPQ)
        for i in range(26):
            pq.delete(i)
        assert pq.is_empty()

    def test_delete_min(self):
        pq = initiate_index_val(IndexMinPQ)
        m = pq.del_min()
        assert m == 25
        m = pq.del_min()
        assert m == 24

    def test_change(self):
        pq = initiate_index_val(IndexMinPQ)
        pq.change(25, 'bb')
        assert pq.min() == 'b'
