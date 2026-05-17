import sys

eps = sys.float_info.epsilon

def IsEqual(a, b):
    return abs(a - b) < eps

def IsEqual_abs(a, b):
    return abs(abs(a) - abs(b)) < eps

def identity(m: int):
    n = m
    if m <= 0 or n <= 0:
        raise ValueError("m or n < 0")
    elif m != n:
        raise ValueError("matrix isn't quard")
    data = []
    for i in range(m):
        data.append([])
        for j in range(n):
            if i == j:
                data[i].append(1.0)
                continue
            data[i].append(0.0)
    return Matrix(matrixs2=data)

class Matrix:
    def __init__(self, m1: int=None, n1: int=None, matrixs2: list=None):
        self.matrix = None
        self.size = None
        self.m = None
        self.n = None
        if matrixs2:
            self.m = len(matrixs2)
            self.n = len(matrixs2[0])
            for i in matrixs2:
                if type(i) == list:
                    for j in i:
                        if type(j) == list:
                            raise ValueError("List is not matrix. It include not only int and float type data")
                        if type(j) != float and type(j) != int and type(j) != complex:
                            raise ValueError("List is not matrix. It include not only int and float type data")
                else:
                    raise ValueError("List is not matrix (MATRIXS: list [[x11, x12], [x21, x22]] etc.)")
                if self.m - self.n == 0:
                    self.quard = True
                else:
                    self.quard = False
                self.size = self.m * self.n
                self.matrix = matrixs2
                return
        if m1 and n1:
            self.m = m1
            self.n = n1
            self.size = m1 * n1
            if self.m - self.n == 0:
                self.quard = True
            else:
                self.quard = False
            self.matrix = []
            for i in range(m1):
                self.matrix.append([])
                for j in range(n1):
                    self.matrix[i].append(0.0)
            return
        raise ValueError("Input m and n (matrix size: m*n) or input matrix (MATRIxS: list [[x11, x12], [x21, x22]] etc.)")

    def __repr__(self):
        txt = ""
        for i in self.matrix:
            txt = f"{txt}{i}, "
        txt = f"{txt}\nlines: {self.m}, columns: {self.n}, size: {self.size}, quard: {self.quard}."
        return txt
    
    def __str__(self):
        txt = ""
        for i in self.matrix:
            txt = f"{txt}{i}"
            txt = f"{txt}\n"
        txt = txt.replace(',', ' ')
        return txt
    
    def edit(self, m: int, n: int, new: float or int or complex):
            if self.m < m or self.n < n or m <= 0 or n <= 0:
                raise ValueError("There are line or column doesn't exist")
            if type(new) == float or type(new) == int or type(new) == complex:
                if type(new) == int or type(new) == float or type(new) == complex:
                    self.matrix[m-1][n-1] = new
                    return True
                else:
                    raise ValueError("Type of new variable isn't int, float or complex")
            raise ValueError("You aren't input float, int or complex number")
    
    def addition(self, other: Matrix):
        if type(other) == Matrix:
            if self.m == other.m and self.n == other.n:
                newmatrix = []
                for i in range(self.m):
                    newmatrix.append([])
                    for j in range(self.n):
                        newmatrix[i].append(self.matrix[i][j] + other.matrix[i][j])
                return Matrix(matrixs2=newmatrix)
            else:
                raise ValueError("Matrixs must have the same dimensions for addition")
        else:
            raise ValueError("First value isn't matrix")
    
    def __add__(self, Mother):
        return self.addition(Mother)
    
    def subscribe(self, other: Matrix):
        if type(other) == Matrix:
            if self.m == other.m and self.n == other.n:
                newmatrix = []
                for i in range(self.m):
                    newmatrix.append([])
                    for j in range(self.n):
                        newmatrix[i].append(self.matrix[i][j] - other.matrix[i][j])
                return Matrix(matrixs2=newmatrix)
            else:
                raise ValueError("Matrixs must have the same dimensions for subscribe")
        else:
            raise ValueError("First value isn't matrix")
    
    def __sub__(self, Mother):
        return self.subscribe(Mother)
        
    def multiply(self, other: Matrix or int or float or complex):
            result_data = None
            if type(other) == Matrix:
                if self.n != other.m:
                    raise ValueError("Matrixs must have the same dimensions for multiply")
                result_data = [[0 for _ in range(other.n)] for _ in range(self.m)]
                for i in range(self.m):
                    for j in range(other.n):
                        for k in range(self.n):
                            result_data[i][j] += self.matrix[i][k] * other.matrix[k][j]
            elif type(other) == int or type(other) == float or type(other) == complex:
                result_data = []
                for i in range(self.m):
                    result_data.append([])
                    for j in range(self.n):
                        result_data[i].append(self.matrix[i][j] * other)
            else:
                raise ValueError("First value isn't matrix, int, float or complex")
            return Matrix(matrixs2=result_data)
    
    def __mul__(self, other1):
        return self.multiply(other1)
    
    def __rmul__(self, other1):
        if type(other1) == int or type(other1) == float or type(other1) == complex:
            return self.multiply(other1)
        return other1.multiply(self)
    
    def transpose(self):
        new_data = [
            [self.matrix[i][j] for i in range(self.m)]
            for j in range(self.n)
        ]
        return Matrix(matrixs2=new_data)
    
    def take(self, m:int, n: int):
        if m <= 0 or n <= 0:
            raise ValueError("m or n < 0")
        return self.matrix[m-1][n-1]
    
    def __len__(self):
        return self.size
    
    def det(self) -> float or int or complex:
        if not self.quard:
            raise ValueError("Determinant can only be calculated for square matrixs")
        a = [[item for item in row] for row in self.matrix]
        n = self.m
        det_sign = 1
        for i in range(n):
            pivot_row = i
            for r in range(i + 1, n):
                if abs(a[r][i]) > abs(a[pivot_row][i]):
                    pivot_row = r
            if pivot_row != i:
                a[i], a[pivot_row] = a[pivot_row], a[i]
                det_sign *= -1
            if abs(a[i][i]) < eps:
                return 0
            for r in range(i + 1, n):
                factor = a[r][i] / a[i][i]
                for c in range(i, n):
                    a[r][c] -= factor * a[i][c]
        determinant_value = det_sign
        for i in range(n):
            determinant_value *= a[i][i]
        if isinstance(determinant_value, complex):
            if abs(determinant_value.imag) < eps:
                determinant_value = determinant_value.real
        return determinant_value
    
    def inverse(self):
        if self.det is None:
            raise ValueError("Det isn't found")
        if IsEqual_abs(self.det(), 0):
            raise ValueError("Inverse matrix isn't found. det = 0")
        return (1 / self.det()) * self.adjugate().transpose()
    
    def __pow__(self, other):
        data = self
        if other == 0:
            return 1
        if other < 0:
            data = data.inverse()
        for _ in range(1, abs(other)):
            data *= data
        
        for i in range(data.m):
            for j in range(data.n):
                data.matrix[i][j] = int(data.take(i+1, j+1) * 10**3) / 10**3
        return data
    
    def adjugate(self):
        if not self.quard:
            raise ValueError("Adjugate matrix can only be calculated for square matrices")

        n = self.m
        if n == 1:
            return Matrix(matrixs2=[[1]])

        adj_data = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                remaining_rows = self.matrix[:i] + self.matrix[i+1:]
                minor_data = [row[:j] + row[j+1:] for row in remaining_rows]
                minor_matrix = Matrix(matrixs2=minor_data)
                minor_det = minor_matrix.det()
                sign = (-1) ** (i + j)
                adj_data[i][j] = sign * minor_det

        return Matrix(matrixs2=adj_data)
    
    def divide(self, other: Matrix or int or float or complex):
        if other == 0:
            raise ValueError("It is impossible to divide")
        return self * other**-1
    
    def __truediv__(self, other1):
        return self.divide(other1)
    
    def __rtruediv__(self, other1):
        if type(other1) == int or type(other1) == float or type(other1) == complex:
            return other1 * self**-1
        return other1.divide(self)



if __name__ == "__main__":
    exit()