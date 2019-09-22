from src.fundamental.Queue import Queue
from src.fundamental.Stack import Stack


class DepthFirstSearch:
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


class DepthFirstPaths:
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self._depthfirstpaths()

    def _depthfirstpaths(self):
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


class BreadthFirstPaths:
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self._breadthfirstpaths()

    def _breadthfirstpaths(self):
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
        self._cc()

    def _cc(self):
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
        self._cycle()

    def _cycle(self):
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
        self._twocolor()

    def _twocolor(self):
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
