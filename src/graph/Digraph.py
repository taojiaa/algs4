from src.fundamental.Stack import Stack
from src.fundamental.Queue import Queue

from .Graph import DepthFirstSearch, CC
from .base import Digraph, EdgeWeightedDigraph


class DirectedDFS(DepthFirstSearch):
    def __init__(self, G, s):
        self._cycle = None
        super().__init__(G, s)


class DirectedCycle:
    def __init__(self, G):
        self._g = G
        self._cycle = None
        self._directedcycle()

    def _directedcycle(self):
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


class EdgeWeightedDirectedCycle:
    def __init__(self, G):
        self._g = G
        self._cycle = None
        self._edgeweighteddirectedcycle()

    def _edgeweighteddirectedcycle(self):
        self._marked = [None] * self._g.V()
        self._edgeto = [None] * self._g.V()
        self._onstack = [None] * self._g.V()
        for v in range(self._g.V()):
            if not self._marked[v]:
                self._dfs(self._g, v)

    def _dfs(self, g, v):
        self._marked[v] = True
        self._onstack[v] = True
        for e in g.adj(v):
            w = e.To()
            if self.has_cycle():
                return
            elif not self._marked[w]:
                self._edgeto[w] = e
                self._dfs(g, w)
            elif self._onstack[w]:
                self._cycle = Stack()
                f = e
                while f.From() != w:
                    self._cycle.push(f)
                    f = self._edgeto[f.From()]
                self._cycle.push(f)
                return
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


class KosarajuSCC(CC):
    def __init__(self, G):
        self._g = G
        self._count = 0
        self._kosarajuscc()

    def _kosarajuscc(self):
        self._marked = [None] * self._g.V()
        self._id = [None] * self._g.V()
        orders = DepthFirstOrder(self._g.reverse()).reverse_post()
        for s in orders:
            if not self._marked[s]:
                self._dfs(self._g, s)
                self._count += 1

    def _dfs(self, *args, **kwargs):
        return super()._dfs(*args, **kwargs)

    def connected(self, *args, **kwargs):
        return super().connected(*args, **kwargs)

    def id(self, *args, **kwargs):
        return super().id(*args, **kwargs)

    def count(self, *args, **kwargs):
        return super().count(*args, **kwargs)
