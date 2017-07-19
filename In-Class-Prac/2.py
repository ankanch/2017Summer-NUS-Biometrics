import numpy as np

#To use functions from Numpy, you need to first import the library by
import numpy as np
#2. Generate a matrix from a list.
M = np.array([1,1,1])
#3. Convert a matrix to a list.
L = list(M)
#4. Generate a random array.
M = np.random.randint(1,100,(100,100))
#5. Display the size of a matrix
print(M.shape)
#6. Perform a transpose.
M_transpose = M.transpose()
#7. Traverse this matrix and compute the sum of all elements. (Hint: use M.shape)

#8. Compute the sum of its 50th column and 50th row.

#9. Multiply each element by 2.

#10. Compare M*M and M.dot(M).