import numpy as np
import math

def norm(matrix):
    #取得一个矩阵的行范数
    l = list()
    for x in range(matrix.shape[0]):
        l.append(np.sum(np.abs(matrix[x])))
    return max(l)



dataRaw = [
    [10,-1,-2,7.2],
    [-1,10,-2,8.3],
    [-1,-1,5,4.2]
]
matrixRaw = np.array(dataRaw)
ansRaw = np.zeros(matrixRaw.shape[0])# k=0  array([ 0.,  0.,  0.])
ans = np.zeros(matrixRaw.shape[0])# k=1 array([ 0.,  0.,  0.])

for x in range(0,ansRaw.shape[0]):
    # x(0,3)
    ans[x] = (matrixRaw[x][matrixRaw.shape[1]-1] - np.dot(ansRaw,matrixRaw[x][0:matrixRaw.shape[1]-1]) +matrixRaw[x][x]*ansRaw[x])/matrixRaw[x][x]
    # ans : array([ 0.72,  0.83,  0.84])
print(norm(ans))
print(norm(ansRaw))
while ((norm(ans)-norm(ansRaw))>0.5*math.pow(10,-5)):
    ansRaw = ans.copy()
    print(ansRaw)
    for x in range(0,ansRaw.shape[0]):
        ans[x] = (matrixRaw[x][matrixRaw.shape[1]-1] - np.dot(ansRaw,matrixRaw[x][0:matrixRaw.shape[1]-1]) +matrixRaw[x][x]*ansRaw[x])/matrixRaw[x][x]
        
print(ans)