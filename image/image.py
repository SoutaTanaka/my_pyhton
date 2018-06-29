import numpy as np
from PIL import Image, ImageFilter
#import Image
a = np.array([[0,255],[255,0]])
img = np.tile(a,(5000,5000))

print(type(img))

pimg = Image.fromarray(img)

#pimg.show()

