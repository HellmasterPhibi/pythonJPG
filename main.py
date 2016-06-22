from __future__ import print_function
from PIL import Image


img = Image.open('skluzavka.jpg')

print(img.format, img.size, img.mode)
box = (0, 0, 400, 400)
region = img.crop(box)
region.show()