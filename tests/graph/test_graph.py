from src.graph.base import Graph
from src.graph.others import CC
from src.graph.paths import (BreadthFirstPaths, DepthFirstPaths,
                             DepthFirstSearch)

from .utils import generate_path


class TestGraph:
    def test_v(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        assert g.V() == 13

    def test_e(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        assert g.E() == 13

    def test_adj(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        adj = [i for i in g.adj(0)]
        assert adj == [6, 2, 1, 5]


class TestDepthFirstSearch:
    def test_count(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        s = DepthFirstSearch(g, 0)
        assert s.count() == 7

    def test_marked(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        s = DepthFirstSearch(g, 0)
        assert s.marked(6)
        assert not s.marked(9)


class TestDepthFirstPaths:
    def test_has_path_to(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        p = DepthFirstPaths(g, 0)
        assert p.hasPathTo(6)

    def test_path_to(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        p = DepthFirstPaths(g, 0)
        paths = [i for i in p.pathTo(4)]
        assert paths == [0, 6, 4] or paths == [0, 5, 4]


class TestBreadthFirstPaths:
    def test_has_path_to(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        p = BreadthFirstPaths(g, 0)
        assert p.hasPathTo(6)

    def test_path_to(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        p = BreadthFirstPaths(g, 0)
        paths = [i for i in p.pathTo(4)]
        assert paths == [0, 6, 4] or paths == [0, 5, 4]


class TestCC:
    def test_connected(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        cc = CC(g)
        assert cc.connected(0, 4)
        assert not cc.connected(0, 9)

    def test_count(self):
        file_path = generate_path('files/tinyG.txt')
        with open(file_path, 'r') as f:
            g = Graph.from_file(f)
        cc = CC(g)
        assert cc.count() == 3
