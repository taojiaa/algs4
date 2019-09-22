from .order import DepthFirstOrder


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
