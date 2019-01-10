from os import listdir
from skimage import io
from functions import *
from skimage.color import rgb2gray
from skimage import img_as_uint
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast

df = pd.read_csv("photolist.csv")
photopath = "./original/"
savepath = "./cropped/"

for i in tqdm(range(len(df))):
    filename = df.iloc[i, 0]
    im = io.imread(photopath + filename)
    startx = ast.literal_eval(df.iloc[i, 1])
    stopx = ast.literal_eval(df.iloc[i, 2])
    starty = ast.literal_eval(df.iloc[i, 3])
    stopy = ast.literal_eval(df.iloc[i, 4])

    if (len(startx) > 0 and len(starty) > 0):
        #print(filename)
        im = io.imread('./test/' + filename)
 
        for x in range(len(startx)):
            for y in range(len(starty)):
                cropped = im[starty[y]:stopy[y],startx[x]:stopx[x]]
                z = x + y
                z = str(z)
                io.imsave(savepath + filename[0:-4] + "_" + z + ".jpg", cropped)