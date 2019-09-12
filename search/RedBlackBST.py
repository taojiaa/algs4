
from .utils import compare
from .Base import SortedSymbolTable

RED = 1
BLACK = 0


class Node:
    # only allows to initiate a single node.
    def __init__(self, key, val, color):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self._size = 1
        self.color = color

    @property
    def size(self):
        if self is not None:
            return self._size
        else:
            return 0

    @size.setter
    def size(self, size):
        self._size = size


class RedBlackBST(SortedSymbolTable):

    def __init__(self):
        self.root = None

    def _is_red(self, node):
        if node is None:
            return None
        return node.color == RED

    def _rotate_left(self, node):
        # the new node is temp, so we need to return.
        temp = node.right
        node.right = temp.left
        temp.left = node
        temp.color = node.color
        node.color = RED
        temp.size = node.size
        node.size = self._size(node.left) + self._size(node.right) + 1
        return temp
        
    def _rotate_right(self, node):
        # the new node is temp, so we need to return.
        temp = node.left
        node.left = temp.right
        temp.right = node
        temp.color = node.color
        node.color = RED
        temp.size = node.size
        node.size = self._size(node.left) + self._size(node.right) + 1
        return temp
    
    def _flip_colors(self, node):
        # change the property, so there is no need to return.
        node.left.color = BLACK
        node.right.color = BLACK
        node.color = RED

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return node.size

    def is_empty(self):
        return self._size(self.root) == 0

    def put(self, key, val):
        if val is None:
            self.delete(key)
            return
        self.root = self._put(key, val, self.root)
        self.root.color = BLACK

    def _put(self, key, val, node):
        if node is None:
            return Node(key, val, RED)
        cmpt = compare(key, node.key)
        if cmpt < 0:
            node.left = self._put(key, val, node.left)
        elif cmpt > 0:
            node.right = self._put(key, val, node.right)
        else:
            node.val = val
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def contains(self, key):
        if self.get(key):
            return True
        return False

    def get(self, key):
        return self._get(key, self.root)

    def _get(self, key, node):
        if node is None:
            return None
        cmpt = compare(key, node.key)
        if cmpt < 0:
            return self._get(key, node.left)
        elif cmpt > 0:
            return self._get(key, node.right)
        else:
            return node.val

    def delete(self, key):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def delete_min(self):
        pass

    def delete_max(self):
        pass

    def floor(self, key):
        pass

    def ceiling(self, key):
        pass

    def rank(self, key):
        pass

    def select(self, k):
        pass

    def keys(self):
        pass

    def range_size(self, lo, hi):
        pass

    def range_keys(self, lo, hi):
        pass
