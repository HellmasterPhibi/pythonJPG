from __future__ import print_function
from PIL import Image


img = Image.open('skluzavka.jpg')

print(img.format, img.size, img.mode)
width, height = img.size
box = (0, 0, width/2, height)
region = img.crop(box)
region.show()
region.save('vyrez.jpg','jpeg')