from src.graph.MST import LazyPrimMST, PrimMST
from src.graph.base import Edge, EdgeWeightedGraph

from .utils import construct_graph


class TestEdgeWeightedGraph:
    def test_init(self):
        g = construct_graph(10, EdgeWeightedGraph)
        e = Edge(1, 2, 0.5)
        g.add_edge(e)
        assert g.V() == 10
        assert g.E() == 1


class TestLazyPrimMST:
    def test_weight(self):
        g = construct_graph('files/tinyEWG.txt', EdgeWeightedGraph)
        mst = LazyPrimMST(g)
        assert round(mst.weight(), 2) == 1.81


class TestPrimMST:
    def test_weight(self):
        g = construct_graph('files/tinyEWG.txt', EdgeWeightedGraph)
        mst = PrimMST(g)
        assert round(mst.weight(), 2) == 1.81
