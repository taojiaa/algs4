from .utils import compare
from .Base import SortedSymbolTable


class Node:
    def __init__(self, key, val, size):
        self.key = key
        self.val = val
        self.size = size
        self.left = None
        self.right = None


class BST(SortedSymbolTable):
    def __init__(self):
        pass