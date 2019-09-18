from src.fundamental.Bag import Bag
from src.fundamental.Stack import Stack
from .base_undirected_graph import Search, Paths


class Graph:

    # Only allows int val to identify node

    def __init__(self, num_v=None, text=None):
        if text:
            self.e = 0
            self._init_from_text(text)
        elif num_v:
            self.e = 0
            self.v = num_v

    def _init_from_text(self, text):
        def words_gen(fileobj):
            for line in fileobj:
                for word in line.split():
                    yield int(word)

        with open(text, 'r') as file:
            words = words_gen(file)
            self.v = next(words)
            e = next(words)

            self._adj = [None] * self.v

            for i in range(self.v):
                self._adj[i] = Bag()

            for i in range(e):
                v = next(words)
                w = next(words)
                self.add_edge(v, w)

    def V(self):
        return self.v

    def E(self):
        return self.e

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._adj[w].add(v)
        self.e = self.e + 1

    def adj(self, v):
        return self._adj[v]

    def degree(self, v):
        return self._adj[v].size()

    def __repr__(self):
        s = ''
        s = s + (self.v + " vertices, " + self.e + " edges " + '\n')
        for i in range(self.v):
            s = s + (i + ": ")
            for w in self._adj[i]:
                s = s + (w + " ")
            s = s + '\n'
        return s


class DepthFirstSearch(Search):

    def __init__(self, G, s):
        self.g = G
        self.s = s
        self.dfs()

    def dfs(self):
        self._marked = [False] * self.g.V()
        self._count = 0
        self._dfs(self.g, self.s)

    def _dfs(self, g, v):
        self._marked[v] = True
        self._count = self._count + 1
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs(g, w)

    def marked(self, v):
        return self._marked[v]

    def count(self):
        return self._count


class DepthFirstPaths(Paths):

    def __init__(self, G, s):
        self.g = G
        self.s = s
        self.dfs()

    def dfs(self):
        self._marked = [False] * self.g.V()
        self._edgeto = [False] * self.g.V()
        self._count = 0
        self._dfs(self.g, self.s)

    def _dfs(self, g, v):
        self._marked[v] = True
        self._count = self._count + 1
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
        while v != self.s:
            path.push(v)
            v = self._edgeto[v]
        path.push(self.s)
        return path

