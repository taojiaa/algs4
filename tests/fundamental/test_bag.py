from src.fundamental.Bag import Bag


def initiate():
    bag = Bag()
    for i in range(10):
        bag.add(i)
    return bag


class TestBag:

    def test_size(self):
        bag = initiate()
        assert bag.size() == 10

    def test_empty(self):
        bag = Bag()
        assert bag.is_empty()
        bag = initiate()
        assert not bag.is_empty()

    def test_iter(self):
        bag = initiate()
        vals = []
        for item in bag:
            vals.append(item)
        assert vals == list(range(10))[::-1]

