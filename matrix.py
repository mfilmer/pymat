from numbers import Number

class Dim(list):
    def __new__(cls,inDim):
        # Make sure inDim is iterable
        iter(inDim)

        # If every item in inDim is a number create a Vec
        if all(isinstance(item,Number) for item in inDim):
            return Vec.__new__(cls,inDim)

        # Make sure every item in inDim is iterable
        try:
            for item in inDim: iter(item)
        except TypeError:
            raise TypeError('All lists must be iterable')

        # Make sure every item in inDim has the same length
        # or that there are zero items in the list
        if len(set(len(item) for item in inDim)) > 1:
            raise ValueError('All lists must be the same length')
        
        # Actually create the Dim because it passed all the tests
        return list.__new__(cls,inDim)

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
        return list.__new__(cls,inDim)

class Matrix(Dim):
    def __init__(self,inMat):
        inMat = map(Dim,inMat)
        super(Matrix,self).__init__(inMat)

    ##### Public Methods #####
    def transpose(self):
        return Matrix(zip(*self))

    def inverse(self):
        pass

    def det(self):
        """Calculate the determinant of a matrix"""
        pass

    def minor(self,key):
        """Return the requested minor of a matrix"""
        pass

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
            return super(Matrix,self).__getitem__(key)
        elif isinstance(key,(slice,int)):
            return super(Matrix,self).__getitem__(key)
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

