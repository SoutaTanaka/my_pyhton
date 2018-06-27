import numpy as np
from PIL import Image, ImageFilter
#import Image
a = np.array([[[0, 0, 0],[255, 255, 255]],[[255,255,255],[0,0,0]]])
img = np.tile(a,(5,5))

print(type(img))
print(img)
#jpimg = Image.fromarray(img)

#pimg.show()

