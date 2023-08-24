class MatrixException(Exception):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f'Конфликт размерности матриц, matrix_a = {self.x1}x{self.y1}; matrix_b = {self.x2}x{self.y2}'


class Matrix():

    def __init__(self, matrix: list):
        self._matrix = matrix

    def __eq__(self, __other: object) -> bool:
        if len(self._matrix) != len(__other._matrix):
            return False
        else:
            __flag = False
            for i in range(len(self._matrix)):
                if self._matrix[i] == __other._matrix[i]:
                    __flag = True
                else:
                    self._flag = False
            return __flag

    def __add__(self, other):
        if len(self._matrix) != len(other._matrix):
            raise MatrixException(len(self._matrix), len(self._matrix[0]), len(other._matrix), len(other._matrix[0]))
        else:
            __result_matrix = []
            for i in range(len(self._matrix)):
                line1 = self._matrix[i]
                line2 = other._matrix[i]
                c = [x + y for x, y in zip(line1, line2)]
                __result_matrix.append(c)
            return Matrix(__result_matrix)

    def __mul__(self, other):
        if len(self._matrix[0]) != len(other._matrix):
            raise MatrixException(len(self._matrix), len(self._matrix[0]), len(other._matrix), len(other._matrix[0]))
        else:
            result = []
            for i in range(len(self._matrix)):
                new_row = []
                for j in range(len(other._matrix[0])):
                    elem = 0
                    for k in range(len(other._matrix)):
                        elem += self._matrix[i][k] * other._matrix[k][j]
                    new_row.append(elem)
                result.append(new_row)
            return Matrix(result)

    def __str__(self) -> str:
        result_string = ''

        for i in self._matrix:
            result_string += f'{i}\n'

        return result_string


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_3 = Matrix([[10, 2, 3], [40, 5, 6], [7, 8, 90]])
    matrix_4 = Matrix([[10, 2, 3], [40, 5, 6]])

    print(matrix_1 == matrix_2)
    print(matrix_3 == matrix_4)

    print(matrix_1 + matrix_3)
    print(matrix_1 + matrix_4)

    print(matrix_1 * matrix_3)
    print(matrix_1 * matrix_4)
