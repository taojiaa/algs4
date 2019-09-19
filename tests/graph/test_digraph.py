import os
from pathlib import Path

from src.graph.Digraph import Digraph


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

