from utils import FrequencyCounter


class Node:
    def __init__(self, key=None, val=None, node=None):
        self.key = key
        self.val = val
        self.next = node


class SequentialSearchST:
    def __init__(self):
        self._node = Node()
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def contains(self, key):
        if not key:
            raise ValueError('The key can not be None.')
        if self.get(key):
            return True
        return False

    def get(self, key):
        if not key:
            raise ValueError('The key can not be None.')
        node = self._node
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    def put(self, key, val):
        if not key:
            raise ValueError('The key can not be None.')
        if not val:
            self.delete(key)
            return
        node = self._node
        while node:
            if node.key == key:
                node.val = val
                return
            node = node.next
        self._node = Node(key, val, self._node)
        self._size = self._size + 1

    def delete(self, key):
        if not key:
            raise ValueError('The key can not be None.')
        

    def keys(self):
        _keys = []
        node = self._node
        while node:
            if node.key:
                _keys.append(node.key)
            node = node.next
        return _keys


if __name__ == '__main__':
    st = SequentialSearchST()
    FrequencyCounter('random_words.txt', st)
