from matplotlib import pyplot as plt
import numpy as np

P = np.asarray([2,3])   # change point tobe transformed here
C = np.asarray([3,2])   # change transform center here

# set up related matrix
T1 = np.asarray([[1,0,-99],[0,1,-99],[0,0,1]])
T1[:,2][0] = C[0]*-1
T1[:,2][1] = C[1]*-1

R = np.asarray([[99.0,-99.0,0],[99.0,99.0,0],[0,0,1.0]])
theta = [x*np.pi/4 for x in range(1,8)] # generate all thetas from pi/4 to 7pi/4
Rlist = []
for t in theta:
    R[:,0][0] = np.cos(t)    #cos
    R[:,0][1] = np.sin(t)    #sin
    R[:,1][0] = np.sin(t*-1)    #-sin
    R[:,1][1] = np.cos(t)    #cos
    Rlist.append(np.copy(R))

T2 = np.asarray([[1,0,99],[0,1,99],[0,0,1]])
T2[:,2][0] = C[0]
T2[:,2][1] = C[1]


# perform transformation
np.append(P,1)
P.resize(3,1)
ATlist = []
for r in Rlist:
    at = T2*R*T1*P
    at = np.dot(np.dot(np.dot(T2,r),T1),P)
    ATlist.append(at[:])

# plot on diagram
plt.title("Assigment 4 Part III - Geometric Transform - Long Zhang gstCN0342")
plt.plot(P[:-1][0],P[:-1][1], 'bo',label="original P(2,3)",markersize=8) #plot original point
plt.plot(C[0],C[1], 'mx',label="rotate center",markersize=8) #plot rotate center
for i,a in enumerate(ATlist):
    plt.plot(a[:-1][0],a[:-1][1], 'ro',label="transformed θ=%dπ/4"%(i+1),markersize=8) #plot point after transformation
plt.legend( loc=0)
plt.show()