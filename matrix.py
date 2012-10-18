from numbers import Number
import itertools

test2DMat = [[1,2,3],[4,5,6],[7,8,9]]
test3DMat = [[[1,2,3],[4,5,6],[7,8,9]],[[2,3,4],[5,6,7],[8,9,0]],[[9,8,7],[6,5,4],[3,2,1]]]

class Dim(list):
    def __new__(cls,inDim):
        print 'new dim'

        # If every item in inDim is a number create a Vec
        if all(isinstance(item,Number) for item in inDim):
            #return Vec(inDim)
            return Vec.__new__(cls,inDim)

        # Otherwise create a Dim
        return list.__new__(cls,inDim)

    def __init__(self,inDim):
        print 'init dim'

        # Make sure every item in inDim is iterable
        try:
            for item in inDim: iter(item)
        except TypeError:
            raise TypeError('All items in a Dim must be iterable')

        # Make sure every item in inDim has the same length
        # or that there are zero items in the list
        if len(set(len(item) for item in inDim)) > 1:
            raise ValueError('All lists in a Dim must be the same length')

        inDim = map(Dim,inDim)
        list.__init__(self,inDim)

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
        print 'new Vec'
        if cls.__name__ not in [Vec.__name__,Dim.__name__]:
            newMat = list.__new__(Vec,inDim)
            newMat.__init__(inDim)
            return newMat
        return list.__new__(Vec,inDim)

    def __init__(self,inDim):
        print 'init vec',inDim
        list.__init__(self,inDim)


class Matrix(Dim):
    def __new__(cls,inMat):
        print 'new matrix'
        return Dim.__new__(cls,inMat)

    def __init__(self,inMat):
        print 'init matrix'
        super(Matrix,self).__init__(inMat)

    ##### Public Methods #####
    #todo: improve this
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
            raise ValueError

    def transpose(self):
        return Matrix(itertools.izip(*self))

    def inverse(self):
        pass

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
    def __getitem__(self,key):
        if isinstance(key,tuple):
            try:
                i,j = key
            except ValueError:
                raise KeyError
            if not isinstance(i,(slice,int)) or not isinstance(j,(slice,int)):
                raise KeyError
            return Matrix(super(Matrix,self).__getitem__(key))
        elif isinstance(key,(slice,int)):
            return Matrix(super(Matrix,self).__getitem__(key))
        else:
            raise KeyError

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

