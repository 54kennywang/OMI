def DA_PCODE_compare(inputfile_name):
    inputData = open(inputfile_name, "r", encoding = "ISO-8859-1") # open the file
    rowIndex = 1
    nullNum = 0
    D_mismatch = 0
    P_mismatch = 0
    for line in inputData:
        # line = ' '.join(line.split())
        dataList = line.split(',')
        hasNull = False
        for item in dataList:
            if(len(str(item)) == 0):
                nullNum = nullNum + 1
                hasNull = True
                break

        if(hasNull == False): # no null in current row
            if(dataList[0] != dataList[2]):
                D_mismatch = D_mismatch + 1
                # print (rowIndex , ' DAUID mismatch')
            if(dataList[1][0: 3] != dataList[3][0: 3]):
                # print( '  ', dataList[1][0: 3], '$  ', dataList[4][0: 3], '$  ')
                P_mismatch = P_mismatch + 1
                print (rowIndex , ' PCODE3 mismatch')
        rowIndex = rowIndex + 1

    print(D_mismatch - 1, ' DAUID mismatch')
    print(P_mismatch - 1, ' PCODE3 mismatch')
    print(nullNum, ' rows of NULL')
    inputData.close()



if(__name__ == '__main__'):
    DA_PCODE_compare('PCODE_LINK_compareALL.csv')