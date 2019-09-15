import statistics 

def calculateAll(inputfile_name, outputfile_name):
    inputData = open(inputfile_name, "r", encoding = "ISO-8859-1") # open the file
    outputFile = open(outputfile_name,"w")
    outputFile.write('SD_Instability_DA16,SD_Deprivation_DA16,SD_Dependency_DA16,SD_Ethniccon_DA16,SD_Instability_q_DA16,SD_Deprivation_q_DA16,SD_Dependency_q_DA16,SD_Ethniccon_q_DA16,PCODE3,count\n')        
   
    x = 0
    PCODE3_dic = {} # {PCODE3:[Pop2016, Instability_DA16, Deprivation_DA16, Dependency_DA16, Ethniccon_DA16, Instability_q_DA16, Deprivation_q_DA16, Dependency_q_DA16, Ethniccon_q_DA16, counter]}
    for line in inputData:
        if(x == 0):
            x = x + 1
        else:
            dataList = line.split(',')
            if(dataList[-1] in PCODE3_dic):
                PCODE3_dic[dataList[-1]][0].append(float(dataList[2]))
                PCODE3_dic[dataList[-1]][1].append(float(dataList[3]))
                PCODE3_dic[dataList[-1]][2].append(float(dataList[4]))
                PCODE3_dic[dataList[-1]][3].append(float(dataList[5]))
                PCODE3_dic[dataList[-1]][4].append(float(dataList[6]))
                PCODE3_dic[dataList[-1]][5].append(float(dataList[7]))
                PCODE3_dic[dataList[-1]][6].append(float(dataList[8]))
                PCODE3_dic[dataList[-1]][7].append(float(dataList[9]))
            else:
                PCODE3_dic[dataList[-1]] = [
                [float(dataList[2])],
                [float(dataList[3])],
                [float(dataList[4])],
                [float(dataList[5])],
                [int(dataList[6])],
                [int(dataList[7])],
                [int(dataList[8])],
                [int(dataList[9])]
                ]
    for pcode in PCODE3_dic:
        result = ''
        if(len(PCODE3_dic[pcode][0]) == 1):
        	result = ('0,' + '0,' + '0,' + '0,' + '0,' + '0,' + '0,' + '0,' + str(pcode.rstrip()) + ',1')
        else:
	        result = (
	        str(statistics.stdev(PCODE3_dic[pcode][0])) + ',' + 
	        str(statistics.stdev(PCODE3_dic[pcode][1])) + ',' + 
	        str(statistics.stdev(PCODE3_dic[pcode][2])) + ',' + 
	        str(statistics.stdev(PCODE3_dic[pcode][3])) + ',' + 
	        str(statistics.stdev(PCODE3_dic[pcode][4])) + ',' + 
	        str(statistics.stdev(PCODE3_dic[pcode][5])) + ',' + 
	        str(statistics.stdev(PCODE3_dic[pcode][6])) + ',' + 
	        str(statistics.stdev(PCODE3_dic[pcode][7])) + ',' + 
	        str(pcode.rstrip()) + ',' + 
	        str(len(PCODE3_dic[pcode][0]))
	        )

        outputFile.write(result + '\n')
    inputData.close()
    outputFile.close()

if(__name__ == '__main__'):
    calculateAll('2016_left_join.csv', '2016_standard_derivation.csv')
    # calculateAll('prac.csv', 'prac_SD.csv')
