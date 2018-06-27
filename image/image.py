import numpy as np
from PIL import Image, ImageFilter
a = np.array([[0,255],[255,0]])
img = np.tile(a,(5000,5000))

pimg = Image.fromearray(np.uint8(img))

pimg.show()


