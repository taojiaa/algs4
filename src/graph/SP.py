from src.fundamental.Bag import Bag

from .MST import EdgeWeightedGraph
from .Digraph import Digraph


class DirectedEdge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def From(self):
        return self._v

    def To(self):
        return self._w

    def weight(self):
        return self._weight


class EdgeWeightedDigraph(Digraph):

    def __init__(self, **kwargs):
        pass

    def add_edge(self, e):
        self._adj[e.From()].add(e)
        self._indegree += 1
        self._e += 1

    def edges(self):
        b = Bag()
        for v in range(self._v):
            for e in self._adj[v]:
                b.add(e)
        return b
