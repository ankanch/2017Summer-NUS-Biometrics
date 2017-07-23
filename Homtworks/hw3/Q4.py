import numpy as np
from numpy import linalg


### code for Q4 (c)
A = np.asarray([[100,100],[100,100.01]])
b = np.asarray([[2],[2]])
r = linalg.solve(A,b)
print("result for Q4.c=\n",r)

b = np.asarray([[2],[2.0001]])
r = linalg.solve(A,b)
print("result for Q4.c after accurte b=\n",r)