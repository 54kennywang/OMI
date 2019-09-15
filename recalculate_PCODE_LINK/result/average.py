def average_for_PCODE3(inputfile_name, outputfile_name, year):
    inputData = open(inputfile_name, "r", encoding = "ISO-8859-1") # open the file
    outputFile = open(outputfile_name,"w")
    if(int(year) == 2016):
        outputFile.write('Pop2016,Instability_DA16,Deprivation_DA16,Dependency_DA16,Ethniccon_DA16,Instability_q_DA16,Deprivation_q_DA16,Dependency_q_DA16,Ethniccon_q_DA16,PCODE3\n')        
    else:
        outputFile.write('Pop2006,Instability_DA06,Deprivation_DA06,Dependency_DA06,Ethniccon_DA06,Instability_q_DA06,Deprivation_q_DA06,Dependency_q_DA06,Ethniccon_q_DA06,PCODE3\n')        
    x = 0
    PCODE3_dic = {} # {PCODE3:[Pop2016, Instability_DA16, Deprivation_DA16, Dependency_DA16, Ethniccon_DA16, Instability_q_DA16, Deprivation_q_DA16, Dependency_q_DA16, Ethniccon_q_DA16, counter]}
    for line in inputData:
        if(x == 0):
            x = x + 1
        else:
            dataList = line.split(',')
            if(dataList[-1] in PCODE3_dic):
                PCODE3_dic[dataList[-1]][0] = float(PCODE3_dic[dataList[-1]][0]) + float(dataList[1])
                PCODE3_dic[dataList[-1]][1] = float(PCODE3_dic[dataList[-1]][1]) + float(dataList[2])
                PCODE3_dic[dataList[-1]][2] = float(PCODE3_dic[dataList[-1]][2]) + float(dataList[3])
                PCODE3_dic[dataList[-1]][3] = float(PCODE3_dic[dataList[-1]][3]) + float(dataList[4])
                PCODE3_dic[dataList[-1]][4] = float(PCODE3_dic[dataList[-1]][4]) + float(dataList[5])
                PCODE3_dic[dataList[-1]][5] = float(PCODE3_dic[dataList[-1]][5]) + float(dataList[6])
                PCODE3_dic[dataList[-1]][6] = float(PCODE3_dic[dataList[-1]][6]) + float(dataList[7])
                PCODE3_dic[dataList[-1]][7] = float(PCODE3_dic[dataList[-1]][7]) + float(dataList[8])
                PCODE3_dic[dataList[-1]][8] = float(PCODE3_dic[dataList[-1]][8]) + float(dataList[9])
                PCODE3_dic[dataList[-1]][9] = PCODE3_dic[dataList[-1]][9] + 1
            else:
                PCODE3_dic[dataList[-1]] = [float(dataList[1]), float(dataList[2]), float(dataList[3]), float(dataList[4]), float(dataList[5]), float(dataList[6]), float(dataList[7]), float(dataList[8]), float(dataList[9]), 1]
    for pcode in PCODE3_dic:
        result = ''
        result = str(round(float(PCODE3_dic[pcode][0])/float(PCODE3_dic[pcode][-1]))) + ',' + str(float(PCODE3_dic[pcode][1])/float(PCODE3_dic[pcode][-1])) + ',' + str(float(PCODE3_dic[pcode][2])/float(PCODE3_dic[pcode][-1])) + ',' + str(float(PCODE3_dic[pcode][3])/float(PCODE3_dic[pcode][-1])) + ',' + str(float(PCODE3_dic[pcode][4])/float(PCODE3_dic[pcode][-1])) + ',' + str(round(float(PCODE3_dic[pcode][5])/float(PCODE3_dic[pcode][-1]))) + ',' + str(round(float(PCODE3_dic[pcode][6])/float(PCODE3_dic[pcode][-1]))) + ',' + str(round(float(PCODE3_dic[pcode][7])/float(PCODE3_dic[pcode][-1]))) + ',' + str(round(float(PCODE3_dic[pcode][8])/float(PCODE3_dic[pcode][-1]))) + ',' + str(pcode)
        # print(result)
        outputFile.write(result)
    inputData.close()
    outputFile.close()


if(__name__ == '__main__'):
    # average_for_PCODE3('dups.csv', 'delete.csv')
    average_for_PCODE3('2006_left_join.csv', '2006_average_round.csv', 2006)
    average_for_PCODE3('2016_left_join.csv', '2016_average_round.csv', 2016)
