#!/usr/bin/python
from PIL import Image
import os, sys

path = "./Train/KIA/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            im = im.convert('RGB')
            imResize = im.resize((150,150), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()