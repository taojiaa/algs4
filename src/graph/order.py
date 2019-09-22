from src.fundamental.Queue import Queue
from src.fundamental.Stack import Stack

from .base import Digraph, EdgeWeightedDigraph
from .cycle import DirectedCycle, EdgeWeightedDirectedCycle


class DepthFirstOrder:
    def __init__(self, G):
        self._g = G
        self._pre = Queue()
        self._post = Queue()
        self._reverse_post = Stack()
        if type(G) == Digraph:
            self._depthfirstorder_d()
        elif type(G) == EdgeWeightedDigraph:
            self._depthfirstorder_ewd()

    def _depthfirstorder_d(self):
        self._marked = [None] * self._g.V()
        for v in range(self._g.V()):
            if not self._marked[v]:
                self._dfs_d(self._g, v)

    def _dfs_d(self, g, v):
        self._marked[v] = True
        self._pre.enqueue(v)
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs_d(g, w)
        self._post.enqueue(v)
        self._reverse_post.push(v)

    def _depthfirstorder_ewd(self):
        self._marked = [None] * self._g.V()
        for v in range(self._g.V()):
            if not self._marked[v]:
                self._dfs_ewd(self._g, v)

    def _dfs_ewd(self, g, v):
        self._marked[v] = True
        self._pre.enqueue(v)
        for e in g.adj(v):
            w = e.To()
            if not self._marked[w]:
                self._dfs_ewd(g, w)
        self._post.enqueue(v)
        self._reverse_post.push(v)

    def pre(self):
        return self._pre

    def post(self):
        return self._post

    def reverse_post(self):
        return self._reverse_post


class Topological:
    def __init__(self, G):
        self._g = G
        self._order = None
        if type(G) == Digraph:
            self._topological_d()
        elif type(G) == EdgeWeightedDigraph:
            self._topological_ewd()

    def _topological_d(self):
        c_finder = DirectedCycle(self._g)
        if not c_finder.has_cycle():
            dfs = DepthFirstOrder(self._g)
            self._order = dfs.reverse_post()

    def _topological_ewd(self):
        c_finder = EdgeWeightedDirectedCycle(self._g)
        if not c_finder.has_cycle():
            dfs = DepthFirstOrder(self._g)
            self._order = dfs.reverse_post()

    def order(self):
        return self._order

    def has_order(self):
        return self._order is not None

    def is_dag(self):
        return self.has_order()
