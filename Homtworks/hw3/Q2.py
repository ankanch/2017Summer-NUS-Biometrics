from sympy import Matrix
A = [[1,1,4], [-1, 2, 2]]
A = Matrix(A)
print("reduced row=\n",A.rref())
print("nullspace=\n",A.nullspace())
print("column spaces=\n",A.columnspace())
