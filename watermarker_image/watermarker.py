from wand.image import Image

with Image(filename='background.jpg') as background:
  with Image(filename='watermark.png') as watermark:
    background.watermark(image=watermark, transparency=0.1)
  background.save(filename='result.jpg')
