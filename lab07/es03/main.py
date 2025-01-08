class MatrixException(Exception):

    def __init__(self, message):
        self.message = message


class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return f'{self.matrix}'

    def __repr__(self):
        return f'Matrix({self.matrix})'
    
    def __eq__(self, m):
        if type(m) == Matrix:
            if self.rows != m.rows or self.cols != m.cols:
                return False
            
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.matrix[i][j] != m.matrix[i][j]:
                        return False
            
            return True
        else:
            return False
    
    def __add__(self, m):
        if self.rows != m.rows or self.cols != m.cols:
            raise MatrixException('numero di righe o colonne non coincidono per l\'addizione')
        
        res = []

        for i in range(self.rows):
            r = []

            for j in range(self.cols):
                r.append(self.matrix[i][j] + m.matrix[i][j])
            
            res.append(r)
        
        return res
    
    def __mul__(self, m):
        if type(m) == int or type(m) == float:
            return [[self.matrix[i][j] * m for j in range(self.cols)] for i in range(self.rows)]
        else:
            if self.cols != m.rows:
                raise MatrixException('numero di righe e colonne non concidono per la moltiplicazione')
            
            res = [[0] * m.cols for _ in range(self.rows)]

            for i in range(self.rows):
                for j in range(m.cols):
                    for k in range(m.rows):
                        res[i][j] += self.matrix[i][k] * m.matrix[k][j]
            
            return res
    
    def copy(self):
        return Matrix(self.matrix)

    def transposition(self):
        t = [[0] * self.rows for _ in range(self.cols)]

        for i in range(self.rows):
            for j in range(self.cols):
                t[j][i] = self.matrix[i][j]
        
        return t
    
    def norm(self):
        res = float('-inf')

        for j in range(self.cols):
            s = 0

            for i in range(self.rows):
                s += self.matrix[i][j]
            
            res = max(res, s)
        
        return res


def main():
    m1 = Matrix([[1,2,3], [1,2,3], [6,5,4]])        # 3 x 3
    m2 = Matrix([[0,1,2], [1,2,3], [0,0,0]])        # 3 x 3
    m3 = Matrix([[3,8,0], [9,0,1]])                 # 2 x 3
    m4 = Matrix([[3,8,0,1], [9,0,1,3], [0,0,0,0]])  # 3 x 4
    m5 = Matrix([[3,8,0], [9,0,1]])                 # 2 x 3
    m6 = m4.copy()                                  # 3 x 4

    # print(m1)
    # print(repr(m1))
    print('Equivalenza:', m3 == m5)
    print('Addizione:', m1 + m2)
    print('Prodotto scalare:', m1 * 2)
    print('Prodotto tra matrici:', m3 * m4)
    print('Trasposizione:', m3.transposition())
    print('Norma 1:', m1.norm())
    print('Copia:', m6)

if __name__ == '__main__':
    main()