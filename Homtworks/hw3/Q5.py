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

pyplot.plot(S,'b.')
pyplot.show()

####
KL = [20,50,100,200]
for K in KL:
    Sk = numpy.diag(S[:K])
    Uk = U[:, :K]
    Vtk = Vt[:K, :]

    aImk = numpy.dot(Uk, numpy.dot( Sk, Vtk))
    Imk = Image.fromarray(aImk)
    Imk.show()

