from numbers import Number
import itertools as IT

test2DMat = [[1,2,3],[4,5,6],[7,8,9]]
test3DMat = [[[1,2,3],[4,5,6],[7,8,9]],[[2,3,4],[5,6,7],[8,9,0]],[[9,8,7],[6,5,4],[3,2,1]]]
test3DLop = [[[1],[4]],[[2],[5]],[[9],[6]]]
DEBUG = False

class Dim(list):
    def __new__(cls,inDim):
        if DEBUG: print 'new dim'
        inDim = list(inDim)

        # If every item in inDim is a number create a Vec
        if all(isinstance(item,Number) for item in inDim):
            #return Vec(inDim)
            return Vec.__new__(cls,inDim)

        # Otherwise create a Dim
        newDim = list.__new__(cls,inDim)
        setattr(newDim,'UI',None)
        newDim.__init__(inDim)
        return newDim

    def __init__(self,inDim):
        if hasattr(self,'UI'):
            delattr(self,'UI')
            if DEBUG: print 'init dim'

            # Make sure every item in inDim is iterable
            try:
                for item in inDim: iter(item)
            except TypeError:
                raise TypeError('Each element in a {0} must be iterable'
                        .format(type(self).__name__))

            # Make sure every item in inDim has the same length
            # or that there are zero items in the list
            if len(set(len(item) for item in inDim)) > 1:
                raise ValueError('Each element in a {0} must be the same '
                        'length'.format(type(self).__name__))

            inDim = map(Dim,inDim)
            list.__init__(self,inDim)

    ##### Magic Methods #####
    def __getitem__(self,key):
        if isinstance(key,tuple):
            key = key[0]
        return super(Dim,self).__getitem__(key)


    ##### Math Methods #####
    def __add__(self,other):
        pass
    def __radd__(self,other):
        pass

    def __sub__(self,other):
        pass
    def __rsub__(self,other):
        pass


class Vec(Dim):
    def __new__(cls,inDim):
        if DEBUG: print 'new Vec'
        if isinstance(cls,Dim):
            newVec = list.__new__(Vec,inDim)
            newVec.__init__(inDim)
            return newVec
        return list.__new__(Vec,inDim)

    def __init__(self,inDim):
        if DEBUG: print 'init vec',inDim
        list.__init__(self,inDim)

    def size(self,dim=0):
        if dim > 0:
            return 1
        elif dim < 0:
            raise ValueError('paramater to size() cannot be negative')
        return len(self)


class Matrix(Dim):
    def __new__(cls,inMat):
        if DEBUG: print 'new matrix'
        if not isinstance(inMat,(list,tuple)):
            try:
                inMat = tuple(inMat)
            except TypeError:
                return inMat
        newMat = Dim.__new__(cls,inMat)
        setattr(newMat,'uninitialized',None)
        newMat.__init__(inMat)
        return newMat

    def __init__(self,inMat):
        if hasattr(self,'uninitialized'):
            delattr(self,'uninitialized')
            if DEBUG: print 'init matrix'
            super(Matrix,self).__init__(inMat)


    ##### Public Methods #####
    def size(self,dim=None):
        """Get the requested dimension of a matrix"""
        if dim is None:
            dims = []
            while True:
                try:
                    dims.append(len(self))
                except TypeError:
                    break
                self = self[0]
            return tuple(dims)
        elif dim > 0:
            return self[0].size(dim-1)
        elif dim == 0:
            return len(self)
        else:
            raise ValueError('parameter to size() cannot be negative')

    def transpose(self):
        return Matrix(IT.izip(*self))

    def inverse(self):
        pass

    #todo: finish
    def det(self):
        """Calculate the determinant of a matrix"""
        # Make sure the matrix is square
        if self.size(0) != self.size(1):
            raise TypeError('Determinant only defined on square matrices')

    #todo: figure out what this actually is (because its not a minor)
    def minor(self,(i,j)):
        """Return the requested minor of a matrix"""
        y = self[:]
        del(y[i-1])
        y = self.transpose()
        del(y[j-1])
        return zip(*y)

    def ref(self):
        """Return a row echelon form matrix"""
        pass

    def rref(self):
        """Return a reduced row echelon form matrix"""
        pass

    def gauss_jordan(m, eps = 1.0/(10**10)):
        """Puts given matrix (2D array) into the Reduced Row Echelon Form.
        Returns True if successful, False if 'm' is singular.
        NOTE: make sure all the matrix items support fractions! Int matrix will NOT work!
        """
        (h, w) = (len(m), len(m[0]))
        for y in range(0,h):
            maxrow = y
            for y2 in range(y+1, h):    # Find max pivot
                if abs(m[y2][y]) > abs(m[maxrow][y]):
                    maxrow = y2
            (m[y], m[maxrow]) = (m[maxrow], m[y])
            if abs(m[y][y]) <= eps:     # Singular?
                return False
            for y2 in range(y+1, h):    # Eliminate column y
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
        for y in range(h-1, 0-1, -1): # Backsubstitute
            c  = m[y][y]
            for y2 in range(0,y):
                for x in range(w-1, y-1, -1):
                    m[y2][x] -=  m[y][x] * m[y2][y] / c
            m[y][y] /= c
            for x in range(h, w):       # Normalize row y
                m[y][x] /= c
        return True


    ##### Magic Methods #####
    #todo: remove this
    def __getslice__(self,key):
        raise Exception('this called __getslice__ fix that')

    #todo: improve this
    def __getitem__(self,key):
        if isinstance(key,tuple):
            if len(key) == 1:
                key = key[0]
            else:
                if isinstance(key[0],int):
                    return Matrix(self[0][key[1:]])
                elif isinstance(key[0],slice):
                    return Matrix(x[key[1:]] for x in self[key[0]])
                    #return Matrix(IT.imap(lambda x: x[key[1:]],self[key[0]]))
                else:
                    raise TypeError
                #return type(self)(IT.imap(lambda x: x[key[1:]],self[key[0]]))
        if isinstance(key,(int,slice)):
            return Matrix(super(Matrix,self).__getitem__(key))
        else:
            raise TypeError('{0} indicies cannot be of type: {1}'
                    .format(type(self).__name__,type(key).__name__))

    def __str__(self):
        return super(Matrix,self).__str__()

    def __repr__(self):
        return super(Matrix,self).__repr__()

    def __nonzero__(self):
        return super(Matrix,self).__nonzero__()


    ##### Math Methods #####
    def __add__(self,other):
        pass
    def __radd__(self,other):
        pass

    def __sub__(self,other):
        pass
    def __rsub__(self,other):
        pass

    def __mul__(self,other):
        pass
    def __rmul__(self,other):
        pass

    def __div__(self,other):
        pass
    def __truediv__(self,other):
        pass
    def __floordiv__(self,other):
        pass

    def __pos__(self):
        pass

    def __neg__(self):
        pass

    def __abs__(self):
        pass

