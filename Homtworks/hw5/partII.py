import FisherFace as FF
import numpy as np
from matplotlib import pyplot as plt

# PCA features part
#1.2.
K=30
faces,idLabel = FF.read_faces("./train")
W,LL,m = FF.myPCA(faces)
#3.
We = W[:,:K]
#4.
Ylist = []
for f in faces.T:
    y= np.dot(np.transpose(We),f-m)
    Ylist.append(y)
#plt.plot(Ylist)
#plt.show()
#5.
Xlist = []
for f,y in zip(faces.T,Ylist):
    x = np.dot(We,y) + m
    Xlist.append(x)
print(Xlist)
#plt.plot(Xlist)
#plt.show()

# LDA feature part
K1 = 90
W1 = W[:,:K1]