from src.fundamental.Bag import Bag


class Graph:
    def __init__(self, v: int):
        self._v = v
        self._e = 0
        self._adj = [Bag() for i in range(self._v)]

    @classmethod
    def from_file(cls, f):
        v = int(f.readline().strip())
        e = int(f.readline().strip())
        graph = cls(v)
        for i in range(e):
            v, w = f.readline().rstrip('\n').split()
            graph.add_edge(int(v), int(w))
        return graph

    def V(self):
        return self._v

    def E(self):
        return self._e

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._e += 1

    def adj(self, v):
        return self._adj[v]

    def degree(self, v):
        return self._adj[v].size()

    def to_string(self):
        s = ''
        s = s + (self._v + " vertices, " + self._e + " edges " + '\n')
        for i in range(self._v):
            s = s + (i + ": ")
            for w in self._adj[i]:
                s = s + (w + " ")
            s = s + '\n'
        return s


class Digraph:
    def __init__(self, v: int):
        self._v = v
        self._e = 0
        self._adj = [Bag() for i in range(self._v)]
        self._indegree = [0] * self._v

    @classmethod
    def from_file(cls, f):
        v = int(f.readline().strip())
        e = int(f.readline().strip())
        graph = cls(v)
        for i in range(e):
            v, w = f.readline().rstrip('\n').split()
            graph.add_edge(int(v), int(w))
        return graph

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


class EdgeWeightedGraph(Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_file(cls, f):
        v = int(f.readline().strip())
        e = int(f.readline().strip())
        graph = cls(v)
        for i in range(e):
            v, w, ew = f.readline().rstrip('\n').split()
            graph.add_edge(Edge(int(v), int(w), float(ew)))
        return graph

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


class EdgeWeightedDigraph(Digraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_file(cls, f):
        v = int(f.readline().strip())
        e = int(f.readline().strip())
        graph = cls(v)
        for i in range(e):
            v, w, ew = f.readline().rstrip('\n').split()
            graph.add_edge(DirectedEdge(int(v), int(w), float(ew)))
        return graph

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
