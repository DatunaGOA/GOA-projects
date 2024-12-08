
def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def diagonal_sums(matrix):
    n = len(matrix)
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    anti_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    return main_diagonal_sum, anti_diagonal_sum


matrix1 = [[1, 3], [1, 4]]
matrix2 = [[4, 1], [2, 2]]
print(add_matrices(matrix1, matrix2))  

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(matrix)) 

square_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sums(square_matrix))  