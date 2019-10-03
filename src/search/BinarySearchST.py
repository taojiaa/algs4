from typing import List, Optional, TypeVar

from .Base import SortedSymbolTable
from .utils import compare

Key = TypeVar('Key')
Value = TypeVar('Value')


class BinarySearchST(SortedSymbolTable):
    def __init__(self, capacity: int = 20) -> None:
        self._keys: List[Optional[Key]] = [None] * capacity
        self._vals: List[Optional[Value]] = [None] * capacity
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def contains(self, key: Key) -> bool:
        if self.get(key):
            return True
        return False

    def rank(self, key: Key) -> int:
        # Note that rank might return self._size, raising an error when calling self._keys(rank(key)).
        return self._rank(key, 0, self._size - 1)

    def _rank(self, key: Key, lo: int, hi: int) -> int:
        # lo, hi is the number index.
        if lo > hi:
            return lo
        mid = lo + (hi - lo) // 2
        cmpt = compare(key, self._keys[mid])
        if cmpt > 0:
            return self._rank(key, mid + 1, hi)
        elif cmpt < 0:
            return self._rank(key, lo, mid - 1)
        else:
            return mid

    def min(self) -> Key:
        return self._keys[0]

    def max(self) -> Key:
        return self._keys[self._size - 1]

    def select(self, k: int) -> Key:
        return self._keys[k]

    def get(self, key: Key) -> Value:
        i = self.rank(key)
        if (i < self._size) and (compare(key, self._keys[i]) == 0):
            return self._vals[i]
        return None

    def put(self, key: Key, val: Value) -> None:
        if val is None:
            self.delete(key)
        i = self.rank(key)
        if (i < self._size) and (compare(key, self._keys[i]) == 0):
            self._vals[i] = val
            return
        if self._size == len(self._keys):
            self._resize(len(self._keys) * 2)
        for j in range(self._size, i, -1):
            self._keys[j] = self._keys[j - 1]
            self._vals[j] = self._vals[j - 1]
        self._keys[i] = key
        self._vals[i] = val
        self._size = self._size + 1

    def delete(self, key: Key) -> None:
        if self.is_empty():
            return
        i = self.rank(key)
        if (i == self._size) or (compare(key, self._keys[i]) != 0):
            return
        for j in range(i, self._size):
            self._keys[j] = self._keys[j + 1]
            self._vals[j] = self._vals[j + 1]
        self._size = self._size - 1
        if self._size == (len(self._keys) // 4):
            self._resize(len(self._keys) // 2)

    def delete_min(self) -> None:
        self.delete(self.min())

    def delete_max(self) -> None:
        self.delete(self.max())

    def floor(self, key: Key) -> Key:
        i = self.rank(key)
        if i == 0:
            return None
        if (i < self._size) and (compare(key, self._keys[i]) == 0):
            return self._keys[i]
        else:
            # the both conditions above can be reduced to one condition: 
            # is the key larger than self._keys[rank(key)]
            return self._keys[i - 1]

    def ceiling(self, key: Key) -> Key:
        i = self.rank(key)
        if i == self._size:
            return None
        else:
            return self._keys[i]

    def keys(self) -> Key:
        return self._keys[:self._size]

    def range_size(self, lo: int, hi: int) -> int:
        if lo > hi:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def range_keys(self, lo: int, hi: int) -> Key:
        k_lo, k_hi = self.rank(lo), self.rank(hi)
        if compare(self._keys[k_hi], hi) == 0:
            return self._keys[k_lo:k_hi + 1]
        else:
            return self._keys[k_lo:k_hi]

    def _resize(self, capacity: int) -> None:
        assert capacity >= self._size
        temp_keys: List[Optional[Key]] = [None] * capacity
        temp_vals: List[Optional[Value]] = [None] * capacity
        for i in range(self._size):
            temp_keys[i] = self._keys[i]
            temp_vals[i] = self._vals[i]
        self._keys = temp_keys
        self._vals = temp_vals

    def __getitem__(self, key: Key) -> Value:
        return self.get(key)

    def __setitem__(self, key: Key, val: Value) -> None:
        return self.put(key, val)
