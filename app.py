from PIL import Image
import pytesseract
import os

filename = '1.png'
img2 = Image.open(filename)
text = pytesseract.image_to_string(img2)
print(text)
