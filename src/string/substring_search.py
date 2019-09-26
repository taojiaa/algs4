class Brute:
    def __init__(self):
        pass

    def search_1(self, pat: str, text: str) -> int:
        m, n = len(pat), len(text)
        for i in range(n - m + 1):
            for j in range(m):
                if text[i + j] != pat[j]:
                    break
            else:
                return i
        return n

    def search_2(self, pat: str, text: str) -> int:
        m, n = len(pat), len(text)
        i, j = 0, 0
        while i < n and j < m:
            if text[i] == pat[j]:
                j += 1
            else:
                i -= j
                j = 0
            i += 1
        if j == m:
            return i - m
        else:
            return n


class KMP:
    R = 256

    def __init__(self, pat: str):
        self._pat = pat
        self._kmp()

    def _charAt(self, c):
        return ord(c)

    def _kmp(self):
        m = len(self._pat)
        self._dfa = [[0] * m for _ in range(KMP.R)]
        self._dfa[self._charAt(self._pat[0])][0] = 1
        x = 0
        for j in range(1, m):
            for c in range(KMP.R):
                self._dfa[c][j] = self._dfa[c][x]
            self._dfa[self._charAt(self._pat[j])][j] = j + 1
            x = self._dfa[self._charAt(self._pat[j])][x]

    def search(self, text: str) -> int:
        m, n = len(self._pat), len(text)
        i = j = 0
        while i < n and j < m:
            j = self._dfa[self._charAt(text[i])][j]
            i += 1
        if j == m:
            return i - m
        else:
            return n


class BoyerMoore:
    R = 256

    def __init__(self, pat: str):
        self._pat = pat
        self._boyermoore()

    def _charAt(self, c):
        return ord(c)

    def _boyermoore(self):
        m = len(self._pat)
        self._right = [-1] * BoyerMoore.R
        for j in range(m):
            self._right[self._charAt(self._pat[j])] = j

    def search(self, text: str) -> int:
        m, n = len(self._pat), len(text)
        i = 0
        while i <= n - m:
            skip = 0
            for j in range(m - 1, -1, -1):
                if text[i + j] != self._pat[j]:
                    skip = j - self._right[self._charAt(text[i + j])]
                    if skip < 1:
                        skip = 1
                    break
            if skip == 0:
                return i
            i += skip
        return n
