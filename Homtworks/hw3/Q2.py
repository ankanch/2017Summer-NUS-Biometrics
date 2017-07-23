from sympy import Matrix
A = [[1,1,4], [-1, 2, 2]]
A = Matrix(A)
print("reduced row=\n",A.rref())
print("nullspace=\n",A.nullspace())
print("column spaces=\n",A.columnspace())
A = Matrix([[1,1,4], [-1, 2, 2],[0,0,0]])
print("matrix det=\n",A.det())
A = Matrix([[1,1,4], [-1, 2, 2]])
print("matrix condition=\n",A.condition_number())