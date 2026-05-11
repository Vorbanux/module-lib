if __name__ == "__main__":
    exit()

import sys

eps = sys.float_info.epsilon

def IsEqual(a, b):
    return abs(a - b) < eps

def IsEqual_abs(a, b):
    return abs(abs(a) - abs(b)) < eps

class Matric:
    def __init__(self, m1: int=None, n1: int=None, matrics2: list=None):
        self.matric = None
        self.size = None
        self.m = None
        self.n = None
        if matrics2:
            self.m = len(matrics2)
            self.n = len(matrics2[0])
            for i in matrics2:
                if type(i) == list:
                    for j in i:
                        if type(j) == list:
                            print("[ERROR]: List is not matrice. It include not only int and float type data.")
                            return None
                        if type(j) != float and type(j) != int and type(j) != complex:
                            print("[ERROR]: List is not matrice. It include not only int and float type data.")
                            return None
                else:
                    print("[ERROR]: List is not matrice (MATRICES: list [[x11, x12], [x21, x22]] etc.).")
                    return None
                if self.m - self.n == 0:
                    self.quard = True
                else:
                    self.quard = False
                self.size = self.m * self.n
                self.matric = matrics2
                return None
        if m1 and n1:
            self.m = m1
            self.n = n1
            self.size = m1 * n1
            if self.m - self.n == 0:
                self.quard = True
            else:
                self.quard = False
            self.matric = []
            for i in range(m1):
                self.matric.append([])
                for j in range(n1):
                    self.matric[i].append(0)
            return None
        print("[ERROR]: input m and n (matric size: m*n) or input matric (MATRICES: list [[x11, x12], [x21, x22]] etc.).")
        return None

    def __repr__(self):
        txt = ""
        for i in self.matric:
            txt = f"{txt}{i}, "
        txt = f"{txt}\nlines: {self.m}, columns: {self.n}, size: {self.size}, quard: {self.quard}."
        return txt
    
    def __str__(self):
        txt = ""
        for i in self.matric:
            txt = f"{txt}{i}"
            txt = f"{txt}\n"
        txt = txt.replace(',', ' ')
        return txt
    
    def edit(self, m: int, n: int, new: float or int or complex):
            if self.m < m or self.n < n or m <= 0 or n <= 0:
                print("[ERROR]: There are line or column doesn't exist")
                return False
            if type(new) == float or type(new) == int or type(new) == complex:
                self.matric[m-1][n-1] = new
                return True
            print("[ERROR]: You aren't input float number.")
            return False
    
    def addition(self, matrice2: object):
        if self.size == matrice2.size:
            newmatric = []
            for i in range(self.m):
                print(i)
                newmatric.append([])
                for j in range(self.n):
                    #print(j)
                    newmatric[i].append(self.matric[i][j] + matrice2.matric[i][j])
            return Matric(matrics2=newmatric)
        else:
            print("[ERROR]: Matrices must have the same dimensions for addition")
            return None
    
    def subscribe(self, matrice2: object):
        if self.size == matrice2.size:
            newmatric = []
            for i in range(self.m):
                print(i)
                newmatric.append([])
                for j in range(self.n):
                    #print(j)
                    newmatric[i].append(self.matric[i][j] - matrice2.matric[i][j])
            return Matric(matrics2=newmatric)
        else:
            print("[ERROR]: Matrices must have the same dimensions for subscribe")
            return None
        
    def multiply(self, other):
    # Проверка: n первой должно быть равно m второй
    if self.n != other.m:
        print("[ERROR]: Matrices must have the same dimensions for multiply")
        return None
    result_data = [[0 for _ in range(other.n)] for _ in range(self.m)]

    for i in range(self.m):          # Идем по строкам A
        for j in range(other.n):     # Идем по столбцам B
            for k in range(self.n):  # Считаем сумму (скалярное произведение)
                result_data[i][j] += self.matric[i][k] * other.matric[k][j]
    
    return Matrix(result_data)