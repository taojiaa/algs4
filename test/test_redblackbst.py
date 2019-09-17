import pytest

from src.search.RedBlackBST import RedBlackBST

from .base_search import SortedSymbolTableTest


@pytest.fixture
def test_class():
    return RedBlackBST


class TestRedBlackBST(SortedSymbolTableTest):
    pass
