from src.fundamental.Queue import Queue
from src.fundamental.Stack import Stack


class DepthFirstSearch:
    def __init__(self, G, s):
        self._g = G
        self._s = s
        self._depthfirstsearch()

    def _depthfirstsearch(self):
        self._marked = [False] * self._g.V()
        self._count = 0
        if isinstance(self._s, int):
            self._dfs(self._g, self._s)
        else:
            for source in self._s:
                if not self._marked[source]:
                    self._dfs(self._g, source)

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


class DirectedDFS(DepthFirstSearch):
    def __init__(self, G, s):
        self._cycle = None
        super().__init__(G, s)


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
        self._marked[self._s] = True
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
