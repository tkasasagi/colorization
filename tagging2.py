from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from os import listdir
import pandas as pd


import tensorflow as tf
import numpy as np

from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.resnet50 import *
from tensorflow.python.keras.applications.inception_v3 import *


#print (tf.__version__) # Must be v1.1+

filelist = listdir("./outputs/")
tags = []

model = InceptionV3(weights='imagenet')

for file in filelist:
    print(file)
    img = image.load_img('./outputs/' + file, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    preds = model.predict(x)
    result = decode_predictions(preds, top=100)
    tags.append(result)
    
df = pd.DataFrame()
df['image'] = filelist
df['tags'] = result

df.to_csv('tagging.csv', index = False)
    
