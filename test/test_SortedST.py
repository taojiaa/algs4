import pytest

from src.search.BST import BST
from src.search.BinarySearchST import BinarySearchST
from src.search.RedBlackBST import RedBlackBST

from .Base import SortedSymbolTableTest


@pytest.fixture
def test_class():
    return BST


class TestBST(SortedSymbolTableTest):
    pass


@pytest.fixture()
def test_class():
    return BinarySearchST


class TestBinarySearchST(SortedSymbolTableTest):
    pass


@pytest.fixture
def test_class():
    return RedBlackBST


class TestRedBlackBST(SortedSymbolTableTest):
    pass
