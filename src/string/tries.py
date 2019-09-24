from .base import StringST
from src.fundamental.Queue import Queue


class TriesST(StringST):
    R = 256

    class Node:
        def __init__(self):
            self.val = None
            self.next = [None] * TriesST.R

    def __init__(self):
        self._root = None
        self._size = 0

    def _charAt(self, c):
        return ord(c)

    def get(self, key):
        node = self._get(self._root, key, 0)
        if node is None:
            return None
        return node.val

    def _get(self, node, key, d):
        if node is None:
            return None
        if d == len(key):
            return node
        c = self._charAt(key[d])
        return self._get(node.next[c], key, d + 1)

    def put(self, key, val):
        self._root = self._put(self._root, key, val, 0)

    def _put(self, node, key, val, d):
        if node is None:
            # If d doesn't equal to len(key), 
            # we shouldn't put the val in this new node.
            node = TriesST.Node()
        if d == len(key):
            if node.val is None:
                self._size += 1
            # Insert a new value or change an existing value.
            node.val = val
            return node
        c = self._charAt(key[d])
        node.next[c] = self._put(node.next[c], key, val, d + 1)
        return node

    def delete(self, key):
        self._root = self._delete(self._root, key, 0)

    def _delete(self, node, key, d):
        if node is None:
            return None
        if d == len(key):
            if node.val is not None:
                self._size -= 1
            node.val = None
        else:
            c = self._charAt(key[d])
            node.next[c] = self._delete(node.next[c], key, d + 1)
        # If the val and link are both None, we delete the current node.
        if node.val is not None:
            return node
        for i in range(TriesST.R):
            if node.next[i] is not None:
                return node
        return None

    def contains(self, key):
        return self.get(key) is not None
        
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def keys(self):
        return self.keys_with_prefix('')

    def keys_with_prefix(self, pre):
        q = Queue()
        # Note that if we pass into the container (like queue, list..),
        # we can add items to them in the function like this.
        self._collect(self._get(self._root, pre, 0), pre, q)
        return q

    def _collect(self, node, pre, q):
        if node is None:
            return None
        if node.val is not None:
            q.enqueue(pre)
        for i in range(TriesST.R):
            self._collect(node.next[i], pre + chr(i), q)

    def longest_prefix_of(self, pre):
        length = self._search(self._root, pre, 0, 0)
        return pre[:length]

    def _search(self, node, pre, d, length):
        if node is None:
            return length
        if node.val is not None:
            length = d
        if d == len(pre):
            return length
        c = self._charAt(pre[d])
        return self._search(node.next[c], pre, d + 1, length)

    def keys_that_match(self, pat):
        q = Queue()
        self._collect_match(self._root, '', pat, q)
        return q

    def _collect_match(self, node, pre, pat, q):
        d = len(pre)
        if node is None:
            return None
        if d == len(pat) and node.val is not None:
            q.enqueue(pre)
        if d == len(pat):
            return
        nc = self._charAt(pat[d])
        for i in range(TriesST.R):
            if pat[d] == '.' or nc == i:
                self._collect_match(node.next[i], pre + chr(i), pat, q)
