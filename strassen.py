import numpy as np
import random
import sys

# # open the file
# try:
#     file = open(sys.argv[3], 'r')
#     dim = int(sys.argv[2])
# except FileNotFoundError:
#     print("File not found.")
#     sys.exit(1)

# # read the matrix from the file
# matrixA = np.zeros((dim,dim), dtype=int)
# matrixB = np.zeros((dim,dim), dtype=int)
# row = []
# for line in file:
#     row.append(int(line))

# k = 0
# for i in range(dim):
#     for j in range(dim):
#         matrixA[i][j] = row[k]
#         k += 1
        
# for i in range(dim):
#     for j in range(dim):
#         matrixB[i][j] = row[k]
#         k += 1
    

# for initial testing
def matrix_gen(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            mat[i][j] = random.randint(0,2)

    mat = np.array(mat)
    return mat


def matrix_mult(mat1,mat2):
    res = np.dot(mat1,mat2)
    return res


def split(matrix):
    row, col = matrix.shape
    if row % 2 == 1:
        matrix = np.vstack((matrix, np.zeros((1, col), dtype=int)))
        row += 1
    if col % 2 == 1:
        matrix = np.hstack((matrix, np.zeros((row, 1), dtype=int)))
        col += 1

    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]



def strassen(x, y):
	
	# Base case when size of matrices is 32x32
	if len(x) <= 257:
		return matrix_mult(x,y)

	# Splitting the matrices into quadrants. This will be done recursively
	# until the base case is reached.
	a, b, c, d = split(x)
	e, f, g, h = split(y)
    
	# Computing the 7 products, recursively (p1, p2...p7)
	p1 = strassen(a, f - h)
	p2 = strassen(a + b, h)	
	p3 = strassen(c + d, e)	
	p4 = strassen(d, g - e)	
	p5 = strassen(a + d, e + h)	
	p6 = strassen(b - d, g + h)
	p7 = strassen(a - c, e + f)

	# Computing the values of the 4 quadrants of the final matrix c
	AE_BG = p5 + p4 - p2 + p6
	AF_BH = p1 + p2		
	CE_DG = p3 + p4		
	CF_DH = p1 + p5 - p3 - p7

	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
	c = np.vstack((np.hstack((AE_BG, AF_BH)), np.hstack((CE_DG, CF_DH))))
        
	c = c[:x.shape[0], :y.shape[1]]

	return c


def print_diagonal(matrix):
    sum = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                # print(matrix[i][j], end=" ")
                sum += matrix[i][j]
            # else:
                # print(" ", end=" ")
        # print()
    return sum//6

# print_diagonal(strassen(matrixA, matrixB))

# mat1 = matrix_gen(3)
# mat2 = matrix_gen(3)
# print(strassen(mat1, mat2))
# print_diagonal(strassen(mat1, mat2))


def edge_generator(graph, dim):
    for i in range(dim):
        for j in range(dim):
            if j > i:
                graph[i][j] = np.random.choice((0,1), p=[0.97,0.03])
            else:
                graph[i][j] = graph[j][i]
    return graph

graph = np.zeros((1024,1024), dtype=int)
edge_grpah = edge_generator(graph, 1024)

A_squared = strassen(edge_grpah, edge_grpah)
A_cubed = strassen(A_squared, edge_grpah)

print(print_diagonal(A_cubed))
    