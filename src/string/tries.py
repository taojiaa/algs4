from .base import StringST


class TriesST(StringST):
    R = 256

    class Node:
        def __init__(self):
            self._val = None
            self._next = [None] * TriesST.R

    def __init__(self):
        self._root = None

    def get(self, key):
        node = self._get(self._root, key, 0)
        if node is None:
            return None
        return node.val

    def _get(self, node, key, d):
        pass
    
        
