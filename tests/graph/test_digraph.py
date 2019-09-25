from src.graph.base import Digraph
from src.graph.cycle import DirectedCycle
from src.graph.order import DepthFirstOrder, Topological
from src.graph.others import KosarajuSCC
from src.graph.paths import DirectedDFS

from .utils import generate_path


class TestDigraph:
    def test_init(self):
        g = Digraph(10)
        assert len(g._adj) == 10

    def test_v(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        assert g.V() == 13

    def test_e(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        assert g.E() == 22

    def test_adj(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        assert list(g.adj(0)) == [5, 1]

    def test_indegree(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        assert g.indegree(4) == 3

    def test_outdegree(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        assert g.outdegree(4) == 2


class TestDirectedDFS:
    def test_count(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        s = DirectedDFS(g, 0)
        assert s.count() == 6

    def test_marked(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        s = DirectedDFS(g, 0)
        assert s.marked(2)
        assert not s.marked(6)


class TestCycle:
    def test_has_cycle(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        s = DirectedCycle(g)
        assert s.has_cycle()

    def test_cycle(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        s = DirectedCycle(g)
        assert list(s.cycle()) == [3, 5, 4, 3]


class TestDepthFirstOrder:
    def test_pre(self):
        file_path = generate_path('files/tinyDG2.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        dfo = DepthFirstOrder(g)
        assert list(dfo.pre()) == [0, 5, 4, 1, 6, 9, 11, 12, 10, 2, 3, 7, 8]

    def test_post(self):
        file_path = generate_path('files/tinyDG2.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        dfo = DepthFirstOrder(g)
        assert list(dfo.post()) == [4, 5, 1, 12, 11, 10, 9, 6, 0, 3, 2, 7, 8]

    def test_reverse_post(self):
        file_path = generate_path('files/tinyDG2.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        dfo = DepthFirstOrder(g)
        assert list(dfo.reverse_post()) == [8, 7, 2, 3, 0, 6, 9, 10, 11, 12, 1, 5, 4]


class TestTopological:
    def test_order_dag(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        t = Topological(g)
        assert t.order() is None

    def test_is_dag_dag(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        t = Topological(g)
        assert not t.is_dag()

    def test_order_not_dag(self):
        file_path = generate_path('files/tinyDG2.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        t = Topological(g)
        assert list(t.order()) == [8, 7, 2, 3, 0, 6, 9, 10, 11, 12, 1, 5, 4]

    def test_is_dag_not_dag(self):
        file_path = generate_path('files/tinyDG2.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        t = Topological(g)
        assert t.is_dag()


class TestKosarajuSCC:
    def test_count(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        scc = KosarajuSCC(g)
        assert scc.count() == 5

    def test_connected(self):
        file_path = generate_path('files/tinyDG.txt')
        with open(file_path, 'r') as f:
            g = Digraph.from_file(f)
        scc = KosarajuSCC(g)
        assert scc.connected(2, 3)
        assert not scc.connected(0, 9)
