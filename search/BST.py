from .utils import compare
from .Base import SortedSymbolTable


class Node:
    # only allows to initiate a single node.
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self._size = 1

    @property
    def size(self):
        if self is not None:
            return self._size
        else:
            return 0

    @size.setter
    def size(self, size):
        self._size = size


class BST(SortedSymbolTable):
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return node.size

    def is_empty(self):
        return self._size(self.root) == 0

    def contains(self, key):
        if self.get(key) is not None:
            return True
        else:
            return False

    def get(self, key):
        return self._get(key, self.root)

    def _get(self, key, node):
        if node is None:
            return
        cmpt = compare(key, node.key)
        if cmpt > 0:
            return self._get(key, node.right)
        elif cmpt < 0:
            return self._get(key, node.left)
        else:
            return node.val

    def put(self, key, val):
        if val is None:
            self.delete(key)
            return
        self.root = self._put(key, val, self.root)

    def _put(self, key, val, node):
        if node is None:
            return Node(key, val)
        cmpt = compare(key, node.key)
        if cmpt > 0:
            node.right = self._put(key, val, node.right)
        elif cmpt < 0:
            node.left = self._put(key, val, node.left)
        else:
            node.val = val
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def min(self):
        if self.root is None:
            return None
        else:
            return self._min(self.root).key

    def _min(self, node):
        if node.left is None:
            return node
        else:
            return self._min(node.left)

    def max(self):
        if self.root is None:
            return None
        else:
            return self._max(self.root).key

    def _max(self, node):
        if node.right is None:
            return node
        else:
            return self._max(node.right)

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        else:
            node.left = self._delete_min(node.left)
            node.size = self._size(node.left) + self._size(node.right) + 1
            return node

    def delete_max(self):
        self.root = self._delete_max(self.root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left
        else:
            node.right = self._delete_max(node.right)
            node.size = self._size(node.left) + self._size(node.right) + 1
            return node

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return None
        cmpt = compare(key, node.key)
        if cmpt > 0:
            node.right = self._delete(key, node.right)
        elif cmpt < 0:
            node.left = self._delete(key, node.left)
        else:
            # the node that matches the key has no its left subtree.
            if node.left is None:
                return node.right
            # the node that matches the key has no right subtree.
            if node.right is None:
                return node.left
            # the node that matches the key has both subtrees.
            # find min(temp) of the right subtree of the current node x
            # make temp as the new node that replaces x.
            # concate the left subtree of x to temp.left.
            # concate the right subtree(except temp) of x to temp.right
            temp = self._min(node.right)
            temp.right = self._delete_min(node.right)
            temp.left = node.left
            node = temp
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def rank(self, key):
        return self._rank(key, self.root)

    def _rank(self, key, node):
        if node is None:
            return 0
        cmpt = compare(key, node.key)
        if cmpt > 0:
            # if the key in the right subtree,
            # we need to add all the left subtree and the current node.
            return self._size(node.left) + self._rank(key, node.right) + 1
        elif cmpt < 0:
            return self._rank(key, node.left)
        else:
            return self._size(node.left)

    def select(self, k):
        # Note that size is not the same as rank.
        if (k < 0) or (k > self.root.size):
            return None
        node = self._select(self.root, k)
        return node.key

    def _select(self, node, k):
        if node is None:
            return
        temp = self._size(node.left)
        if temp > k:
            return self._select(node.left, k)
        elif temp < k:
            return self._select(node.right, k - temp - 1)
        else:
            return node

    def floor(self, key):
        node = self._floor(key, self.root)
        if node is None:
            return None
        else:
            return node.key

    def _floor(self, key, node):
        # just an initial judgement.
        # and a termination when the key is the smallest key in BST.
        if node is None:
            return None
        cmpt = compare(key, node.key)
        if cmpt == 0:
            return node
        elif cmpt < 0:
            return self._floor(key, node.left)
        else:
            temp = self._floor(key, node.right)
            # This None processing is different from the one on the top.
            # floor allows us to select the parent if nothing on right.
            # that's why we need to deal with it in a special case.
            if temp is not None:
                return temp
            else:
                return node

    def ceiling(self, key):
        node = self._ceiling(key, self.root)
        if node is None:
            return None
        else:
            return node.key

    def _ceiling(self, key, node):
        if node is None:
            return None
        cmpt = compare(key, node.key)
        if cmpt == 0:
            return node
        elif cmpt > 0:
            return self._ceiling(key, node.right)
        else:
            temp = self._ceiling(key, node.left)
            if temp is not None:
                return temp
            else:
                return node

    def keys(self):
        return self._keys(self.root)

    def _keys(self, node):
        if node is None:
            return []
        return self._keys(node.left) + [node.key] + self._keys(node.right)

    def range_keys(self, lo, hi):
        self.__keys = []
        self._range_keys(self.root, lo, hi)
        return self.__keys

    def _range_keys(self, node, lo, hi):
        if node is None:
            return
        cmptlo = compare(lo, node.key)
        cmpthi = compare(hi, node.key)
        if cmptlo < 0:
            self._range_keys(node.left, lo, hi)
        if cmptlo <= 0 and cmpthi >= 0:
            self.__keys.append(node.key)
        if cmpthi > 0:
            self._range_keys(node.right, lo, hi)

    def range_size(self, lo, hi):
        return self._range_size(self.root, lo, hi)

    def _range_size(self, node, lo, hi):
        if node is None:
            return 0
        cmptlo = compare(lo, node.key)
        cmpthi = compare(hi, node.key)
        num_left = self._range_size(node.left, lo, hi) if cmptlo < 0 else 0
        num_mid = 1 if cmptlo <= 0 and cmpthi >= 0 else 0
        num_right = self._range_size(node.right, lo, hi) if cmpthi > 0 else 0
        return num_left + num_mid + num_right

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        return self.put(key, val)
