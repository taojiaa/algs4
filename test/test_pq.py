import string
from random import shuffle

from src.sort.PQ import MaxPQ


def initiate(test_class):
    array = list(string.ascii_lowercase) * 2
    shuffle(array)
    pq = test_class(20)
    for i in array:
        pq.insert(i)
    return pq


class Test:

    def test_max_pq(self):
        pq = initiate(MaxPQ)
        assert pq.del_max() == 'z'
        assert pq.size() == 26 * 2 - 1
