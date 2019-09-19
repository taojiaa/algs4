import os
from pathlib import Path

from src.graph.Digraph import Digraph, DirectedDFS, DirectedCycle, Topological, SCC


def initiate():
    root_dir = Path(__file__).resolve().parents[0]
    file_path = os.path.join(root_dir, 'files/tinyDG.txt')
    return Digraph(text=file_path)


class TestDigraph:
    def test_v(self):
        g = initiate()
        assert g.V() == 13

    def test_e(self):
        g = initiate()
        assert g.E() == 22

    def test_adj(self):
        g = initiate()
        adj = [i for i in g.adj(0)]
        assert adj == [5, 1]


class TestDirectedDFS:
    def test_count(self):
        g = initiate()
        s = DirectedDFS(g, 0)
        assert s.count() == 6

    def test_marked(self):
        g = initiate()
        s = DirectedDFS(g, 0)
        assert s.marked(2)
        assert not s.marked(6)


class TestCycle:
    def test_has_cycle(self):
        g = initiate()
        s = DirectedCycle(g)
        assert s.has_cycle()

    def test_cycle(self):
        g = initiate()
        s = DirectedCycle(g)
        cycle = [i for i in s.cycle()]
        assert cycle == [3, 5, 4, 3]


class TestTopological:
    def test_order(self):
        g = initiate()
        t = Topological(g)
        assert t.order() is None

    def test_is_dag(self):
        g = initiate()
        t = Topological(g)
        assert not t.is_dag()


class TestSCC:
    def test_count(self):
        g = initiate()
        scc = SCC(g)
        assert scc.count() == 6

    def test_strongly_connected(self):
        g = initiate()
        scc = SCC(g)
        assert scc.strongly_connected(2, 3)
        assert not scc.strongly_connected(0, 9)
