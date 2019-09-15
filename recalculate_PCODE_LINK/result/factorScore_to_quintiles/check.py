import csv
def check(inputFile1, inputFile2):
    with open(inputFile1, 'r') as f:
        reader = csv.reader(f)
        dataList = list(reader)
    dataList = dataList[1:]
    arr = []
    for i in range(len(dataList)):
        arr.append(dataList[i][0])
    with open(inputFile1, 'r') as f:
        reader = csv.reader(f)
        dataList = list(reader)
    dataList = dataList[1:]
    for i in range(len(dataList)):
        if(dataList[i][0] not in arr):
            print('false')
            return
    print('true')

if(__name__ == '__main__'):
    check('2016_weightedAverage_calculated_quintiles.csv', '2016_weightedAverage_round.csv')