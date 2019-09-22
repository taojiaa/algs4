class QuickFindUF:
    def __init__(self, n):
        self._count = n
        self._id = [i for i in range(n)]

    def count(self):
        return self._count

    def connected(self, p, q):
        return self._id[p] == self._id[q]

    def find(self, p):
        return self._id[p]

    def union(self, p, q):
        p_id = self._id[p]
        q_id = self._id[q]
        if p_id == q_id:
            return
        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id
        self._count -= 1


class QuickUnionUF:
    def __init__(self, n):
        self._count = n
        self._id = [i for i in range(n)]

    def count(self):
        return self._count

    def connected(self, p, q):
        return self._id[p] == self._id[q]

    def find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root
        self._count -= 1


class WeightedQuickUnion:
    def __init__(self, n):
        self._count = n
        self._id = [i for i in range(n)]
        self._sz = [i for i in range(n)]

    def count(self):
        return self._count

    def connected(self, p, q):
        return self._id[p] == self._id[q]

    def find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root
        if self._sz[p_root] < self._sz[q_root]:
            self._id[p_root] = q_root
            self._sz[q_root] += self._sz[p_root]
        else:
            self._id[q_root] = p_root
            self._sz[p_root] += self._sz[q_root]
        self._count -= 1
