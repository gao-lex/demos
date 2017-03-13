def display(DataList):
    rank = DataList[0]
    for x in range(0,rank):
        print(DataList[x+1])

def format(DataList):
    rank = int(DataList[0])
    DataList[0] = int(DataList[0])
    for x in range(1,rank+1):
        TempList = DataList[x].strip('\n').split(' ')
        for xx in range(0,len(TempList)):
            TempList[xx] = int(TempList[xx]) 
        DataList[x] =  TempList
    return DataList

def elimination(DataList):
    # 消元
    rank = DataList[0]
    print('消元开始---------------------')
    main = 1
    for x in range(0,rank-1):
        for xx in range(x+2,rank+1):
            l = DataList[xx][x]/DataList[main][main-1]
            for xxx in range(0,len(DataList[xx])):
                DataList[xx][xxx] = DataList[xx][xxx] - l*DataList[main][xxx]
            display(DataList)
        main = main+1
    print('消元结束---------------------')
    return DataList

def backSubstitutionb(DataList):
    rank = DataList[0]
    answer = []
    for x in range(0,rank):
        if x==0:
            answer.insert(0,DataList[rank][rank]/DataList[rank][rank-1])
            for xx in range(0,rank-x-1):
                DataList[xx+1][rank-1] = DataList[xx+1][rank-1]*answer[0]
        else :
            temp = 0
            for xx in range(0,x):
                temp = temp + DataList[rank-x][rank-xx-1]
            print(temp)
            answer.insert(0,(DataList[rank-x][rank]-temp)/DataList[rank-x][rank-x-1])
            for xx in range(0,rank-1-x):
                DataList[xx+1][rank-x-1] = DataList[xx+1][rank-1-x]*answer[0]
    return answer

gaussDataList = format(open('gaussdata.txt').readlines())
# gaussDataList = format(open('gaussdata-1.txt').readlines())
gaussDataList = elimination(gaussDataList)
print(backSubstitutionb(gaussDataList))
