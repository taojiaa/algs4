from src.graph.MST import LazyPrimMST, PrimMST
from src.graph.base import Edge, EdgeWeightedGraph

from .utils import generate_path


class TestEdgeWeightedGraph:
    def test_init(self):
        g = EdgeWeightedGraph(10)
        e = Edge(1, 2, 0.5)
        g.add_edge(e)
        assert g.V() == 10
        assert g.E() == 1


class TestLazyPrimMST:
    def test_weight(self):
        file_path = generate_path('files/tinyEWG.txt')
        with open(file_path, 'r') as f:
            g = EdgeWeightedGraph.from_file(f)
        mst = LazyPrimMST(g)
        assert round(mst.weight(), 2) == 1.81


class TestPrimMST:
    def test_weight(self):
        file_path = generate_path('files/tinyEWG.txt')
        with open(file_path, 'r') as f:
            g = EdgeWeightedGraph.from_file(f)
        mst = PrimMST(g)
        assert round(mst.weight(), 2) == 1.81
