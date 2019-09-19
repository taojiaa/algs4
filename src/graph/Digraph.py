from src.fundamental.Bag import Bag
from src.fundamental.Stack import Stack
from src.fundamental.Queue import Queue

from .Graph import Graph


class Digraph(Graph):

    def __init__(self, **kwargs):
        super(Digraph, self).__init__(**kwargs)

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._e += 1

    def reverse(self):
        r = Digraph(self._v)
        for i in range(self._v):
            for w in self._g.adj(i):
                r.add_edge(w, i)
        return r
    