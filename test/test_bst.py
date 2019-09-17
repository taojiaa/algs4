import pytest

from src.search.BST import BST

from .base_search import SortedSymbolTableTest


@pytest.fixture
def test_class():
    return BST


class TestBST(SortedSymbolTableTest):
    pass
