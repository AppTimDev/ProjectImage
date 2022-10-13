"""
Usage:
Write some text on an image
"""
from PIL import Image, ImageDraw, ImageFont

img = Image.open('input.png')
w, h = img.size
print(f"Image size: {w} x {h}")

#User-defined variables
text_pos_x = w//4
text_pos_y = h-36
text = "Hello!"

d1 = ImageDraw.Draw(img)
d1.text((text_pos_x, text_pos_y), text, fill=(255, 255, 255))

#show and save image
#img.show()
img.save('output.png', 'png')