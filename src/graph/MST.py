from src.fundamental.Bag import Bag
from src.fundamental.Queue import Queue
from src.sort.PQ import MinPQ

from .Graph import Graph


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


class EdgeWeightGraph(Graph):
    def __init__(self, **kwargs):
        super(EdgeWeightGraph, self).__init__(**kwargs)

    def _init_from_text(self, text):
        def words_gen(fileobj):
            for line in fileobj:
                for word in line.split():
                    yield int(word)
        with open(text, 'r') as file:
            words = words_gen(file)
            self._v = next(words)
            num_e = next(words)

            self._init_adj()
            for _ in range(num_e):
                e = Edge(next(words), next(words), next(words))
                self.add_edge(e)

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
                self._visit(self.g, v)
            if not self._marked[w]:
                self._visit(self.g, w)

    def _visit(self, g, v):
        self._marked[v] = True
        for e in g.adj(v):
            if not self._marked[e.other(v)]:
                self._pq.insert(e)

    def edges(self):
        return self._mst

    def weight(self):
        return self._weight
