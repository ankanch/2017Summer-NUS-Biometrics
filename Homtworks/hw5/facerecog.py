import FisherFace as FF
import numpy as np
from matplotlib import pyplot as plt

faces_train,idLabel_train = FF.read_faces("./train")
print(">>-1:ReadData: feaces.shape=",faces_train.shape,"\tidLabel.shape=",idLabel_train.shape)
K = 30
K1 = 90
# =========================enroll faces==========
# project all training images into corresponding feature space
W,LL,m = FF.myPCA(faces_train)
We = W[:,:K]
W1 = W[:,:K1]
print(">>0:PCA: We.shape=",We.shape,"\tLL.shape=",LL.shape,"\tm.shape=",m.shape)
print(">>0:LDA: W1.shape=",W1.shape)
proj_pca_train = np.dot(We.T,(faces_train.T-m).T).T

#reduced_faces_lda =  np.dot(W1.T,faces_train.T-m).T
print(">>1:PCA-Projection: train.shape=",proj_pca_train.shape)
print(">>1:")
# compute the mean z of all his feature vectors
faces_mean_train = [[] for x in range(10)]
for label,vector in zip(idLabel_train[:K],proj_pca_train):
    faces_mean_train[label].append(vector)
faces_mean_train = [ np.mean(x,0) for x in faces_mean_train]
faces_mean_train = np.asarray(faces_mean_train)
print(">>2:PCA-FacesMean: train.shape=",faces_mean_train.shape)
# store these vectors as columns in numpy-matrix Z for every person
Z = faces_mean_train.T
print(">>3:PCA- Z.shape=",Z.shape)

# ======================identify========================
faces_test,idLabel_test = FF.read_faces("./test")
proj_pca_test = np.dot(We.T,(faces_test.T-m).T)     # column for one sample
print(">>4:PCA- Test-Projection: test.shape=",proj_pca_test.shape)

recog = []
for face in proj_pca_test.T:
    dist = [np.linalg.norm( temp - face ) for temp in faces_mean_train]
    recog.append(dist.index(min(dist)))

# make up confusion matrix
confusionmatrix = [ 0 for x in range(10)]
confusionmatrix = np.asarray([ confusionmatrix for x in range(10)])

correct = 0
for recg,real in zip(recog,idLabel_test):
    if recg == real:
        correct+=1
    confusionmatrix[real][recg]+=1
print(confusionmatrix)
print(">>5:PCA- OverallCorrectRate:",correct/len(recog),",recgnized",correct,"of",len(recog))

# Task 2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
reshaped_we = np.asarray([ np.asarray(FF.float2uint8(x)).reshape(160,140) for x in We.T[:8]])
print(">>6:PCA: reshaped.shape=",reshaped_we.shape)
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)
mean_face = np.asarray([[0 for x in range(140)] for y in range(160)])
print(">>7:PCA: mean_face.shape=",mean_face.shape)
for x,face_img in enumerate(reshaped_we):
    a = fig.add_subplot(3,3,x+1)
    a.set_title("eigenface %d"%(x+1))
    plt.imshow(face_img,'gray')
    mean_face = mean_face + face_img
mean_face = mean_face / 8
a = fig.add_subplot(3,3,9)
a.set_title("mean face")
plt.imshow(mean_face,'gray')
plt.show()