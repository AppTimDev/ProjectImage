"""
Usage:
Write some text on an image

Font used to support adding chinese words: Microsoft JhengHei font family 
"""
from PIL import Image, ImageDraw, ImageFont

img = Image.open('input.png')
w, h = img.size
print(f"Image size: {w} x {h}")

#User-defined variables
text_pos_x = w//4
text_pos_y = h-60
text = "Hello! 大家好!!"

d1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('msjhbd.ttc', 20) #font-size
d1.text((text_pos_x, text_pos_y), text, font=myFont, fill=(255, 255, 255)) #text color white

#show and save image
img.show()
img.save('output.png', 'png')