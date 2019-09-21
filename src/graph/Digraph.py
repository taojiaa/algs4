from src.fundamental.Stack import Stack
from src.fundamental.Queue import Queue
from src.fundamental.Bag import Bag

from .Graph import DepthFirstSearch, CC
from .utils import words_gen


class Digraph:
    def __init__(self, _input):
        if isinstance(_input, int):
            self._v = _input
            self._e = 0
            self._adj = [Bag() for i in range(self._v)]
            self._indegree = [0] * self._v
        else:
            if isinstance(_input, str) and '.txt' in _input:
                self._read(_input)

    def _read(self, text):
        with open(text, 'r') as file:
            words = words_gen(file)
            self._v = int(next(words))
            self._e = 0
            self._adj = [Bag() for i in range(self._v)]
            self._indegree = [0] * self._v

            num_e = int(next(words))
            for _ in range(num_e):
                v = int(next(words))
                w = int(next(words))
                self.add_edge(v, w)

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._indegree[w] += 1
        self._e += 1

    def reverse(self):
        r = Digraph(self._v)
        for i in range(self._v):
            for w in self.adj(i):
                r.add_edge(w, i)
        return r

    def indegree(self, v):
        return self._indegree[v]

    def outdegree(self, v):
        return self._adj[v].size()

    def V(self):
        return self._v

    def E(self):
        return self._e

    def adj(self, v):
        return self._adj[v]


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


class DepthFirstOrder:
    def __init__(self, G):
        self._g = G
        self._pre = Queue()
        self._post = Queue()
        self._reverse_post = Stack()
        self._depthfirstorder()

    def _depthfirstorder(self):
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
        self._topological()

    def _topological(self):
        c_finder = DirectedCycle(self._g)
        if not c_finder.has_cycle():
            dfs = DepthFirstOrder(self._g)
            self._order = dfs.reverse_post()

    def order(self):
        return self._order

    def is_dag(self):
        return self._order is not None


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
