from .utils import compare
from .Base import SortedSymbolTable


class Node:
    # only allows to initiate a single node.
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self._size = 1
        self.left = None
        self.right = None

    @property
    def size(self):
        if self is not None:
            return self._size
        return 0

    @size.setattr
    def size(self, size):
        self._size = size


class BST(SortedSymbolTable):
    def __init__(self):
        self.root = None

    def size(self):
        return Node.size(self.root)

    def get(self, key):
        def get_helper(node, key):
            if node is None:
                return
            cmpt = compare(key, node.key)
            if cmpt > 0:
                return get_helper(key, node.right)
            if cmpt < 0:
                return get_helper(key, node.left)
            if cmpt == 0:
                return node.val
        get_helper(self.root, key)

    def put(self, key, val):
        def put_helper(key, val, node):
            if node is None:
                return Node(key, val, 1)
            cmpt = compare(key, node.key)
            if cmpt > 0:
                node.right = put_helper(key, val, node.right)
            elif cmpt < 0:
                node.left = put_helper(key, val, node.left)
            else:
                node.val = val
            node.size = node.left.size + node.right.size + 1
            return node

        if val is None:
            self.delete(key)
            return
        self.root = put_helper(key, val, self.root)
