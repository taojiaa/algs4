from .utils import compare
from .BST import BST

RED = 1
BLACK = 0


class Node:
    # only allows to initiate a single node.
    def __init__(self, key, val, color):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.color = color


class RedBlackBST(BST):

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
        return self._balance(node)

    def _balance(self, node):
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self, key):
        pass

    def delete_min(self):
        pass

    def delete_max(self):
        pass

