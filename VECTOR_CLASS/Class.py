class n_dimensional_Vector:
    def __init__(self, *n):
        self.values = list(n)   
        self.size = len(n)

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value

    def __str__(self):
        return f"Vector {self.values} and size is {self.size}"
    
    def __eq__(self, other):    
        if not isinstance(other, n_dimensional_Vector): 
            return NotImplemented
        return self.values == other.values

    # def __ne__(self, other):
    #     if not isinstance(other, n_dimensional_Vector):
    #         return NotImplemented
    #     return self.values != other.values

    def __add__(self, other):
        if not isinstance(other, n_dimensional_Vector):
            return NotImplemented
        if self.size != other.size:
            raise ValueError("Vectors must be of the same dimension")
        result = n_dimensional_Vector(*([0] * self.size))
        for i in range(self.size):
            result[i] = self[i] + other[i]
        return result
    def __matmul__(self, other):  #DOT PRODUCT
        if not isinstance(other, n_dimensional_Vector):
            return NotImplemented
        if self.size != other.size:
            raise ValueError("Vectors must be of the same dimension")
        d=0
        for i in range(self.size):
            d+=self[i] * other[i]
        return d
    def cross_product(self, other):
        if not isinstance(other, n_dimensional_Vector):
            return NotImplemented
        if self.size != 3 or other.size != 3:
            raise ValueError("Cross product is only defined for 3-dimensional vectors")
        i = self[1] * other[2] - self[2] * other[1]
        j = self[2] * other[0] - self[0] * other[2]
        k = self[0] * other[1] - self[1] * other[0]
        return n_dimensional_Vector(i, j, k)
    
    def clone(self):
        return n_dimensional_Vector(*self.values)

