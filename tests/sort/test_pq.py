import string
from random import shuffle

from src.sort.PQ import MaxPQ, MinPQ


def initiate(test_class):
    array = list(string.ascii_lowercase) * 2
    shuffle(array)
    pq = test_class(20)
    for i in array:
        pq.insert(i)
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
