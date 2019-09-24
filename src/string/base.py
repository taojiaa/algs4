from abc import ABC, abstractclassmethod


class StringST(ABC):

    @abstractclassmethod
    def __init__(self):
        '''
        create a symbol table.
        '''
        pass

    @abstractclassmethod
    def get(self, key):
        '''
        value paired with key (null if key is absent).
        '''
        pass

    @abstractclassmethod
    def put(self, key, val):
        '''
        put key-value pair into the table (remove key if value is null)
        '''
        pass

    @abstractclassmethod
    def delete(self, key):
        '''
        remove key (and its value).
        '''
        pass

    @abstractclassmethod
    def contains(self, key):
        '''
        is there a value paired with key?
        '''
        pass

    @abstractclassmethod
    def is_empty(self):
        '''
        is the table empty?
        '''
        pass

    @abstractclassmethod
    def longest_prefix_of(self, s):
        '''
        the longest key that is a prefix of s.
        '''
        pass

    @abstractclassmethod
    def keys_with_prefix(self, s):
        '''
        all the keys having s as a prefix.
        '''
        pass

    @abstractclassmethod
    def keys_that_match(self, s):
        '''
        all the keys that match s (where . matches any character).
        '''
        pass

    @abstractclassmethod
    def size(self):
        '''
        number of key-value pairs.
        '''
        pass

    @abstractclassmethod
    def keys(self):
        '''
        all the keys in the table.
        '''
        pass
