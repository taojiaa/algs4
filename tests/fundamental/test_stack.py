from src.fundamental.Stack import Stack


def initiate():
    stack = Stack()
    for i in range(10):
        stack.push(i)
    return stack


class TestStack:
    def test_size(self):
        stack = initiate()
        assert stack.size() == 10

    def test_empty(self):
        stack = Stack()
        assert stack.is_empty()
        stack = initiate()
        assert not stack.is_empty()

    def test_pop(self):
        stack = initiate()
        assert stack.pop() == 9

    def test_iter(self):
        stack = initiate()
        vals = []
        for item in stack:
            vals.append(item)
        assert vals == list(range(10))[::-1]
