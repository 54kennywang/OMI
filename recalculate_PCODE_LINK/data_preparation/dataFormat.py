# inputfile_name = "dups.txt"
# outputfile_name = "dups.csv"


def DA_PCODE(inputfile_name, outputfile_name, digits):
    inputData = open(inputfile_name, "r", encoding = "ISO-8859-1") # open the file
    outputFile1 = open(outputfile_name + '1',"w")
    outputFile2 = open(outputfile_name + '2',"w")
    # outputFile = open(outputfile_name,"w")
    t = 0
    if (digits == 6):
        outputFile.write('DAUID,PCODE6\n')
    else:
        outputFile1.write('DAUID,PCODE3\n')    	
        outputFile2.write('DAUID,PCODE3\n')    	
        # outputFile.write('DAUID,PCODE3\n')    	
    for line in inputData:
        t = t + 1
        line = ' '.join(line.split())
        dataList = line.split(' ')
        # print (dataList[-6])
        dataList[0] = dataList[0][:6]
        a = 0
        for x in range(-2 ,-8, -1):
            if(len(str(dataList[x])) >= 42):
                a = x
                break

        index = dataList[a].find('.')
        result = ''
        if (digits == 6):
            result = str(dataList[a][index + 19: index + 27]) + ',' + dataList[0] + '\n'
        else:
            result = str(dataList[a][index + 19: index + 27]) + ',' + dataList[0][0: 3] + '\n'
        if(t < 1000000):
            outputFile1.write(result)
        else:
            outputFile2.write(result)
        # outputFile.write(result)
    inputData.close()
    outputFile1.close()
    outputFile2.close()


if(__name__ == '__main__'):
    # DA_PCODE('dups.txt', 'dups.csv')
    # DA_PCODE("PCCF1706.PCCF.DUPS.txt", "dups_DA_PCODE6.csv", 6)
    # DA_PCODE("PCCF1706.PCCF.UNIQ.txt", "uniq_DA_PCODE6.csv", 6)

    DA_PCODE("PCCF1706.PCCF.DUPS.txt", "dups_DA_PCODE3.csv", 3)
    # DA_PCODE("PCCF1706.PCCF.UNIQ.txt", "uniq_DA_PCODE3.csv", 3)
