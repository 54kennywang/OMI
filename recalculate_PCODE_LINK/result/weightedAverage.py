def average_for_PCODE3(inputfile_name, outputfile_name, year):
    inputData = open(inputfile_name, "r", encoding = "ISO-8859-1") # open the file
    outputFile = open(outputfile_name,"w")
    if(int(year) == 2016):
        outputFile.write('TotalPop2016,Instability_DA16,Deprivation_DA16,Dependency_DA16,Ethniccon_DA16,Instability_q_DA16,Deprivation_q_DA16,Dependency_q_DA16,Ethniccon_q_DA16,PCODE3\n')        
    else:
        outputFile.write('TotalPop2006,Instability_DA06,Deprivation_DA06,Dependency_DA06,Ethniccon_DA06,Instability_q_DA06,Deprivation_q_DA06,Dependency_q_DA06,Ethniccon_q_DA06,PCODE3\n')        
    x = 0
    PCODE3_dic = {} # {PCODE3:[Pop2016, Instability_DA16, Deprivation_DA16, Dependency_DA16, Ethniccon_DA16, Instability_q_DA16, Deprivation_q_DA16, Dependency_q_DA16, Ethniccon_q_DA16, counter]}
    for line in inputData:
        if(x == 0):
            x = x + 1
        else:
            dataList = line.split(',')
            if(dataList[-1] in PCODE3_dic):
                PCODE3_dic[dataList[-1]][0] = int(PCODE3_dic[dataList[-1]][0]) + int(dataList[1]) # total pop
                PCODE3_dic[dataList[-1]][1] = float(PCODE3_dic[dataList[-1]][1]) + float(float(dataList[2]) * int(dataList[1])) # Instability_DA16
                PCODE3_dic[dataList[-1]][2] = float(PCODE3_dic[dataList[-1]][2]) + float(float(dataList[3]) * int(dataList[1])) # Deprivation_DA16
                PCODE3_dic[dataList[-1]][3] = float(PCODE3_dic[dataList[-1]][3]) + float(float(dataList[4]) * int(dataList[1])) # Dependency_DA16
                PCODE3_dic[dataList[-1]][4] = float(PCODE3_dic[dataList[-1]][4]) + float(float(dataList[5]) * int(dataList[1])) # Ethniccon_DA16
                PCODE3_dic[dataList[-1]][5] = int(PCODE3_dic[dataList[-1]][5]) + int(dataList[6]) * int(dataList[1]) # Instability_q_DA16
                PCODE3_dic[dataList[-1]][6] = int(PCODE3_dic[dataList[-1]][6]) + int(dataList[7]) * int(dataList[1]) # Deprivation_q_DA16
                PCODE3_dic[dataList[-1]][7] = int(PCODE3_dic[dataList[-1]][7]) + int(dataList[8]) * int(dataList[1]) # Dependency_q_DA16
                PCODE3_dic[dataList[-1]][8] = int(PCODE3_dic[dataList[-1]][8]) + int(dataList[9]) * int(dataList[1]) # Ethniccon_q_DA16
                PCODE3_dic[dataList[-1]][9] = PCODE3_dic[dataList[-1]][9] + 1 # count
            else:
                PCODE3_dic[dataList[-1]] = [int(dataList[1]),
                float(float(dataList[2]) * int(dataList[1])),
                float(float(dataList[3]) * int(dataList[1])),
                float(float(dataList[4]) * int(dataList[1])),
                float(float(dataList[5]) * int(dataList[1])),
                int(dataList[6]) * int(dataList[1]),
                int(dataList[7]) * int(dataList[1]),
                int(dataList[8]) * int(dataList[1]),
                int(dataList[9]) * int(dataList[1]),
                1]
    for pcode in PCODE3_dic:
        result = ''
        # print (PCODE3_dic[pcode])
        result = (str(int(PCODE3_dic[pcode][0])) + ',' + 
        str(float(float(PCODE3_dic[pcode][1]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(float(float(PCODE3_dic[pcode][2]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(float(float(PCODE3_dic[pcode][3]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(float(float(PCODE3_dic[pcode][4]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(float(int(PCODE3_dic[pcode][5]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(float(int(PCODE3_dic[pcode][6]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(float(int(PCODE3_dic[pcode][7]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(float(int(PCODE3_dic[pcode][8]) / (PCODE3_dic[pcode][0]))) + ',' + 
        str(pcode))

        outputFile.write(result)
    inputData.close()
    outputFile.close()


if(__name__ == '__main__'):
    # average_for_PCODE3('2006_left_join.csv', '2006_average_round.csv', 2006)
    average_for_PCODE3('2016_left_join.csv', '2016_weightedAverage.csv', 2016)
    # average_for_PCODE3('practice_input.csv', '2016_weightedAveragePractice_round.csv', 2016)
