import os
from pathlib import Path

from src.graph.Digraph import (DepthFirstOrder, Digraph, DirectedCycle,
                               DirectedDFS, KosarajuSCC, Topological)


def initiate(file_name):
    root_dir = Path(__file__).resolve().parents[0]
    file_path = os.path.join(root_dir, file_name)
    return Digraph(text=file_path)


class TestDigraph:
    def test_init(self):
        g = Digraph(num_v=10)
        assert len(g._adj) == 10

    def test_v(self):
        g = initiate('files/tinyDG.txt')
        assert g.V() == 13

    def test_e(self):
        g = initiate('files/tinyDG.txt')
        assert g.E() == 22

    def test_adj(self):
        g = initiate('files/tinyDG.txt')
        assert list(g.adj(0)) == [5, 1]


class TestDirectedDFS:
    def test_count(self):
        g = initiate('files/tinyDG.txt')
        s = DirectedDFS(g, 0)
        assert s.count() == 6

    def test_marked(self):
        g = initiate('files/tinyDG.txt')
        s = DirectedDFS(g, 0)
        assert s.marked(2)
        assert not s.marked(6)


class TestCycle:
    def test_has_cycle(self):
        g = initiate('files/tinyDG.txt')
        s = DirectedCycle(g)
        assert s.has_cycle()

    def test_cycle(self):
        g = initiate('files/tinyDG.txt')
        s = DirectedCycle(g)
        assert list(s.cycle()) == [3, 5, 4, 3]


class TestDepthFirstOrder:
    def test_pre(self):
        g = initiate('files/tinyDG2.txt')
        dfo = DepthFirstOrder(g)
        assert list(dfo.pre()) == [0, 5, 4, 1, 6, 9, 11, 12, 10, 2, 3, 7, 8]

    def test_post(self):
        g = initiate('files/tinyDG2.txt')
        dfo = DepthFirstOrder(g)
        assert list(dfo.post()) == [4, 5, 1, 12, 11, 10, 9, 6, 0, 3, 2, 7, 8]

    def test_reverse_post(self):
        g = initiate('files/tinyDG2.txt')
        dfo = DepthFirstOrder(g)
        assert list(dfo.reverse_post()) == [8, 7, 2, 3, 0, 6, 9, 10, 11, 12, 1, 5, 4]


class TestTopological:
    def test_order_dag(self):
        g = initiate('files/tinyDG.txt')
        t = Topological(g)
        assert t.order() is None

    def test_is_dag_dag(self):
        g = initiate('files/tinyDG.txt')
        t = Topological(g)
        assert not t.is_dag()

    def test_order_not_dag(self):
        g = initiate('files/tinyDG2.txt')
        t = Topological(g)
        assert list(t.order()) == [8, 7, 2, 3, 0, 6, 9, 10, 11, 12, 1, 5, 4]

    def test_is_dag_not_dag(self):
        g = initiate('files/tinyDG2.txt')
        t = Topological(g)
        assert t.is_dag()


class TestKosarajuSCC:
    def test_count(self):
        g = initiate('files/tinyDG.txt')
        scc = KosarajuSCC(g)
        assert scc.count() == 5

    def test_strongly_connected(self):
        g = initiate('files/tinyDG.txt')
        scc = KosarajuSCC(g)
        assert scc.strongly_connected(2, 3)
        assert not scc.strongly_connected(0, 9)
