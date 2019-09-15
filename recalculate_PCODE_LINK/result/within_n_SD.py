import statistics 

def within_SD(inputfile1, inputfile2, outputfile_name, N):
    inputData1 = open(inputfile1, "r", encoding = "ISO-8859-1") # '2016_left_join.csv'
    inputData2 = open(inputfile2, "r", encoding = "ISO-8859-1") # '2016_weightedAverage_and_SD.csv'
    outputFile = open(outputfile_name,"w")

    outputFile.write(
    'PCODE3,' + 
    'in' + str(N) + 'SD_Instability_DA16,' + 
    'in' + str(N) + 'SD_Deprivation_DA16,' + 
    'in' + str(N) + 'SD_Dependency_DA16,' + 
    'in' + str(N) + 'SD_Ethniccon_DA16,' + 
    'in' + str(N) + 'SD_Instability_q_DA16,' + 
    'in' + str(N) + 'SD_Deprivation_q_DA16,' + 
    'in' + str(N) + 'SD_Dependency_q_DA16,' + 
    'in' + str(N) + 'SD_Ethniccon_q_DA16\n'
    )        
   
    x = 0
    PCODE3_dic = {} # {PCODE3:[Pop2016, Instability_DA16, Deprivation_DA16, Dependency_DA16, Ethniccon_DA16, Instability_q_DA16, Deprivation_q_DA16, Dependency_q_DA16, Ethniccon_q_DA16, counter]}
    for line in inputData2:
        if(x == 0):
            x = x + 1
        else:
            dataList = line.split(',')
            PCODE3_dic[dataList[9]] = [
            [float(dataList[1]) - float(N * float(dataList[10])), float(dataList[1]) + float(N * float(dataList[10]))],
            [float(dataList[2]) - float(N * float(dataList[11])), float(dataList[2]) + float(N * float(dataList[11]))],
            [float(dataList[3]) - float(N * float(dataList[12])), float(dataList[3]) + float(N * float(dataList[12]))],
            [float(dataList[4]) - float(N * float(dataList[13])), float(dataList[4]) + float(N * float(dataList[13]))],
            [float(dataList[5]) - float(N * float(dataList[14])), float(dataList[5]) + float(N * float(dataList[14]))],
            [float(dataList[6]) - float(N * float(dataList[15])), float(dataList[6]) + float(N * float(dataList[15]))],
            [float(dataList[7]) - float(N * float(dataList[16])), float(dataList[7]) + float(N * float(dataList[16]))],
            [float(dataList[8]) - float(N * float(dataList[17])), float(dataList[8]) + float(N * float(dataList[17]))],
            int(dataList[-1].rstrip())
            ]
    # PCODE3_dic: {N9G: [   [], [], [], [], [], [], [], [], 5   ]}
    # print(PCODE3_dic)
    # print('--------------------------------------------------')


    x = 0
    count_dic = {} # {PCODE3:[Pop2016, Instability_DA16, Deprivation_DA16, Dependency_DA16, Ethniccon_DA16, Instability_q_DA16, Deprivation_q_DA16, Dependency_q_DA16, Ethniccon_q_DA16, counter]}
    for line in inputData1:
        if(x == 0):
            x = x + 1
        else:
            dataList = line.split(',')
            dataList[-1] = dataList[-1].rstrip()
            dataList[2] = float(dataList[2])
            dataList[3] = float(dataList[3])
            dataList[4] = float(dataList[4])
            dataList[5] = float(dataList[5])
            dataList[6] = float(dataList[6])
            dataList[7] = float(dataList[7])
            dataList[8] = float(dataList[8])
            dataList[9] = float(dataList[9])

            if(dataList[-1] in count_dic):
                if(dataList[2] >= PCODE3_dic[dataList[-1]][0][0] and dataList[2] <= PCODE3_dic[dataList[-1]][0][1]):
                    count_dic[dataList[-1]][0] += 1
                if(dataList[3] >= PCODE3_dic[dataList[-1]][1][0] and dataList[3] <= PCODE3_dic[dataList[-1]][1][1]):
                    count_dic[dataList[-1]][1] += 1
                if(dataList[4] >= PCODE3_dic[dataList[-1]][2][0] and dataList[4] <= PCODE3_dic[dataList[-1]][2][1]):
                    count_dic[dataList[-1]][2] += 1
                if(dataList[5] >= PCODE3_dic[dataList[-1]][3][0] and dataList[5] <= PCODE3_dic[dataList[-1]][3][1]):
                    count_dic[dataList[-1]][3] += 1
                if(dataList[6] >= PCODE3_dic[dataList[-1]][4][0] and dataList[6] <= PCODE3_dic[dataList[-1]][4][1]):
                    count_dic[dataList[-1]][4] += 1
                if(dataList[7] >= PCODE3_dic[dataList[-1]][5][0] and dataList[7] <= PCODE3_dic[dataList[-1]][5][1]):
                    count_dic[dataList[-1]][5] += 1
                if(dataList[8] >= PCODE3_dic[dataList[-1]][6][0] and dataList[8] <= PCODE3_dic[dataList[-1]][6][1]):
                    count_dic[dataList[-1]][6] += 1
                if(dataList[9] >= PCODE3_dic[dataList[-1]][7][0] and dataList[9] <= PCODE3_dic[dataList[-1]][7][1]):
                    count_dic[dataList[-1]][7] += 1
            else:
                count_dic[dataList[-1]] = [0, 0, 0, 0, 0, 0, 0, 0, int(PCODE3_dic[dataList[-1]][-1])]

                if(dataList[2] >= PCODE3_dic[dataList[-1]][0][0] and dataList[2] <= PCODE3_dic[dataList[-1]][0][1]):
                    count_dic[dataList[-1]][0] += 1
                if(dataList[3] >= PCODE3_dic[dataList[-1]][1][0] and dataList[3] <= PCODE3_dic[dataList[-1]][1][1]):
                    count_dic[dataList[-1]][1] += 1
                if(dataList[4] >= PCODE3_dic[dataList[-1]][2][0] and dataList[4] <= PCODE3_dic[dataList[-1]][2][1]):
                    count_dic[dataList[-1]][2] += 1
                if(dataList[5] >= PCODE3_dic[dataList[-1]][3][0] and dataList[5] <= PCODE3_dic[dataList[-1]][3][1]):
                    count_dic[dataList[-1]][3] += 1
                if(dataList[6] >= PCODE3_dic[dataList[-1]][4][0] and dataList[6] <= PCODE3_dic[dataList[-1]][4][1]):
                    count_dic[dataList[-1]][4] += 1
                if(dataList[7] >= PCODE3_dic[dataList[-1]][5][0] and dataList[7] <= PCODE3_dic[dataList[-1]][5][1]):
                    count_dic[dataList[-1]][5] += 1
                if(dataList[8] >= PCODE3_dic[dataList[-1]][6][0] and dataList[8] <= PCODE3_dic[dataList[-1]][6][1]):
                    count_dic[dataList[-1]][6] += 1
                if(dataList[9] >= PCODE3_dic[dataList[-1]][7][0] and dataList[9] <= PCODE3_dic[dataList[-1]][7][1]):
                    count_dic[dataList[-1]][7] += 1
    # print(count_dic)
    # print('-----------------------------')

    for pcode in count_dic:
        result = ''
    
        result = (str(pcode.rstrip()) + ',' + 
        str(float(count_dic[pcode][0] / count_dic[pcode][-1])) + ',' + 
        str(float(count_dic[pcode][1] / count_dic[pcode][-1])) + ',' + 
        str(float(count_dic[pcode][2] / count_dic[pcode][-1])) + ',' + 
        str(float(count_dic[pcode][3] / count_dic[pcode][-1])) + ',' + 
        str(float(count_dic[pcode][4] / count_dic[pcode][-1])) + ',' + 
        str(float(count_dic[pcode][5] / count_dic[pcode][-1])) + ',' + 
        str(float(count_dic[pcode][6] / count_dic[pcode][-1])) + ',' + 
        str(float(count_dic[pcode][7] / count_dic[pcode][-1]))
        )

        outputFile.write(result + '\n')
        # print(result)

    inputData1.close()
    inputData2.close()
    outputFile.close()


if(__name__ == '__main__'):
    # within_SD('2016_left_join.csv', '2016_weightedAverage_and_SD.csv', '2016_weightedAverage_within_1SD.csv', 1)
    # within_SD('2016_left_join.csv', '2016_weightedAverage_and_SD.csv', '2016_weightedAverage_within_2SD.csv', 2)
    # within_SD('2016_left_join.csv', '2016_average_and_SD.csv', '2016_average_within_1SD.csv', 1)
    within_SD('2016_left_join.csv', '2016_average_and_SD.csv', '2016_average_within_2SD.csv', 2)


    # within_SD('prac1.csv', 'prac2.csv', '2016_weightedAverage_within_1SD.csv', 1)


