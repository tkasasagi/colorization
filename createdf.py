import pandas as pd
from os import listdir
from functions import *
from tqdm import trange

filepath = "./original/"
filelist = listdir(filepath)

startx = []
stopx  = []
starty = []
stopy  = []

for i in trange(len(filelist)):
    im = io.imread('./binary/' + filelist[i])
    h_hist, v_hist = gethistogram(im)
    sx, tx = findchunk(h_hist, 20)
    sy, ty = (findchunk(v_hist, 30))
    if (len(sy) > 0):
        mean = findmean(sx, tx)
        if (mean < 1000):
            padding = ty[-1] - sy[0]
            if (padding) < mean:
                sy[0] = sy[0] - (mean - padding)
    startx.append(sx)
    stopx.append(tx)
    starty.append(sy)
    stopy.append(ty)

filedf = pd.DataFrame()
filedf["filename"] = filelist
filedf["startx"] = startx
filedf["stopx"] = stopx
filedf["starty"] = starty
filedf["stopy"] = stopy

filedf.to_csv("photolist.csv", index = False)

