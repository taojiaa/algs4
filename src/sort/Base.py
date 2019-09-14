class Sort:

    def __init__(self):
        pass

    def sort(self, a):
        pass

    def is_sorted(self, a):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True
    
