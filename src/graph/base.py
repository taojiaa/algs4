from abc import ABC, abstractclassmethod


class Search(ABC):
    '''
    find vertices connected to a source vertex s
    '''

    @abstractclassmethod
    def marked(self, v):
        '''
        is v connected to s?
        '''
        pass

    @abstractclassmethod
    def count(self):
        '''
        how many vertices are connected to s?
        '''
        pass


class Paths(ABC):
    '''
    find paths in G from source s
    '''

    @abstractclassmethod
    def hasPathTo(self, v):
        '''
        is there a path from s to v?
        '''
        pass

    @abstractclassmethod
    def pathTo(self, v):
        '''
        path from s to v; null if no such path
        '''
        pass
