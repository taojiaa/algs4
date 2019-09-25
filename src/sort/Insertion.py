from .Base import Sort


# Note that the numbers of comparison and exchange are totolly different
# between Selection and Insertion.
class Insertion(Sort):

    def __init__(self):
        super(Insertion, self).__init__()

    def sort(self, array):
        for i in range(len(array)):
            for j in range(i, 0, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    # If the current inserted element is largter than the one on the left,
                    # there is no need to compare them any more (already sorted).
                    break
        return array


class Shells(Sort):

    def __init__(self):
        super(Shells, self).__init__()

    def sort(self, array):
        h = 1
        while h < len(array) // 3:
            h = h * 3 + 1
        while h >= 1:
            for i in range(0, len(array)):
                for j in range(i, h - 1, -h):
                    if array[j] < array[j - h]:
                        array[j], array[j - h] = array[j - h], array[j]
                    else:
                        break
            h = h // 3
        return array
