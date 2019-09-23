import csv
from operator import itemgetter
def factorScore_to_quintiles(inputFile, outputFile):
    with open(inputFile, 'r') as f:
        reader = csv.reader(f)
        dataList = list(reader)
    row1 = dataList[0]
    dataList = dataList[1:]
    # print(dataList)
    for i in range(len(dataList)):
        for j in range(1, 5):
            dataList[i][j] = float(dataList[i][j])

    numRow = len(dataList)
    # print(numRow)
    for i in range (1, 5):
        dataList = sorted(dataList, key=itemgetter(i))
        for j in range(4):
            for x in range(int(float(j*numRow)/4), int(float((j+1)*numRow)/4)):
                dataList[x][i+4] = j + 1
    dataList.insert(0, row1)
    with open(outputFile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(dataList)

if(__name__ == '__main__'):
    factorScore_to_quintiles('2016_weightedAverage_round.csv', '2016_weightedAverage_calculated_quintiles.csv')
    # factorScore_to_quintiles('practice.csv', '2016_weightedAverage_calculated_quintiles.csv')