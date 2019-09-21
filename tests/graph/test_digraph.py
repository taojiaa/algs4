from src.graph.Digraph import (DepthFirstOrder, Digraph, DirectedCycle,
                               DirectedDFS, KosarajuSCC, Topological)
from .utils import construct_graph


class TestDigraph:
    def test_init(self):
        g = construct_graph(10, Digraph)
        assert len(g._adj) == 10

    def test_v(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        assert g.V() == 13

    def test_e(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        assert g.E() == 22

    def test_adj(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        assert list(g.adj(0)) == [5, 1]

    def test_indegree(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        assert g.indegree(4) == 3

    def test_outdegree(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        assert g.outdegree(4) == 2


class TestDirectedDFS:
    def test_count(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        s = DirectedDFS(g, 0)
        assert s.count() == 6

    def test_marked(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        s = DirectedDFS(g, 0)
        assert s.marked(2)
        assert not s.marked(6)


class TestCycle:
    def test_has_cycle(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        s = DirectedCycle(g)
        assert s.has_cycle()

    def test_cycle(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        s = DirectedCycle(g)
        assert list(s.cycle()) == [3, 5, 4, 3]


class TestDepthFirstOrder:
    def test_pre(self):
        g = construct_graph('files/tinyDG2.txt', Digraph)
        dfo = DepthFirstOrder(g)
        assert list(dfo.pre()) == [0, 5, 4, 1, 6, 9, 11, 12, 10, 2, 3, 7, 8]

    def test_post(self):
        g = construct_graph('files/tinyDG2.txt', Digraph)
        dfo = DepthFirstOrder(g)
        assert list(dfo.post()) == [4, 5, 1, 12, 11, 10, 9, 6, 0, 3, 2, 7, 8]

    def test_reverse_post(self):
        g = construct_graph('files/tinyDG2.txt', Digraph)
        dfo = DepthFirstOrder(g)
        assert list(dfo.reverse_post()) == [8, 7, 2, 3, 0, 6, 9, 10, 11, 12, 1, 5, 4]


class TestTopological:
    def test_order_dag(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        t = Topological(g)
        assert t.order() is None

    def test_is_dag_dag(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        t = Topological(g)
        assert not t.is_dag()

    def test_order_not_dag(self):
        g = construct_graph('files/tinyDG2.txt', Digraph)
        t = Topological(g)
        assert list(t.order()) == [8, 7, 2, 3, 0, 6, 9, 10, 11, 12, 1, 5, 4]

    def test_is_dag_not_dag(self):
        g = construct_graph('files/tinyDG2.txt', Digraph)
        t = Topological(g)
        assert t.is_dag()


class TestKosarajuSCC:
    def test_count(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        scc = KosarajuSCC(g)
        assert scc.count() == 5

    def test_connected(self):
        g = construct_graph('files/tinyDG.txt', Digraph)
        scc = KosarajuSCC(g)
        assert scc.connected(2, 3)
        assert not scc.connected(0, 9)
