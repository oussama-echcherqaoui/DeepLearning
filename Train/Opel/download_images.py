import PIL
from PIL import Image
import os, sys
path = "./"
dirs = os.listdir( path )
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            img = Image.open(path+item)
            print(img.size)
            f, e = os.path.splitext(path+item)
            img = img.resize((150,150 ), Image.ANTIALIAS)
            img.save(f + '.jpg')
            print(img.size)
resize()