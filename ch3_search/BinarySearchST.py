from utils import FrequencyCounter
from Base import SortedSymbolTable


class BinarySearchST(SortedSymbolTable):
    def __init__(self, capacity):
        self._keys = [None] * capacity
        self._vals = [None] * capacity
        self._size = 0

    def size(self):
        return self._size

    def range_size(self, lo, hi):
        if lo > hi:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def is_empty(self):
        return self._size == 0

    def contains(self, key):
        if self.get(key):
            return True
        return False

    def rank(self, key):
        pass

    def delete(self, key):
        pass

    def delete_min(self, key):
        pass

    def delete_max(self, key):
        pass


if __name__ == '__main__':
    st = BinarySearchST()
    FrequencyCounter('random_words.txt', st)
