from src.fundamental.Queue import Queue
from src.sort.PQ import IndexMinPQ, MinPQ


class LazyPrimMST:
    def __init__(self, G):
        self._g = G
        self._lazyprimmst()

    def _lazyprimmst(self):
        self._pq = MinPQ()
        self._marked = [None] * self._g.V()
        self._mst = Queue()
        self._weight = 0

        self._visit(self._g, 0)
        while not self._pq.is_empty():
            e = self._pq.del_min()
            v = e.either()
            w = e.other(v)
            if self._marked[v] and self._marked[w]:
                continue
            self._mst.enqueue(e)
            self._weight += e.weight()
            if not self._marked[v]:
                self._visit(self._g, v)
            if not self._marked[w]:
                self._visit(self._g, w)

    def _visit(self, g, v):
        self._marked[v] = True
        for e in g.adj(v):
            if not self._marked[e.other(v)]:
                self._pq.insert(e)

    def edges(self):
        return self._mst

    def weight(self):
        return self._weight


class PrimMST:

    def __init__(self, G):
        self._g = G
        self._mst = Queue()
        self._weight = 0
        self._primmst()

    def _primmst(self):
        self._marked = [None] * self._g.V()
        self._edgeto = [None] * self._g.V()
        self._distto = [None] * self._g.V()
        self._pq = IndexMinPQ(self._g.V())

        for i in range(len(self._distto)):
            self._distto[i] = float('inf')

        self._pq.insert(0, 0.0)
        self._distto[0] = 0.0
        while not self._pq.is_empty():
            self._visit(self._g, self._pq.del_min())

    def _visit(self, g, v):
        self._marked[v] = True
        for e in g.adj(v):
            w = e.other(v)
            if self._marked[w]:
                continue
            # Notice that _distto has been initiated to infinity,
            # so we can compare them even we haven't visited w before.
            if e.weight() < self._distto[w]:
                self._edgeto[w] = e
                self._distto[w] = e.weight()
                if self._pq.contains(w):
                    self._pq.change(w, self._distto[w])
                else:
                    self._pq.insert(w, self._distto[w])

    def edges(self):
        # In this algorithm, the elements in _edgeto could be updated,
        # so we cannot add edge to _mst in _visit.
        for e in self._edgeto:
            # Note that the first point 0 in _edgeto is None.
            if e is not None:
                self._mst.enqueue(e)
        return self._mst

    def weight(self):
        for e in self.edges():
            self._weight += e.weight()
        return self._weight
