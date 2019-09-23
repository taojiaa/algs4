from random import shuffle


class LSD:
    def __init__(self):
        self._R = 256

    def _charAt(self, c):
        return ord(c)

    def sort(self, a, w):
        n = len(a)
        aux = [None] * n
        for d in range(w - 1, -1, -1):
            count = [0] * (self._R + 1)
            for i in range(n):
                count[self._charAt(a[i][d]) + 1] += 1
            for i in range(self._R):
                count[i + 1] += count[i]
            for i in range(n):
                ind = self._charAt(a[i][d])
                aux[count[ind]] = a[i]
                count[ind] += 1
            for i in range(n):
                a[i] = aux[i]
        return a

    def is_sorted(self, a):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True


class MSD:
    def __init__(self):
        self._R = 256
        self._M = 2

    def _charAt(self, s, d):
        return ord(s[d]) if d < len(s) else -1

    def sort(self, a):
        n = len(a)
        self._aux = [None] * n
        self._sort(a, 0, n - 1, 0)
        return a

    def _sort(self, a, lo, hi, d):
        if hi < lo + self._M:
            self._insert_sort(a, lo, hi, d)
            return
        count = [0] * (self._R + 2)
        for i in range(lo, hi + 1):
            count[self._charAt(a[i], d) + 2] += 1
        for i in range(self._R + 1):
            count[i + 1] += count[i]
        for i in range(lo, hi + 1):
            ind = self._charAt(a[i], d) + 1
            self._aux[count[ind]] = a[i]
            count[ind] += 1
        for i in range(lo, hi + 1):
            a[i] = self._aux[i - lo]

        for r in range(self._R):
            self._sort(a, lo + count[r], lo + count[r + 1] - 1, d + 1)

    def _insert_sort(self, a, lo, hi, d):
        for i in range(lo, hi + 1):
            for j in range(i, lo, -1):
                if self._less(a[j], a[j - 1], d):
                    a[j], a[j - 1] = a[j - 1], a[j]
                else:
                    break

    # insertion sort a[lo..hi], starting at dth character
    def _less(self, s1, s2, d):
        for i in range(d, min(len(s1), len(s2))):
            if s1[i] < s2[i]:
                return True
            if s1[i] > s2[i]:
                return False
        return len(s1) < len(s2)

    def is_sorted(self, a):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True


class Quick3String:
    def __init__(self):
        pass

    def _charAt(self, s, d):
        return ord(s[d]) if d < len(s) else -1

    def sort(self, a):
        shuffle(a)
        self._sort(a, 0, len(a) - 1, 0)
        return a

    def _sort(self, a, lo, hi, d):
        if lo >= hi:
            return
        p = lo
        p_1, p_2 = lo + 1, hi
        while p_1 <= p_2:
            t = self._charAt(a[p_1], d)
            v = self._charAt(a[p], d)
            if t < v:
                a[p_1], a[p] = a[p], a[p_1]
                p = p + 1
                p_1 = p_1 + 1
            elif t > v:
                a[p_1], a[p_2] = a[p_2], a[p_1]
                p_2 = p_2 - 1
            else:
                p_1 = p_1 + 1

        self._sort(a, lo, p - 1, d)
        if v >= 0:
            self._sort(a, p, p_2, d + 1)
        self._sort(a, p_2 + 1, hi, d)

    def is_sorted(self, a):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True
