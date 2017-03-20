import numpy as np

dataRaw = [
    [4,2,1,5,-2], 
    [8,7,2,10,-7],
    [4,8,3,6,-7],
    [12,6,11,20,-3]
]
# dataRaw = [
#     [,,,,],
#     [,,,,],
#     [,,,,],
#     [,,,,]
# ]
matrixRaw = np.array(dataRaw)
matrix = matrixRaw[:matrixRaw.shape[0],:matrixRaw.shape[0]]
bMatrix = matrixRaw[:matrixRaw.shape[0],matrixRaw.shape[0]:]
lMatrix = np.eye(matrix.shape[0])
uMatrix = np.zeros(matrix.shape)

uMatrix[0] = matrix[0]
for x in range(1,matrix.shape[0]):
    lMatrix[x][0] = matrix[x][0]/matrix[0][0]

## lu分解
for i in range(1,matrix.shape[0]):
    for j in range(i,matrix.shape[0]):
        temp = np.dot(lMatrix[i][0:i],uMatrix[0:i,j])
        uMatrix[i][j] = matrix[i][j] - temp
        temp = np.dot(lMatrix[j][0:i],uMatrix[0:i,i])
        lMatrix[j][i] = (matrix[j][i]-temp)/uMatrix[i][i]

print(uMatrix)
print(lMatrix)

lMatrixWithb = np.column_stack((lMatrix,bMatrix))

yAnswer = []
for x in range(0,lMatrixWithb.shape[0]):
    yAnswer.append(lMatrixWithb[x][lMatrixWithb.shape[1]-1] - np.sum(lMatrixWithb[x][0:x]))
    lMatrixWithb[x+1:lMatrixWithb.shape[0],x] = lMatrixWithb[x+1:lMatrixWithb.shape[0],x] *yAnswer[len(yAnswer)-1]

uMatrixWithy = np.column_stack((uMatrix,np.array(yAnswer)))
xAnswer = []
for x in range(uMatrixWithy.shape[0]-1,-1,-1):
    xAnswer.insert(0,(  uMatrixWithy[x][uMatrixWithy.shape[1]-1]-np.sum(uMatrixWithy[x][x+1:uMatrixWithy.shape[1]-1]))/uMatrixWithy[x][x])
    uMatrixWithy[0:x,x] = uMatrixWithy[0:x,x] * xAnswer[0]
print(xAnswer)
