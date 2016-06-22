from __future__ import print_function
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def getExif(i):
  ret = {}
  #i = Image.open(fn)
  info = i._getexif()
  for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    ret[decoded] = value
  return ret



img = Image.open('skluzavka.jpg')
exif_dict = piexif.load(img.info["exif"])
print(img.format, img.size, img.mode)
width, height = img.size
box = (0, 0, width/2, height)
region = img.crop(box)
#region.show()
origExif = img.info['exif']
region.save('vyrez.jpg','jpeg', exif=origExif)

vyrez = Image.open('vyrez.jpg')
print(getExif(img))
print(getExif(vyrez))



exif_dict = piexif.load(img.info["exif"])
exif_dict["0th"][piexif.ImageIFD.XResolution] = (width, 1)
exif_dict["0th"][piexif.ImageIFD.YResolution] = (height, 1)

exif_bytes = piexif.dump(exif_dict)
img.save('newExif.jpg', "jpeg", exif=exif_bytes)
img2 = Image.open('newExif.jpg')
print(getExif(img2))