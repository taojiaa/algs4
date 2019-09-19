from src.fundamental.Bag import Bag
from src.fundamental.Stack import Stack
from src.fundamental.Queue import Queue

from .Graph import Graph, DepthFirstSearch, Cycle, CC


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


class DirectedDFS(DepthFirstSearch):
    def __init__(self, G, s):
        self._cycle = None
        super().__init__(G, s)


class DirectedCycle(Cycle):
    def __init__(self, G):
        self._g = G
        self._cycle = None
        self.dfs()

    def dfs(self):
        self._marked = [None] * self._g.V()
        self._edgeto = [None] * self._g.V()
        self._onstack = [None] * self._g.V()
        for v in range(self._g.V()):
            if not self._marked[v]:
                self._dfs(self._g, v)

    def _dfs(self, g, v):
        self._marked[v] = True
        self._onstack[v] = True
        for w in g.adj(v):
            if self.has_cycle():
                return
            elif not self._marked[w]:
                self._edgeto[w] = v
                self._dfs(g, w)
            elif self._onstack[w]:
                self._cycle = Stack()
                x = v
                while x != w:
                    self._cycle.push(x)
                    x = self._edgeto[x]
                self._cycle.push(w)
                self._cycle.push(v)
        # The cycle is identified by reaching a visited node again.
        # If the node cannot form a cycle, we should revert it to False,
        # otherwise, it cannot be viewed as a new node,
        # but a "visited" node in the next set of nodes.
        self._onstack[v] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self._cycle


class DepthFirstOrder:
    def __init__(self, G):
        self._g = G
        self._pre = Queue()
        self._post = Queue()
        self._reverse_post = Stack()

    def dfs(self):
        self._marked = [None] * self._g.V()
        for v in range(self._g.V()):
            if not self._marked[v]:
                self._dfs(self._g, v)

    def _dfs(self, g, v):
        self._marked[v] = True
        self._pre.enqueue(v)
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs(g, w)
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
        self._topo()

    def _topo(self):
        c_finder = DirectedCycle(self._g)
        if not c_finder.has_cycle():
            dfs = DepthFirstOrder(self._g)
            self._order = dfs.reverse_post()

    def order(self):
        return self._order

    def is_dag(self):
        return self._order is not None


class SCC(CC):
    def __init__(self, G):
        super().__init__(G)

    def strongly_connected(self, v, w):
        return self._id[v] == self._id[w]
