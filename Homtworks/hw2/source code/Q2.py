#encoding:utf-8
#Study Numpy, Scipy, PIL and Matplotlib libraries. Use lena.png to perform following
# operations and save the images: (5)

from PIL import Image,ImageOps,ImageFilter
from matplotlib import pyplot as plt
import numpy as np

img_lena = Image.open("./lena.png")
img_lena = img_lena.convert("RGBA")

# perform rotate specified part of the image
                        # L  U   R   Lower
target = img_lena.crop((100,100,400,400))
target = target.convert("RGBA")
rot = target.rotate(45,expand=1)
rot2 = Image.new("RGBA",rot.size,(0,)*4)
out = Image.composite(rot,rot2,rot)
img_lena.paste(out,(50,50),rot)
#img_lena.show()
img_lena.save("./q2_rotate_lena.png")

# perform historgram equalization
img_lena = Image.open("./lena.png")
img_lena = img_lena.convert("RGB")
img_lena =  ImageOps.equalize(img_lena)
#img_lena.show()
img_lena.save("./q2_histeuql_lena.png")
# then draw historgram graph
orginal = Image.open("./lena.png")
processed = Image.open("./q2_histeuql_lena.png")
orginal = orginal.convert("L")
processed = processed.convert("L")
hiso = orginal.histogram()
hisp = processed.histogram()
print(hiso,len(hiso))
print(hisp,len(hisp))
fig = plt.figure()
a = fig.add_subplot(1,2,1)
a.set_title("Orignal Image - Long")
x = np.arange(256)
plt.bar(x,height=hiso,fc='k', ec='k')
plt.ylabel("Frequency")
plt.xlabel("Pixel")
a = fig.add_subplot(1,2,2)
a.set_title("Zhang - After Historgram Equalization")
plt.bar(x, height=hisp,fc='k', ec='k')
plt.xlabel("Pixel")
plt.show()
plt.save("./q2_histogram.png")

# perform max,min,medium filter on lena.png
maxIMF =  img_lena.filter(ImageFilter.MaxFilter)
minIMF = img_lena.filter(ImageFilter.MinFilter)
medIMF = img_lena.filter(ImageFilter.MedianFilter)
#maxIMF.show()
#minIMF.show()
#medIMF.show()
maxIMF.save("./q2_maxIMF_lena.png")
minIMF.save("./q2_minIMF_lena.png")
medIMF.save("./q2_medIMF_lena.png")

# perofrm Guessiuam Blur with sigma equal to 3 and 5
gaussiuam3 = img_lena.filter(ImageFilter.GaussianBlur(3))
gaussiuam5 = img_lena.filter(ImageFilter.GaussianBlur(5))
#gaussiuam3.show()
#gaussiuam5.show()
gaussiuam3.save("./q2_gaussiuam_3_lena.png")
gaussiuam5.save("./q2_gaussiuam_5_lena.png")