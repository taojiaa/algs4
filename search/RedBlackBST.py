from .utils import compare
from .BST import BST

RED = True
BLACK = False


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
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

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

    def delete_min(self):
        # Note that the color helps us identify whether the node is a 2/3 node.

        # _delete_min only accepts the node with red color,
        # otherwise, there is no way to borrow a red node from the current node downside.
        # Thus, at the beginning, we need to ensure it as well,
        # which might bring a problem: changing the color to red reduces the total height.
        # However, we can set it to black after balancing the tree bottom-up.

        if not self._is_red(self.root.left) and not self._is_red(
                self.root.right):
            self.root.color = RED
        self.root = self._delete_min(self.root)
        if not self.is_empty():
            self.root.color = 'BLACK'

    def _delete_min(self, node):
        # Note that when the recursive function returns, it goes back to the top of tree.
        # There are two cases need to be dealt with.
        # Case 1: the right sibling is a 2 node.
        # Case 2: the right sibling is a 3 node.

        # The returned one is None, which replaces the node passed in.
        # Thus we delete the min node.
        if node.left is None:
            return None
        if not self._is_red(node.left) and not self._is_red(node.left.left):
            node = self._move_red_left(node)
        node.left = self._delete_min(node.left)
        return self._balance(node)

    def _move_red_left(self, node):
        # Case 1: put node down.
        self._flip_colors(node)
        # Case 2: check if the sibling is a 3 node.
        if self._is_red(node.right.left):
            # Put the sibling up twice to the new node.
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
            self._flip_colors(node)
        return node

    def delete_max(self):
        if not self._is_red(self.root.left) and not self._is_red(
                self.root.right):
            self.root.color = RED
        self.root = self._delete_max(self.root)
        if not self.is_empty():
            self.root.color = 'BLACK'

    def _delete_max(self, node):
        # Note that the RedBlackBST here is a left-leaning tree.
        # Thus it is a bit different from _delete_min.
        if self._is_red(node.left):
            node = self._rotate_right(node)
        if node.right is None:
            return None
        if not self._is_red(node.right) and not self._is_red(node.right.left):
            node = self._move_red_right(node)
        node.right = self._delete_max(node.right)
        return self._balance(node)

    def _move_red_right(self, node):
        self._flip_colors(node)
        if self._is_red(node.left.left):
            # One rotate and one flip is enough here, no need to use the "three axes".
            node = self._rotate_right(node)
            self._flip_colors(node)
        return node
