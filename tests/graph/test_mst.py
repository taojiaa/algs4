import os
from pathlib import Path

from src.graph.MST import Edge, EdgeWeightGraph, LazyPrimMST


def initiate(file_name):
    root_dir = Path(__file__).resolve().parents[0]
    file_path = os.path.join(root_dir, file_name)
    return EdgeWeightGraph(text=file_path)


class TestEdgeWeightGraph:
    def test_init(self):
        g = EdgeWeightGraph(num_v=10)
        e = Edge(1, 2, 0.5)
        g.add_edge(e)
        assert g.V() == 10
        assert g.E() == 1


class TestLazyPrimMST:

    def test_weight(self):
        g = initiate('files/tinyEWG.txt')
        mst = LazyPrimMST(g)
        assert mst.weight() == 1.81
