from os import listdir
from skimage import io

from skimage.color import rgb2gray
from skimage import img_as_uint
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

def binarize(file, path1, path2):
    im = io.imread(path1 + file)    
    im = rgb2gray(im)
        
    thresh = 0.8
    binary = im > thresh
    binary = img_as_uint(binary)
    binary = 65535 - binary    
    
    io.imsave(path2 + file, binary)
            
    
def gethistogram(im):
    h_hist = (im).mean(axis=0)
    #plt.figure(figsize=(10, 7))
    #plt.plot(h_hist)
    
    v_hist = (im).mean(axis=1)
    #plt.figure(figsize=(10, 7))
    #plt.plot(v_hist)
    return h_hist, v_hist

def findchunk(histogram, threshold):
    start = []
    stop = []
    count = 0
    prev = False
    for i in range(len(histogram)):
        if histogram[i] > threshold:
            if prev == False:
                start.append(i)
                prev = True
                count += 1
            else:
                count += 1            
        else:
            if prev == True:
                if count < 500:
                    count = 0
                    prev = False
                    start.pop()
                else:
                    stop.append(i)
                    count = 0
                    prev = False

    return start, stop

def findmean(start, stop):
    total = 0
    for i in range(len(start)):
        total = total + (stop[i] - start[i])
        #print(total)
    mean = int(total/len(start))
    return mean