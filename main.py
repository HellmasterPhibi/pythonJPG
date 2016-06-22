from __future__ import print_function
from PIL import Image


img = Image.open('skluzavka.jpg')

print(img.format, img.size, img.mode)
box = (0, 0, 1024, 1536)
region = img.crop(box)
region.show()
region.save('vyrez.jpg','jpeg')