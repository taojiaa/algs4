from src.fundamental.Stack import Stack


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
