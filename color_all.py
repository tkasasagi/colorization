import glob
import os
import mlcrate as mlc
from tqdm import tqdm
import multiprocessing
import subprocess
import numpy as np
import time

images = os.listdir('cropped/')

def colorize(img):
    input_fn = 'cropped/{}'.format(img)
    output_fn = 'outputs/{}'.format(img)
    if os.path.isfile(output_fn):
        return 0

    time.sleep(np.random.random()*2)
    out = subprocess.run("th colorize.lua {} {}".format(input_fn, output_fn), shell=True, check=True)
    return out

pool = multiprocessing.Pool(96)

for item in tqdm(pool.imap_unordered(colorize, images), total=len(images), smoothing=0.05):
    pass
