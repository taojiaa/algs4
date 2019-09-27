from src.string.reg import NFA


class TestNFA:
    def test_recognizes_1(self):
        text = 'abcbcbcdaaaabcbcdaaaddd'
        reg = '(a|(bc)*d)*'
        nfa = NFA(reg)
        assert nfa.recognizes(text)

    def test_recognizes_2(self):
        text = 'abcbcbcdaaaabcbcdaaaeddd'
        reg = 'ed'
        nfa = NFA(reg)
        assert nfa.recognizes(text)
