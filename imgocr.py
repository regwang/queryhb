# -*- coding:utf-8 -*-
from PIL import Image
import pytesser3
image = Image.open(r'E:\python\queryhb\oriimg\8.gif')
imgry = image.convert('L')
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()
text=pytesser3.image_to_string(out)
#print(pytesser.image_file_to_string(r'E:\python\queryhb\oriimg\1.gif'))
print(text)
