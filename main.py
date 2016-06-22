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
exifDict = piexif.load(img.info["exif"])
print(img.format, img.size, img.mode)
width, height = img.size
box = (0, 0, width/2, height)
region = img.crop(box)
#region.show()

#copy the original exif data into variable origEfic
origExif = img.info['exif']
region.save('vyrez.jpg','jpeg', exif=origExif)

vyrez = Image.open('vyrez.jpg')

print(getExif(img))
print(getExif(vyrez))



exifDict = piexif.load(img.info["exif"])


exifDict["0th"][piexif.ImageIFD.XResolution] = (width, 1)
exifDict["0th"][piexif.ImageIFD.YResolution] = (height, 1)

extra = {
   'textMeta': '------------------Ahoj, ja jsem poznamka',
   'imageMeta': '*********************I shall be an image',
}

exifDict.update(extra)

print(exifDict)
exifBytes = piexif.dump(exifDict)
img.save('newExif.jpg', "jpeg", exif=exifBytes)
img2 = Image.open('newExif.jpg')
#print(getExif(img2))
exifDict2 = piexif.load(img2.info["exif"])
print(exifDict2)