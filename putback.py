from tqdm import tqdm
import pandas as pd
import ast
from PIL import Image
import os.path

df = pd.read_csv("photolist.csv")

filelist = df[df['startx'] != "[]"]
filelist = filelist[filelist['starty'] != "[]"]

output = filelist['filename'].tolist()

for f in tqdm(range(len(output))):
    if(os.path.isfile("./original/" + output[f])):
        
        #get image number
        
        #imno = output[0][-5]
        image = output[f][:-4]
        
        #get list
        row = df[df['filename'] == image + ".jpg"]
        startx = ast.literal_eval(row.iloc[0,1])
        stopx = ast.literal_eval(row.iloc[0,2])
        starty = ast.literal_eval(row.iloc[0,3])
        stopy = ast.literal_eval(row.iloc[0,4])
        
        loop = len(startx) * len(starty)
        
        original = Image.open('./original/' + image + ".jpg")  
        
        for i in range(loop):
            #cropped = Image.open('./colorized/' + output[0])
            cropped = Image.open('./outputs/' + image + "_" + str(i) + ".jpg")    
            sx = startx[i]
            if i < 3:
                sy = starty[0]
            else:
                sy = starty[1]
            
            original.paste(cropped, (sx, sy))
          
        #Saved in the same relative location 
        original.save("./processed/" + image + ".jpg") 