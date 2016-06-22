from PIL import Image
import piexif
import io

def cropInHalf(input):
   img = Image.open('skluzavka.jpg')
   exifDict = piexif.load(img.info["exif"])
   width, height = img.size
   box = (0, 0, width/2, height)
   region = img.crop(box)
   #copy the original exif data into variable origEfic
   origExif = img.info['exif']
   region.save('vyrez.jpg','jpeg', exif=origExif)

#image for meta exif loading
def ImageDump(imageFile):
  o = io.BytesIO()
  thumb_im = Image.open(imageFile)
  thumb_im.thumbnail((50, 50), Image.ANTIALIAS)
  thumb_im.save(o, "jpeg")
  thumbnail = o.getvalue()
  return thumbnail

vyrez = Image.open('vyrez.jpg')
exifDict = piexif.load(vyrez.info["exif"])
print(exifDict)

oldThumb = exifDict["thumbnail"]
#I chose to hide the secret text message in the field "Software"
exifDict["1st"][piexif.ImageIFD.Software] = "-------------Tajna zprava---------------------"
exifDict["thumbnail"] = ImageDump("wolf.jpg")

exifBytes = piexif.dump(exifDict)
piexif.insert(exifBytes, "vyrez.jpg")
img2 = Image.open('vyrez.jpg')

exifDict2 = piexif.load(img2.info["exif"])
print(exifDict2)

img2.show()

#print text message stored in exif
print(exifDict2["1st"][piexif.ImageIFD.Software])
