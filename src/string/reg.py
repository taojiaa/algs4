from src.fundamental.Bag import Bag
from src.fundamental.Stack import Stack
from src.graph.base import Digraph
from src.graph.paths import DirectedDFS


class NFA:
    def __init__(self, regexp):
        self._re = regexp
        self._m = len(self._re)
        self._nfa()

    def _nfa(self):
        ops = Stack()
        self._g = Digraph(self._m + 1)

        for i in range(self._m):
            lp = i
            c = self._re[i]
            if c == '(' or c == '|':
                ops.push(i)
            elif c == ')':
                o = ops.pop()
                if self._re[o] == '|':
                    lp = ops.pop()
                    self._g.add_edge(lp, o + 1)
                    self._g.add_edge(o, i)
                else:
                    lp = o
            if i < self._m - 1 and self._re[i + 1] == '*':
                self._g.add_edge(lp, i + 1)
                self._g.add_edge(i + 1, lp)
            if c == '(' or c == '*' or c == ')':
                self._g.add_edge(i, i + 1)

    def recognizes(self, text):
        pc = Bag()
        dfs = DirectedDFS(self._g, 0)
        for v in range(self._g.V()):
            if dfs.marked(v):
                pc.add(v)
        for i in range(len(text)):
            match = Bag()
            for v in pc:
                if v < self._m:
                    if self._re[v] == text[i] or self._re[v] == '.':
                        match.add(v + 1)
            pc = Bag()
            dfs = DirectedDFS(self._g, match)
            for v in range(self._g.V()):
                if dfs.marked(v):
                    pc.add(v)
        for v in pc:
            if v == self._m:
                return True
        return False
