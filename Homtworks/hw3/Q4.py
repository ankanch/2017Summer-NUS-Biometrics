import numpy as np
from sympy import Matrix
from numpy import linalg


### code for Q4 (c)
A = np.asarray([[100,100],[100,100.01]])
b = np.asarray([[2],[2]])
r = linalg.solve(A,b)
print("result for Q4.c=\n",r)

b = np.asarray([[2],[2.0001]])
r = linalg.solve(A,b)
print("result for Q4.c after accurte b=\n",r)

B = Matrix([[100,100],[100,100.01]])
print("matrix det=\n",B.det())
print("matrix condition=\n",B.condition_number())

print("22matrix det=\n",linalg.det(A))
print("22matrix condition=\n",linalg.cond(A))