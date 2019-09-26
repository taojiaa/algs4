from src.string.substring_search import Brute, KMP, BoyerMoore


class TestBrute:
    def test_search_1(self):
        sub = Brute()
        pat = 'abracadabra'
        text = 'abacadabrabracabracadabrabrabracad'
        assert sub.search_1(pat, text) == 14

    def test_search_2(self):
        sub = Brute()
        pat = 'abracadabra'
        text = 'abacadabrabracabracadabrabrabracad'
        assert sub.search_2(pat, text) == 14


class TestKMP:
    def test_search(self):
        pat = 'abracadabra'
        text = 'abacadabrabracabracadabrabrabracad'
        sub = KMP(pat)
        assert sub.search(text) == 14


class TestBoyerMoore:
    def test_search(self):
        pat = 'abracadabra'
        text = 'abacadabrabracabracadabrabrabracad'
        sub = BoyerMoore(pat)
        assert sub.search(text) == 14


