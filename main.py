from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import io

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
width, height = img.size
box = (0, 0, width/2, height)
region = img.crop(box)
#region.show()

#copy the original exif data into variable origEfic
origExif = img.info['exif']
region.save('vyrez.jpg','jpeg', exif=origExif)

vyrez = Image.open('vyrez.jpg')

#print(getExif(img))
#print(getExif(vyrez))


exifDict = piexif.load(vyrez.info["exif"])
print(exifDict)

exifDict["0th"][piexif.ImageIFD.XResolution] = (width, 1)
exifDict["0th"][piexif.ImageIFD.YResolution] = (height, 1)
exifDict["1st"][piexif.ImageIFD.Software] = "-------------Tajna zprava---------------------"

#image for meta exif loading
o = io.BytesIO()
thumb_im = Image.open("wolf.jpg")
thumb_im.thumbnail((50, 50), Image.ANTIALIAS)
thumb_im.save(o, "jpeg")
thumbnail = o.getvalue()

exifDict["thumbnail"] = thumbnail
exifBytes = piexif.dump(exifDict)
#extraBytes = piexif.dump(extra)
vyrez.save('newExif.jpg', "jpeg")
#print(getExif(img2))
piexif.insert(exifBytes, "newExif.jpg")
img2 = Image.open('newExif.jpg')

exifDict2 = piexif.load(img2.info["exif"])
print(exifDict2)

img2.show()

#print text message stored in exif
print(exifDict2["1st"][piexif.ImageIFD.Software])