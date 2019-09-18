from src.fundamental.Queue import Queue


def initiate():
    stack = Queue()
    for i in range(10):
        stack.enqueue(i)
    return stack


class TestQueue:
    def test_size(self):
        queue = initiate()
        assert queue.size() == 10

    def test_empty(self):
        queue = Queue()
        assert queue.is_empty()
        queue = initiate()
        assert not queue.is_empty()

    def test_pop(self):
        queue = initiate()
        assert queue.dequeue() == 0

    def test_iter(self):
        queue = initiate()
        vals = []
        for item in queue:
            vals.append(item)
        assert vals == list(range(10))
