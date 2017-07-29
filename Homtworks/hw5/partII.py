import FisherFace as FF
import numpy as np
from matplotlib import pyplot as plt

# Task 1.
# =================================PCA features part
#1.2.
K=30
faces,idLabel = FF.read_faces("./train")
print(faces.shape)
W,LL,m = FF.myPCA(faces)
#3:select feature dim of PCA    
We = W[:,:K]
#4: project to PCA
proj_to_PCA = []
#proj_to_PCA = np.dot(We.T,(faces.T-m).T)
for f in faces.T:
    y= np.dot(np.transpose(We),f-m)
    proj_to_PCA.append(y)
#5: project back from PCA
back_proj_from_PCA = []
for f,y in zip(faces.T,proj_to_PCA):
    x = np.dot(We,y) + m
    back_proj_from_PCA.append(x)
back_proj_from_PCA = np.asarray(back_proj_from_PCA)

# ======================================LDA feature part
# dim reduction
K1 = 90
W1 = W[:,:K1]
reduced_faces = np.dot(W1.T,(faces.T-m).T)
print("In LDA,We get a K1 by 120 matrix:",reduced_faces.shape)
#2.
LDAW,Centers,classLabels = FF.myLDA(reduced_faces,idLabel[:K1])
#3:project to LDA
print(LDAW.shape,W1.shape,faces.T.shape,m.shape)
proj_to_PCAp = np.dot(LDAW.T,np.dot(W1.T,(faces.T-m).T))
print(proj_to_PCAp.shape,Centers.shape,classLabels.shape)
#print(faces.shape,back_proj_from_PCA.shape)

#===== identifiy
ide_faces,ide_label = FF.read_faces("./test")
# projecting to PCA feature space
ide_proj_to_PCA = np.dot(ide_faces.T,(ide_faces.T-m).T)
print("ide_proj_to_PCA.shape=",ide_proj_to_PCA.shape,"\tZ.shape=",Centers.shape)



