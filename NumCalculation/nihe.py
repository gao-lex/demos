import numpy as np

dataRaw = [
    [0,0.5,0.6,0.7,0.8,0.9,1.0],
    [1,1.75,1.96,2.19,2.44,2.71,3.00]
]
# 另一组数据
# dataRaw = [
#     [19.1,25.0,30.1,36.0,40.0,45.1,50.0],
#     [76.30,77.80,79.25,80.80,82.35,83.90,85.10]
# ]

# 第三组数据
# dataRaw = [
#     [1,3,4,5,6,7,8,9,10],
#     [10,5,4,2,1,1,2,3,4]
# ]

matrix = np.array(dataRaw)
tCopy = matrix[0].copy()
rCopy = matrix[1].copy()

lineA = [
    [matrix.shape[1],tCopy.sum(),(tCopy*tCopy).sum()],
    [tCopy.sum(),(tCopy*tCopy).sum(),(tCopy*tCopy*tCopy).sum()],
    [(tCopy*tCopy).sum(),(tCopy*tCopy*tCopy).sum(),(tCopy*tCopy*tCopy*tCopy).sum()]
]
lineB = [rCopy.sum(),(tCopy*rCopy).sum(),(tCopy*tCopy*rCopy).sum()]

matrixLineA = np.array(lineA)
matrixLineB = np.array(lineB)
x = np.linalg.solve(matrixLineA,matrixLineB)

print(x)