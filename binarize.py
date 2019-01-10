from os import listdir
from skimage import io
from functions import *
from skimage.color import rgb2gray
from skimage import img_as_uint
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

filepath = "./original/"

savepath = "./binary/"
filelist = listdir(filepath)


for i in tqdm(range(len(filelist))):    
    binarize(filelist[i], filepath, savepath)


