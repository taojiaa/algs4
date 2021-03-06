from src.graph.SP import AcyclicSP, DijkstraSP, CPM, BellmanFordSP
from src.graph.base import EdgeWeightedDigraph
from src.graph.base import DirectedEdge

from .utils import generate_path


class TestEdgeWeightedDigraph:
    def test_init(self):
        g = EdgeWeightedDigraph(10)
        e = DirectedEdge(1, 2, 0.5)
        g.add_edge(e)
        assert g.V() == 10
        assert g.E() == 1


class TestDijkstraSP:
    def test_distto(self):
        file_path = generate_path('files/tinyEWD.txt')
        with open(file_path, 'r') as f:
            g = EdgeWeightedDigraph.from_file(f)
        sp = DijkstraSP(g, 0)
        assert sp.distTo(4) == 0.38
        assert sp.distTo(1) == 1.05


class TestAcyclicSP:
    def test_distto(self):
        file_path = generate_path('files/tinyEWDAG.txt')
        with open(file_path, 'r') as f:
            g = EdgeWeightedDigraph.from_file(f)
        sp = AcyclicSP(g, 5)
        assert sp.distTo(0) == 0.73
        assert sp.distTo(4) == 0.35


class TestCPM:
    def test_start_time(self):
        file_path = generate_path('files/jobsPC.txt')
        cpm = CPM(file_path)
        assert cpm.start_time(1) == 41
        assert cpm.start_time(2) == 123

    def test_finish_time(self):
        file_path = generate_path('files/jobsPC.txt')
        cpm = CPM(file_path)
        assert cpm.finish_time() == 173


class TestBellmanFordSP:
    def test_distto(self):
        file_path = generate_path('files/tinyEWDAG.txt')
        with open(file_path, 'r') as f:
            g = EdgeWeightedDigraph.from_file(f)
        bsp = BellmanFordSP(g, 0)
        assert bsp.distTo(2) == 0.26
