from os import listdir
from skimage import io

from skimage.color import rgb2gray
from skimage import img_as_uint
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from functions import *


filedf = pd.DataFrame()

filepath = "./test/"

savepath = "./cropped/"
filelist = listdir(filepath)

filename = "3601-000128-0.jpg"

im = io.imread('./binary/' + filename)



h_hist, v_hist = gethistogram(im)

startx, stopx = findchunk(h_hist, 20)
starty, stopy = (findchunk(v_hist, 30))


im2 = io.imread('./test/' + filename)

mean = findmean(startx, stopx)
padding = stopy[-1] - starty[0]
if (padding) < mean:
    starty[0] = starty[0] - (mean - padding)
    
for x in range(len(startx)):
    for y in range(len(starty)):
        cropped = im2[starty[y]:stopy[y],startx[x]:stopx[x]]
        z = x + y
        z = str(z)
        io.imsave(savepath + filename[0:-4] + "_" + z + ".jpg", cropped)

io.imshow(cropped1)
io.imshow(cropped2)
io.imshow(cropped3)

io.imsave(savepath + "test1.jpg", cropped1)
io.imsave(savepath + "test2.jpg", cropped2)
io.imsave(savepath + "test3.jpg", cropped3)



from PIL import Image

im = Image.open('./test/' + "3601-000175-0.jpg")  
cropped1 = Image.open('./colorized/' + "test1.jpg")
cropped2 = Image.open('./colorized/' + "test2.jpg")
cropped3 = Image.open('./colorized/' + "test3.jpg")

im.paste(cropped1, (startx[0], starty[0])) 
im.paste(cropped2, (startx[1], starty[0])) 
im.paste(cropped3, (startx[2], starty[0])) 
  
#Saved in the same relative location 
im.save("pasted_picture.jpg") 