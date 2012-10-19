# This is the program as it was posted on codereview.SE 
# (with some minor formatting changes)

from numbers import Number

test2DMat = [[1,2,3],
             [4,5,6],
             [7,8,9]]
test3DMat = [[[1,2,3],
             [4,5,6],
             [7,8,9]],

            [[2,3,4],
             [5,6,7],
             [8,9,0]],

            [[9,8,7],
             [6,5,4],
             [3,2,1]]]

class Dim(list):
    def __new__(cls,inDim):
        # Make sure inDim is iterable
        iter(inDim)

        # If every item in inDim is a number create a Vec
        if all(isinstance(item,Number) for item in inDim):
            #return Vec(inDim)
            return Vec.__new__(cls,inDim)

        # Make sure every item in inDim is iterable
        try:
            for item in inDim: iter(item)
        except TypeError:
            raise TypeError('All items in a Dim must be iterable')

        # Make sure every item in inDim has the same length
        # or that there are zero items in the list
        if len(set(len(item) for item in inDim)) > 1:
            raise ValueError('All lists in a Dim must be the same length')

        # Actually create the Dim because it passed all the tests
        return list.__new__(cls,inDim)

    def __init__(self,inDim):
        inDim = map(Dim,inDim)
        list.__init__(self,inDim)


class Vec(Dim):
    def __new__(cls,inDim):
        if cls.__name__ not in [Vec.__name__,Dim.__name__]:
            newMat = list.__new__(Vec,inDim)
            newMat.__init__(inDim)
            return newMat
        return list.__new__(Vec,inDim)

    def __init__(self,inDim):
        list.__init__(self,inDim)


class Matrix(Dim):
    def __new__(cls,inMat):
        return Dim.__new__(cls,inMat)

    def __init__(self,inMat):
        super(Matrix,self).__init__(inMat)
