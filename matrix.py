
class Matrix(list):
    def __init__(self,inMat):
        inMat = map(Row,inMat)
        super(Matrix,self).__init__(inMat)

    ##### Public Methods #####
    def transpose(self):
        pass

    def inverse(self):
        pass

    def det(self):
        pass

    def minor(self,key):
        pass

    def ref(self):
        pass

    def rref(self):
        pass

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

class Row(list):
    ##### Math Methods #####
    def __add__(self,other):
        pass
    def __radd__(self,other):
        pass

    def __sub__(self,other):
        pass
    def __rsub__(self,other):
        pass
