import os
from PIL import Image
from PIL import ImageEnhance
import numpy as np

print(os.listdir("."))
img = Image.open('./lena.png')
print(img.format , img.size,img.mode )
img.show()

enhancer = ImageEnhance.Contrast(img)
enhanced_img = enhancer.enhance(2.0)
enhanced_img.show()
enhanced_img.save("out.png")

img_array = np.asarray(img)
img = Image.fromarray(img_array)

