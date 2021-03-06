from abc import ABC, abstractmethod


class StringST(ABC):

    @abstractmethod
    def __init__(self):
        '''
        create a symbol table.
        '''
        pass

    @abstractmethod
    def get(self, key):
        '''
        value paired with key (null if key is absent).
        '''
        pass

    @abstractmethod
    def put(self, key, val):
        '''
        put key-value pair into the table (remove key if value is null)
        '''
        pass

    @abstractmethod
    def delete(self, key):
        '''
        remove key (and its value).
        '''
        pass

    @abstractmethod
    def contains(self, key):
        '''
        is there a value paired with key?
        '''
        pass

    @abstractmethod
    def is_empty(self):
        '''
        is the table empty?
        '''
        pass

    @abstractmethod
    def longest_prefix_of(self, s):
        '''
        the longest key that is a prefix of s.
        '''
        pass

    @abstractmethod
    def keys_with_prefix(self, s):
        '''
        all the keys having s as a prefix.
        '''
        pass

    @abstractmethod
    def keys_that_match(self, s):
        '''
        all the keys that match s (where . matches any character).
        '''
        pass

    @abstractmethod
    def size(self):
        '''
        number of key-value pairs.
        '''
        pass

    @abstractmethod
    def keys(self):
        '''
        all the keys in the table.
        '''
        pass
