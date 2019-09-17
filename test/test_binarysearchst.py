import pytest

from src.search.BinarySearchST import BinarySearchST

from .base_search import SortedSymbolTableTest


@pytest.fixture()
def test_class():
    return BinarySearchST


class TestBinarySearchST(SortedSymbolTableTest):
    pass
