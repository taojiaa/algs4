from src.graph.SP import AcyclicSP, DijkstraSP
from src.graph.Digraph import EdgeWeightedDigraph
from src.graph.base import DirectedEdge

from .utils import construct_graph


class TestEdgeWeightedDigraph:
    def test_init(self):
        g = construct_graph(10, EdgeWeightedDigraph)
        e = DirectedEdge(1, 2, 0.5)
        g.add_edge(e)
        assert g.V() == 10
        assert g.E() == 1


class TestDijkstraSP:
    def test_distto(self):
        g = construct_graph('files/tinyEWD.txt', EdgeWeightedDigraph)
        sp = DijkstraSP(g, 0)
        assert sp.distTo(4) == 0.38
        assert sp.distTo(1) == 1.05


class TestAcyclicSP:
    def test_distto(self):
        g = construct_graph('files/tinyEWDAG.txt', EdgeWeightedDigraph)
        sp = AcyclicSP(g, 5)
        assert sp.distTo(0) == 0.73
        assert sp.distTo(4) == 0.35

