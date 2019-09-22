from src.fundamental.Bag import Bag
from src.fundamental.Stack import Stack
from src.fundamental.Queue import Queue
from src.sort.PQ import IndexMinPQ

from .Digraph import Digraph, Topological
from .utils import words_gen


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

    def __gt__(self, other):
        return self._weight > other._weight

    def __lt__(self, other):
        return self._weight < other._weight

    def __ge__(self, other):
        return self._weight >= other._weight

    def __le__(self, other):
        return self._weight <= other._weight


class EdgeWeightedDigraph(Digraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _read(self, text):
        with open(text, 'r') as file:
            words = words_gen(file)
            self._v = int(next(words))
            self._e = 0
            self._adj = [Bag() for i in range(self._v)]
            self._indegree = [0] * self._v

            num_e = int(next(words))
            for _ in range(num_e):
                v1 = int(next(words))
                v2 = int(next(words))
                tw = float(next(words))
                e = DirectedEdge(v1, v2, tw)
                self.add_edge(e)

    def add_edge(self, e):
        w = e.From()
        self._adj[w].add(e)
        self._indegree[w] += 1
        self._e += 1

    def edges(self):
        b = Bag()
        for v in range(self._v):
            for e in self._adj[v]:
                b.add(e)
        return b

    def V(self, *args, **kwargs):
        return super().V(*args, **kwargs)

    def E(self, *args, **kwargs):
        return super().E(*args, **kwargs)

    def adj(self, *args, **kwargs):
        return super().adj(*args, **kwargs)

    def indegree(self, *args, **kwargs):
        return super().indegree(*args, **kwargs)

    def outdegree(self, *args, **kwargs):
        return super().outdegree(*args, **kwargs)

    def reverse(self):
        # todo
        pass


class DijkstraSP:
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self._dijkstrasp(self._s)

    def _dijkstrasp(self, s):
        self._edgeto = [None] * self._g.V()
        self._distto = [None] * self._g.V()
        self._pq = IndexMinPQ(self._g.V())

        for i in range(len(self._distto)):
            self._distto[i] = float('inf')

        self._distto[s] = 0.0
        self._pq.insert(s, 0.0)

        while not self._pq.is_empty():
            self._relax(self._g, self._pq.del_min())

    def _relax(self, g, v):
        for e in g.adj(v):
            w = e.To()
            if self._distto[w] > self._distto[v] + e.weight():
                self._distto[w] = self._distto[v] + e.weight()
                self._edgeto[w] = e
                if self._pq.contains(w):
                    self._pq.change(w, self._distto[w])
                else:
                    self._pq.insert(w, self._distto[w])

    def distTo(self, v):
        return self._distto[v]

    def hasPathTo(self, v):
        return self._distto[v] < float('inf')

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        stack = Stack()
        e = self._edgeto[v]
        while e.From() is not None:
            w = e.From()
            stack.push(e)
            e = self._edgeto[w]
        return stack


class AcyclicSP:
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self._acyclicsp(self._s)

    def _acyclicsp(self, s):
        self._edgeto = [None] * self._g.V()
        self._distto = [None] * self._g.V()

        for i in range(len(self._distto)):
            self._distto[i] = float('inf')

        self._distto[s] = 0.0
        top = Topological(self._g)
        if not top.has_order():
            raise ValueError('Digraph is not acyclic.')
        for i in top.order():
            self._relax(self._g, i)

    def _relax(self, g, v):
        for e in g.adj(v):
            w = e.To()
            if self._distto[w] > self._distto[v] + e.weight():
                self._distto[w] = self._distto[v] + e.weight()
                self._edgeto[w] = e

    def distTo(self, v):
        return self._distto[v]

    def hasPathTo(self, v):
        return self._distto[v] < float('inf')

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        stack = Stack()
        e = self._edgeto[v]
        while e.From() is not None:
            w = e.From()
            stack.push(e)
            e = self._edgeto[w]
        return stack


class AcyclicLP:
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self._acycliclp(self._s)

    def _acycliclp(self, s):
        self._edgeto = [None] * self._g.V()
        self._distto = [None] * self._g.V()

        for i in range(len(self._distto)):
            self._distto[i] = float('-inf')

        self._distto[s] = 0.0
        top = Topological(self._g)
        if not top.has_order():
            raise ValueError('Digraph is not acyclic.')
        for i in top.order():
            self._relax(self._g, i)

    def _relax(self, g, v):
        for e in g.adj(v):
            w = e.To()
            if self._distto[w] < self._distto[v] + e.weight():
                self._distto[w] = self._distto[v] + e.weight()
                self._edgeto[w] = e

    def distTo(self, v):
        return self._distto[v]

    def hasPathTo(self, v):
        return self._distto[v] < float('inf')

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        stack = Stack()
        e = self._edgeto[v]
        while e.From() is not None:
            w = e.From()
            stack.push(e)
            e = self._edgeto[w]
        return stack


class CPM:
    def __init__(self, text):
        self._read(text)
        self._cpm()

    def _read(self, text):
        def stripped_lines(f):
            return (l.rstrip("\n") for l in f)

        with open(text) as file:
            lines = stripped_lines(file)

            V = int(next(lines))
            self._g = EdgeWeightedDigraph(2 * V + 2)
            self._s = 2 * V
            self._t = 2 * V + 1

            for i, line in enumerate(lines):
                line = line.split(' ')
                duration = float(line[0])
                self._g.add_edge(DirectedEdge(i, i + V, duration))
                self._g.add_edge(DirectedEdge(self._s, i, 0))
                self._g.add_edge(DirectedEdge(i + V, self._t, 0))
                for successor in line[2:]:
                    self._g.add_edge(DirectedEdge(i + V, successor, 0))

    def _cpm(self):
        self._lp = AcyclicLP(self._g, self._s)

    def start_time(self, v):
        return self._lp._distto[v]

    def finish_time(self):
        return self._lp._distto[self._t]


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


class BellmanFordSP:
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self._cost = 0
        self._cycle = None
        self._bellmanfordsp()

    def _bellmanfordsp(self):
        # This algorithm relaxes each edge so it doesn't need PQ,
        # and that is also the reason why we don't change dist in PQ.
        self._q = Queue()
        self._onq = [False] * self._g.V()
        self._edgeto = [None] * self._g.V()
        self._distto = [None] * self._g.V()

        for i in range(len(self._distto)):
            self._distto[i] = float('inf')

        while not self._q.is_empty() and not self.has_negative_cycle():
            v = self._q.dequeue()
            self._onq[v] = False
            self._relax(self._g, v)

    def _relax(self, g, v):
        for e in g.adj(v):
            w = e.To()
            if self._distto[w] > self._distto[v] + e.weight():
                self._distto[w] = self._distto[v] + e.weight()
                if not self._onq[w]:
                    self._q.enqueue(w)
                    self._onq[w] = True
        self._cost += 1
        if self._cost % g.V() == 0:
            self.find_negative_cycle()
            if self.has_negative_cycle():
                return

    def has_negative_cycle(self):
        return self._cycle is not None

    def find_negative_cycle(self):
        ewd = EdgeWeightedDigraph(self._g.V())
        for v in range(self._g.V()):
            e = self._edgeto[v]
            if e is not None:
                ewd.add_edge(e)
        finder = EdgeWeightedDirectedCycle(ewd)
        self._cycle = finder.has_cycle()
