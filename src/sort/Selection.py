from .Base import Sort


class Selection(Sort):

    def __init__(self):
        super(Selection, self).__init__()

    def sort(self, array):
        for i in range(len(array)):
            cur_min = i
            for j in range(i + 1, len(array)):
                if array[j] < array[cur_min]:
                    cur_min = j
            array[i], array[cur_min] = array[cur_min], array[i]
        return array
