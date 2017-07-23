#encoding:utf-8
#A = [1, 3, 2, 4; 2, 2, 3, 1; 3, 2, 4, 5; 4, 2, 0, 1], B = [1, 2, 3, 4; 2, 1, 3, 0; 4, 1, 3, 4; 2, 4,
#3, 4]. Please compute the convolution between A and B by hand. They try to verify your
#answer by Python code. (Hint: from scipy import signal, use signal.convolve). (2)

from scipy import signal
import numpy as np

A = np.array([[1, 3, 2, 4],[ 2, 2, 3, 1],[ 3, 2, 4, 5],[4, 2, 0, 1]])
B = np.array([[1, 2, 3, 4],[2, 1, 3, 0],[ 4, 1, 3, 4],[2, 4,3, 4]])
print(">>>A=\n",A,"\n>>>B=\n",B)

result = signal.convolve(A,B)
print(">>>convolve A and B = \n",result)
