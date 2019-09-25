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
        if key is None:
            raise ValueError('The key must not be null.')
        if len(key) == 0:
            raise ValueError('The key must have length >= 1.')
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
        if key is None:
            raise ValueError('The key must not be null.')
        if len(key) == 0:
            raise ValueError('The key must have length >= 1.')
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


class TST(StringST):
    class Node:
        def __init__(self):
            # explicitly store the char, unlike the TriesST.
            self.c = None
            self.val = None
            self.left = None
            self.mid = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def get(self, key):
        if key is None:
            raise ValueError('The key must not be null.')
        if len(key) == 0:
            raise ValueError('The key must have length >= 1.')
        node = self._get(self._root, key, 0)
        if node is None:
            return None
        return node.val

    def _get(self, node, key, d):
        if node is None:
            return None
        c = key[d]
        # Note that the path of this kind of recursion is like con1 -> con2 -> con1,
        # and then return directly without getting into other conditions.
        if c < node.c:
            return self._get(node.left, key, d)
        if c > node.c:
            return self._get(node.right, key, d)
        if d < len(key) - 1:
            return self._get(node.mid, key, d + 1)
        return node

    def put(self, key, val):
        if key is None:
            raise ValueError('The key must not be null.')
        if len(key) == 0:
            raise ValueError('The key must have length >= 1.')
        if not self.contains(key):
            self._size += 1
        else:
            if val is None:
                self._size -= 1
        self._root = self._put(self._root, key, val, 0)

    def _put(self, node, key, val, d):
        c = key[d]
        if node is None:
            node = TST.Node()
            node.c = c
        if c < node.c:
            node.left = self._put(node.left, key, val, d)
        elif c > node.c:
            node.right = self._put(node.right, key, val, d)
        elif d < len(key) - 1:
            node.mid = self._put(node.mid, key, val, d + 1)
        else:
            node.val = val
        return node

    def delete(self, key):
        # delete the node is very difficult?
        self._root = self.put(key, None)

    def contains(self, key):
        return self.get(key) is not None
        
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def keys(self, s):
        return self.keys_with_prefix('')

    def keys_with_prefix(self, pre):
        q = Queue()
        node = self._get(self._root, pre, 0)
        if node.val is not None:
            q.enqueue(pre)
        self._collect(node.mid, pre, q)
        return q

    def _collect(self, node, pre, q):
        if node is None:
            return
        if node.val is not None:
            q.enqueue(pre + node.c)
        self._collect(node.left, pre, q)
        self._collect(node.mid, pre + node.c, q)
        self._collect(node.right, pre, q)

    def keys_that_match(self, pat):
        q = Queue()
        self._collect_match(self._root, '', pat, q)
        return q

    def _collect_match(self, node, pre, pat, q):
        if node is None:
            return
        d = len(pre)
        c = pat[d]
        if c == '.' or c < node.c:
            self._collect_match(node.left, pre, pat, q)
        if c == '.' or c == node.c:
            if (d == len(pat) - 1) and (node.val is not None):
                q.enqueue(pre + node.c)
            if d < len(pat) - 1:
                self._collect_match(node.mid, pre + node.c, pat, q)
        if c == '.' or c > node.c:
            self._collect_match(node.right, pre, pat, q)

    def longest_prefix_of(self, pre):
        length = 0
        d = 0
        node = self._root
        while (node is not None) and (d < len(pre)):
            c = pre[d]
            if c < node.c:
                node = node.left
            elif c > node.c:
                node = node.right
            else:
                d = d + 1
                if node.val is not None:
                    length = d
                node = node.mid
        return pre[:length]
