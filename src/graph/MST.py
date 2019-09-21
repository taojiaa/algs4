from src.fundamental.Bag import Bag
from src.fundamental.Queue import Queue
from src.sort.PQ import IndexMinPQ, MinPQ

from .Graph import Graph
from .utils import words_gen


class Edge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        return self._weight

    def either(self):
        return self._v

    def other(self, vertex):
        if vertex == self._v:
            return self._w
        elif vertex == self._w:
            return self._v
        else:
            raise ValueError(f'{vertex} is not either of the edge nodes.')

    def compare_to(self, e):
        if self._weight > e.weight():
            return 1
        elif self._weight == e.weight():
            return 0
        else:
            return -1

    def __gt__(self, other):
        return self._weight > other._weight

    def __lt__(self, other):
        return self._weight < other._weight

    def __ge__(self, other):
        return self._weight >= other._weight

    def __le__(self, other):
        return self._weight <= other._weight


class EdgeWeightedGraph(Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _read(self, text):
        with open(text, 'r') as file:
            words = words_gen(file)
            self._v = int(next(words))
            self._e = 0
            self._adj = [Bag() for i in range(self._v)]

            num_e = int(next(words))
            for _ in range(num_e):
                v1 = int(next(words))
                v2 = int(next(words))
                tw = float(next(words))
                e = Edge(v1, v2, tw)
                self.add_edge(e)

    def V(self, *args, **kwargs):
        return super().V(*args, **kwargs)

    def E(self, *args, **kwargs):
        return super().E(*args, **kwargs)

    def adj(self, *args, **kwargs):
        return super().adj(*args, **kwargs)

    def degree(self, *args, **kwargs):
        return super().degree(*args, **kwargs)

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self._adj[v].add(e)
        self._adj[w].add(e)
        self._e += 1

    def edges(self):
        b = Bag()
        for v in range(self._v):
            for e in self._adj[v]:
                if e.other(v) > v:
                    b.add(e)
        return b

    def to_string(self):
        # todo
        pass


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
