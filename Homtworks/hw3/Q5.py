from PIL import Image
from PIL import ImageOps
import numpy
from numpy import linalg
import matplotlib
from matplotlib import pyplot

flower = Image.open("flower.bmp")
flower.show()

flower = ImageOps.grayscale(flower)
aflower = numpy.asarray(flower) # aflower is unit8
aflower = numpy.float32(aflower)

U,S,Vt = linalg.svd(aflower)

#pyplot.plot(S,'b.')
#pyplot.show()

####
KL = [0,0,200,100,50,20]
fig = pyplot.figure()
pyplot.subplots_adjust(hspace=0.5)
a = fig.add_subplot(3,2,1)
a.set_title("singular values")
pyplot.plot(S,'b.')
a = fig.add_subplot(3,2,2)
a.set_title("original image")
pyplot.imshow(aflower, cmap='gray')
for i,K in enumerate(KL):
    if i > 1:
        Sk = numpy.diag(S[:K])
        Uk = U[:, :K]
        Vtk = Vt[:K, :]
        aImk = numpy.dot(Uk, numpy.dot( Sk, Vtk))
        Imk = Image.fromarray(aImk)
        a = fig.add_subplot(3,2,i+1)
        a.set_title(">>>>> Image with K=%d <<<<<"%K)
        pyplot.imshow(aImk,  cmap='gray')
        #Imk.show()
pyplot.show()

