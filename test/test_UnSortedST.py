import pytest

from search.SequentialSearchST import SequentialSearchST

from .Base import UnSortedSymbolTableTest


@pytest.fixture
def test_class():
    return SequentialSearchST


class TestBST(UnSortedSymbolTableTest):
    pass
