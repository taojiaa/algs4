from utils import FrequencyCounter


class Node:
    def __init__(self, key=None, val=None, node=None):
        self.key = key
        self.val = val
        self.next = node


def raise_key(func):
    def wrapper(*args, **kwargs):
        if args[1] is None:
            raise ValueError('The key cannot be None.')
        return func(*args, **kwargs)
    return wrapper


class SequentialSearchST:
    def __init__(self):
        self._node = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    @raise_key
    def contains(self, key):
        if self.get(key):
            return True
        return False

    @raise_key
    def get(self, key):
        node = self._node
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    @raise_key
    def put(self, key, val):
        if val is None:
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

    @raise_key
    def delete(self, key):
        def delete_helper(key, node):
            if node is None:
                return None
            if key == node.key:
                self._size = self._size - 1
                return node.next
            node.next = delete_helper(key, node.next)
        delete_helper(key, self._node)

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
