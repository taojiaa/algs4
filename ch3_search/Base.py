from abc import ABC, abstractmethod


class SymbolTable(ABC):

    @abstractmethod
    def size(self):
        '''
        number of key-value pairs in the table
        '''
        pass

    @abstractmethod
    def is_empty(self):
        '''
        is the table empty?
        '''
        pass

    @abstractmethod
    def contains(self, key):
        '''
        is there a value paired with key?
        '''
        pass

    @abstractmethod
    def get(self, key):
        '''
        value paired with key (null if key is absent)
        '''
        pass

    @abstractmethod
    def put(self, key, value):
        '''
        put key-value pair into the table (remove key from table if value is null)
        '''
        pass

    @abstractmethod
    def delete(self, key):
        '''
        remove key (and its value) from table
        '''
        pass


class UnsortedSymbolTable(SymbolTable):

    @abstractmethod
    def keys(self):
        '''
        all the keys in the table
        '''
        pass


class SortedSymbolTable(SymbolTable):

    @abstractmethod
    def min(self):
        '''
        smallest key
        '''
        pass

    @abstractmethod
    def max(self):
        '''
        largest key
        '''
        pass

    @abstractmethod
    def delete_min(self, key):
        '''
        delete smallest key
        '''
        pass

    @abstractmethod
    def delete_max(self, key):
        '''
        delete largest key
        '''
        pass

    @abstractmethod
    def rank(self, key):
        pass

    @abstractmethod
    def floor(self, key):
        '''
        largest key less than or equal to key
        '''
        pass

    @abstractmethod
    def ceiling(self, key):
        '''
        smallest key greater than or equal to key
        '''
        pass

    @abstractmethod
    def select(self, key):
        '''
        key of rank k
        '''
        pass

    @abstractmethod
    def keys(self):
        '''
        all keys in the table, in sorted order
        '''
        pass

    @abstractmethod
    def range_size(self, lo, hi):
        '''
        number of keys in [lo..hi]
        '''
        pass

    @abstractmethod
    def range_keys(self, lo, hi):
        '''
        keys in [lo..hi], in sorted order
        '''
        pass
