import pandas as pd
import ast

df = pd.read_csv("photolist.csv")

finallist = []

startx = df['startx'].tolist()
stopx  = df['stopx'].tolist()
starty = df['starty'].tolist()
stopy  = df['stopy'].tolist()

finalw = []
finalh = []

def cl(li):
    return ast.literal_eval(li)

for i in range(len(startx)):    
    sx = ast.literal_eval(startx[i])
    #print(sx)    
    tx = ast.literal_eval(stopx[i])
    w = []
    for j in range(len(sx)):
        w.append(tx[j] - sx[j])
    finalw.append(w)
    
for i in range(len(starty)):    
    sy = ast.literal_eval(starty[i])
    #print(sx)    
    ty = ast.literal_eval(stopy[i])
    h = []
    for j in range(len(sy)):
        h.append(ty[j] - sy[j])
    finalh.append(h)
    
for k in range(len(startx)):
    
    li = [cl(startx[k]), cl(starty[k]), finalw[k], finalh[k]]
    finallist.append(li)
    
df = pd.DataFrame()

df['list'] = finallist

df.to_csv("list.csv", index = False)

data = finallist[55]
len(data[1])


coordinate = []
numpic = []
for data in finallist:
    total = len(data[0]) * len(data[1])
    numpic.append(total)
    if total == 3:
        print(data)
    

    
    
        final = (data[0][0], data[1][0], data[2][0], data[3][0])
        coordinate.append(final)

        


    

    