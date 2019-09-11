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

    @size.setattr
    def size(self, size):
        self._size = size


class BST(SortedSymbolTable):
    def __init__(self):
        self.root = None

    def size(self):
        if self.root is None:
            return 0
        return self.root.size

    def is_empty(self):
        return self.root.size == 0

    def contains(self, key):
        if self.get(key) is not None:
            return True
        else:
            return False

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
        return get_helper(self.root, key)

    def put(self, key, val):
        def put_helper(key, val, node):
            if node is None:
                return Node(key, val)
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

    def min(self):
        def min_helper(node):
            if node.left is None:
                return node
            else:
                return min_helper(node.left)

        if self.root is None:
            return None
        else:
            return min_helper(self.root)

    def max(self):
        def max_helper(node):
            if node.right is None:
                return node
            else:
                return max_helper(node.right)

        if self.root is None:
            return None
        else:
            return max_helper(self.root)

    def delete_min(self):
        def delete_min_helper(node):
            if node.left is None:
                return node.right
            else:
                node.left = delete_min_helper(node.left)
                node.size = node.left.size + node.right.size + 1
        self.root = delete_min_helper(self.root)

    def delete_max(self):
        def delete_max_helper(node):
            if node.right is None:
                return node.left
            else:
                node.right = delete_max_helper(node.right)
                node.size = node.left.size + node.right.size + 1
        self.root = delete_max_helper(self.root)

    def delete(self, key):
        def min_helper(node):
            if node.left is None:
                return node
            else:
                return min_helper(node.left)

        def delete_min_helper(node):
            if node.left is None:
                return node.right
            else:
                node.left = delete_min_helper(node.left)
                node.size = node.left.size + node.right.size + 1

        def delete_helper(node, key):
            if node is None:
                return None
            cmpt = compare(key, node.key)
            if cmpt > 0:
                node.right = delete_helper(key, node.right)
            elif cmpt < 0:
                node.left = delete_helper(key, node.left)
            else:
                # the node that matches the key has no its left subtree.
                if node.left is None:
                    return node.right
                # the node that matches the key has no right subtree.
                elif node.right is None:
                    return node.left
                # the node that matches the key has both subtrees.
                else:
                    # find min(temp) of the right subtree of the current node x
                    # make temp as the new node that replaces x.
                    # concate the left subtree of x to temp.left.
                    # concate the right subtree(except temp) of x to temp.right
                    temp = min_helper(node.right)
                    temp.left = node.left
                    temp.right = delete_min_helper(node.right)
                    node = temp
            node.size = node.left.size + node.right.size + 1
            return node
        self.root = delete_helper(self.root, key)

    def rank(self, key):
        def rank_helper(key, node):
            if node is None:
                return 0
            cmpt = compare(key, node.key)
            if cmpt > 0:
                # if the key in the right subtree, 
                # we need to add all the left subtree and the current node.
                return node.left.size + rank_helper(key, node.right) + 1
            elif cmpt < 0:
                return rank_helper(key, node.left)
            else:
                return node.left.size
        return rank_helper(key, self.root)

    def floor(self, key):
        def floor_helper(key, node):
            # just an initial judgement.
            # and a termination when the key is the smallest key in BST.
            if node is None:
                return None
            cmpt = compare(key, node.key)
            if cmpt == 0:
                return node
            elif cmpt < 0:
                return floor_helper(key, node.left)
            else:
                temp = floor_helper(key, node.right)
                # This None processing is different from the one on the top.
                # floor allows us to select the parent if nothing on right.
                # that's why we need to deal with it in a special case.
                if temp is not None:
                    return temp
                else:
                    return node
        node = floor_helper(key, self.root)
        if node is None:
            return None
        else:
            return node.key

    def ceiling(self, key):
        def ceiling_helper(key, node):
            if node is None:
                return None
            cmpt = compare(key, node.key)
            if cmpt == 0:
                return node
            elif cmpt > 0:
                return ceiling_helper(key, node.right)
            else:
                temp = ceiling_helper(key, node.left)
                if temp is not None:
                    return temp
                else:
                    return node
        node = ceiling_helper(key, self.root)
        if node is None:
            return None
        else:
            return node.key

    def keys(self):
        def keys_helper(node):
            if node is None:
                return []
            return keys_helper(node.left) + [node.key] + keys_helper(node.right)
        return keys_helper(self.root)

    def range_keys(self, lo, hi):
        def range_keys_helper(node, lo, hi):
            if node is None:
                return
            cmpthi = compare(lo, node.key)
            cmptlo = compare(hi, node.key)
            if cmptlo < 0:
                range_keys_helper(node.left, lo, hi)
            if cmptlo <= 0 and cmpthi >= 0:
                _keys.append(node.key)
            if cmpthi > 0:
                range_keys_helper(node.right, lo, hi)
        _keys = []
        range_keys_helper(self.root, lo, hi)
        return _keys

    def range_size(self, lo, hi):
        def range_size_helper(node, lo, hi):
            if node is None:
                return 0
            cmpthi = compare(lo, node.key)
            cmptlo = compare(hi, node.key)
            if cmptlo < 0:
                num_left = range_size_helper(node.left, lo, hi)
            if cmptlo <= 0 and cmpthi >= 0:
                num_mid = 1
            if cmpthi > 0:
                num_right = range_size_helper(node.right, lo, hi)
            return num_left + num_mid + num_right
        return range_size_helper(self.root, lo, hi)
