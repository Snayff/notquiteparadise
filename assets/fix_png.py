# remove sRGB errors from .png files
path =r"C:\Users\Gabriel\Documents\NotQuiteParadise\assets" # path to all .png images
import os

png_files =[]

for dirpath, subdirs, files in os.walk(path):
    for x in files:
        if x.endswith(".png"):
            png_files.append(os.path.join(dirpath, x))

file =r'C:\\Users\\Gabriel\\Downloads\\pngcrush_1_8_11_w64' #pngcrush file 


for name in png_files:
    cmd = r'{} -ow -rem allb -reduce {}'.format(file,name)
    os.system(cmd)