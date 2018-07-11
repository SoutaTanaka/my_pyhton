import numpy as np
from PIL import Image
#import Image

a = np.array([[[255,255,255,255],[0,0,0,255]],[[0,0,0,255],[255,255,255,255]]])
img = np.tile(a,(500,500,1))




#print(img)

#pimg = Image.fromarray(img)
#pimg.show()

#print(type(img))

pimg = Image.fromarray(np.uint8(img))

pimg.save("fooo.png")
#pimg.show()

