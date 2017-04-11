import numpy as np
import math
# 求f（0.596）
dataRaw = [
    [0.4,0.55,0.65,0.80,0.9,1.05],
    [0.41075,0.57815,0.69675,0.88811,1.02652,1.25386]
]

matrixRaw = np.array(dataRaw,dtype=np.float64)
matrixfx = matrixRaw[1].copy()

for x in range(1,matrixRaw.shape[1]):
    for xx in range(x,matrixRaw.shape[1]):
        matrixfx[xx] = (matrixRaw[1][xx]-matrixRaw[1][xx-1])/(matrixRaw[0][xx]-matrixRaw[0][xx-x])
    matrixRaw[1] = matrixfx.copy()
    print(matrixRaw)
    print("-------------------")

n5 = 0
for x in range(0,matrixRaw.shape[1]):
    if(x==0):
        n5 += matrixRaw[1][x]
    else :
        n5 += matrixRaw[1][x]*(0.596-matrixRaw[0][x-1])

print(n5)