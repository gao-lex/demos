import numpy as np

def exchange(dataMatrix, dataRow, dataLine, dataMain):
    dataMatrix[[dataMain, dataRow+dataMain]] = dataMatrix[[dataRow+dataMain, dataMain]]  # 花式索引，转换行
    dataTMatrix = dataMatrix.T.copy()  # 花式索引，转换列
    dataTMatrix[[dataMain, dataLine+dataMain]] = dataTMatrix[[dataLine+dataMain, dataMain]]
    dataMatrix = dataTMatrix.T
    return dataMatrix

def elimination (dataMatrix,dataMain):
    # 消元，此处传入的默认为引用，不需返回
    for row in range(dataMain+1,dataMatrix.shape[0]):
        l = dataMatrix[row][dataMain]/dataMatrix[dataMain][dataMain]
        print(l)
        for mamber in range(0,dataMatrix.shape[1]):
            dataMatrix[row][mamber] = dataMatrix[row][mamber] - l * dataMatrix[dataMain][mamber]
        print(dataMatrix)

def completeMain(datalist):
    # 完全主元素
    rank = datalist[0] # 阶数
    order = list(range(1, rank + 1))# order为方程值的序号
    order.append(0)
    matrix = np.array(datalist[1:])  # 去掉rank
    for mainElement in range(0, rank - 1):
        absMatrix = abs(matrix)  # 绝对值化
        absMatrixRemoveB = absMatrix[mainElement:rank, mainElement:rank]  #去掉b值,是一个引用
        posMax = np.where(absMatrixRemoveB == np.max(absMatrixRemoveB))
        row = posMax[0][0]  # 绝对值最大者所处的行
        line = posMax[1][0]  # 绝对值最大者所处的列
        if row == 0 and line == 0:
            elimination(matrix,mainElement)
        else:
            matrix = exchange(matrix, row, line, mainElement)
            order[line],order[mainElement] = order[mainElement],order[line]#交换方程值序号
            print(matrix)
            elimination(matrix,mainElement)
    return matrix,order

def backSubstitutionb(dataMatrix):
    answer = []
    for row in range(dataMatrix.shape[0],0,-1):
        temp = 0
        for x in range(row,dataMatrix.shape[1]-1):
            temp = temp+dataMatrix[row-1][x]
        answer.insert(0,(dataMatrix[row-1][dataMatrix.shape[1]-1]-temp)/dataMatrix[row-1][row-1])
        for x in range(0,row-1):
            dataMatrix[x][row-1] = dataMatrix[x][row-1]*answer[0]
    return answer

dataRaw = [
    4, 
    [0.03, 59.14, 3, 1,59.17], 
    [5.291, -6.130, -1, 2,46.78],
    [11.2, 9, 5, 2,1],
    [1,2,1,1,2]
]

dataComEli = completeMain(dataRaw)
ans = backSubstitutionb(dataComEli[0])
print(ans)
print(dataComEli[1][:-1])