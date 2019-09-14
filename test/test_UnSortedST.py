import pytest

from src.search.SequentialSearchST import SequentialSearchST

from .base_search import UnSortedSymbolTableTest


@pytest.fixture
def test_class():
    return SequentialSearchST


class TestBST(UnSortedSymbolTableTest):
    pass
