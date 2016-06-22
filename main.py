from PIL import Image
import piexif
import io
import argparse

parser = argparse.ArgumentParser(description='This script opens a specific 3D jpg image file, cuts one half of it and adds specific metadata. '
                                             'This script can be used only on the file skluzavka.jpg, so be sure that you have such file in the same directory. '
                                            'The output file is called vyrez.jpg and it wil be also saved into the current directory. '
                                             'All metadata are shown on the standard output so you can compare.'
                                             'The metadata added are: '
                                             '1) a secret message(plaintext) in the exif cathegory "software" '
                                             '2) an image file (binary) in the exif cathegory "thumbnail". '
                                             'Afterwards, this same script returns these exif data to their original state. ')

args = parser.parse_args()


def cropInHalf(input):
   img = Image.open(input)
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

cropInHalf('skluzavka.jpg')

def getExif(fileName):
  vyrez = Image.open(fileName)
  exifDict = piexif.load(vyrez.info["exif"])
  print(exifDict)
  return exifDict

exifDict=getExif('vyrez.jpg')

oldThumb = exifDict["thumbnail"]
#I chose to hide the secret text message in the field "Software"
exifDict["1st"][piexif.ImageIFD.Software] = "-------------Tajna zprava---------------------"
exifDict["thumbnail"] = ImageDump("wolf.jpg")

exifBytes = piexif.dump(exifDict)
piexif.insert(exifBytes, "vyrez.jpg")

exifDict2 = getExif('vyrez.jpg')
#print text message stored in exif
print(exifDict2["1st"][piexif.ImageIFD.Software])

#now remove the meta image and secret message:
exifDict2["thumbnail"] = oldThumb
exifDict2["1st"][piexif.ImageIFD.Software] = ""
exifBytes2 = piexif.dump(exifDict2)
piexif.insert(exifBytes2, "vyrez.jpg")

exifDict3 = getExif('vyrez.jpg')
#print text message stored in exif
print(exifDict3["1st"][piexif.ImageIFD.Software])

