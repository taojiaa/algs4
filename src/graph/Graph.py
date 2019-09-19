from src.fundamental.Bag import Bag
from src.fundamental.Stack import Stack
from src.fundamental.Queue import Queue
from .base_undirected_graph import Search, Paths


class Graph:

    # Only allows int val to identify node

    def __init__(self, num_v=None, text=None):
        if text:
            self._e = 0
            self._init_from_text(text)
        elif num_v:
            self._e = 0
            self._v = num_v

    def _init_from_text(self, text):
        def words_gen(fileobj):
            for line in fileobj:
                for word in line.split():
                    yield int(word)

        with open(text, 'r') as file:
            words = words_gen(file)
            self._v = next(words)
            e = next(words)

            self._adj = [None] * self._v

            for i in range(self._v):
                self._adj[i] = Bag()

            for i in range(e):
                v = next(words)
                w = next(words)
                self.add_edge(v, w)

    def V(self):
        return self._v

    def E(self):
        return self._e

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._e = self._e + 1

    def adj(self, v):
        return self._adj[v]

    def degree(self, v):
        return self._adj[v].size()

    def __repr__(self):
        s = ''
        s = s + (self._v + " vertices, " + self._e + " edges " + '\n')
        for i in range(self._v):
            s = s + (i + ": ")
            for w in self._adj[i]:
                s = s + (w + " ")
            s = s + '\n'
        return s


class DepthFirstSearch(Search):
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self.dfs()

    def dfs(self):
        self._marked = [False] * self._g.V()
        self._count = 0
        self._dfs(self._g, self._s)

    def _dfs(self, g, v):
        self._marked[v] = True
        self._count += 1
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs(g, w)

    def marked(self, v):
        return self._marked[v]

    def count(self):
        return self._count


class DepthFirstPaths(Paths):
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self.dfs()

    def dfs(self):
        self._marked = [False] * self._g.V()
        self._edgeto = [False] * self._g.V()
        self._dfs(self._g, self._s)

    def _dfs(self, g, v):
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked[w]:
                self._edgeto[w] = v
                self._dfs(g, w)

    def hasPathTo(self, v):
        return self._marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = Stack()
        while v != self._s:
            path.push(v)
            v = self._edgeto[v]
        path.push(self._s)
        return path


class BreadthFirstPaths(Paths):
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self.bfs()

    def bfs(self):
        self._queue = Queue()
        self._marked = [None] * self._g.V()
        self._edgeto = [None] * self._g.V()
        self._queue.enqueue(self._s)
        while not self._queue.is_empty():
            v = self._queue.dequeue()
            for w in self._g.adj(v):
                if not self._marked[w]:
                    self._edgeto[w] = v
                    self._marked[w] = True
                    self._queue.enqueue(w)

    def hasPathTo(self, v):
        return self._marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = Stack()
        while v != self._s:
            path.push(v)
            v = self._edgeto[v]
        path.push(self._s)
        return path


class CC:
    def __init__(self, G):
        self._g = G
        self._count = 0
        self.dfs()

    def dfs(self):
        # The components are different from the previous one,
        # becasue it doesn't specify that connected to 0 or one specific node.
        self._marked = [None] * self._g.V()
        self._id = [None] * self._g.V()
        for s in range(self._g.V()):
            if not self._marked[s]:
                # dfs should be eariler than count self-addition,
                # since dfs find all the connected nodes sharing the same id.
                self._dfs(self._g, s)
                self._count += 1

    def _dfs(self, g, v):
        self._marked[v] = True
        self._id[v] = self._count
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs(g, w)

    def connected(self, v, w):
        return self._id[v] == self._id[w]

    def id(self, v):
        return self._id[v]

    def count(self):
        return self._count


class Cycle:
    def __init__(self, G):
        self._g = G
        self._has_cycle = False
        self.dfs()

    def dfs(self):
        self._marked = [None] * self._g.V()
        for s in range(self._g.V()):
            if not self._marked[s]:
                self._dfs(self._g, s, s)

    def _dfs(self, g, v, u):
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs(g, w, v)
            else:
                if w != u:
                    self._has_cycle = True

    def has_cycle(self):
        return self._has_cycle


class TwoColor:
    def __init__(self, G):
        self._g = G
        self._is_twocolorable = True
        self.dfs()

    def dfs(self):
        self._marked = [None] * self._g.V()
        self._colors = [None] * self._g.V()
        for s in range(self._g.V()):
            if not self._marked[s]:
                self._dfs(self._g, s, s)

    def _dfs(self, g, v, u):
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked[w]:
                self._colors[w] = not self._colors[v]
                self._dfs(g, w, v)
            else:
                if self._colors[w] == self._colors[v]:
                    self._is_twocolorable = False

    def is_bipartite(self):
        return self._is_twocolorable
