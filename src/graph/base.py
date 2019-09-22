from src.fundamental.Bag import Bag

from .utils import words_gen


class Graph:
    # Only allows int val to identify vertex
    def __init__(self, _input):
        if isinstance(_input, int):
            self._v = _input
            self._e = 0
            self._adj = [Bag() for i in range(self._v)]
        else:
            if isinstance(_input, str) and '.txt' in _input:
                self._read(_input)

    def _read(self, text):
        with open(text, 'r') as file:
            words = words_gen(file)
            self._v = int(next(words))
            self._e = 0
            self._adj = [Bag() for i in range(self._v)]

            num_e = int(next(words))
            for _ in range(num_e):
                v = int(next(words))
                w = int(next(words))
                self.add_edge(v, w)

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
