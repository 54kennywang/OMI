def above(inputfile, X):
    inputData = open(inputfile, "r", encoding = "ISO-8859-1") # '2016_left_join.csv'
    
   
    x = -1
    counter = 0
    PCODE3_dic = {} # {PCODE3:[Pop2016, Instability_DA16, Deprivation_DA16, Dependency_DA16, Ethniccon_DA16, Instability_q_DA16, Deprivation_q_DA16, Dependency_q_DA16, Ethniccon_q_DA16, counter]}
    for line in inputData:
        if(x == -1):
            x += 1
        else:
            x += 1
            dataList = line.split(',')
            if(float(dataList[1]) >= X and float(dataList[2]) >= X and float(dataList[3]) >= X and float(dataList[4]) >= X):
                counter += 1

    print('above ' + str(X) + ': ' + str(counter) + ' / ' + str(x) + ' = ' + str(float(counter/x)))

    inputData.close()


if(__name__ == '__main__'):
    # above('2016_average_within_1SD.csv', 0.7) # 0.03415559772296015
    # above('2016_average_within_2SD.csv', 0.9) # 0.8121442125237192

    above('2016_weightedAverage_q_within_1SD.csv', 0.5) # 0.9089184060721063
    above('2016_weightedAverage_q_within_1SD.csv', 0.7) # 0.15370018975332067
    above('2016_weightedAverage_q_within_2SD.csv', 0.9) # 0.9259962049335864

    above('UHN_2016_weightAverage_q_within_1SD.csv', 0.5) # 0.5466101694915254
    above('UHN_2016_weightAverage_q_within_1SD.csv', 0.7) # 0.07203389830508475
    above('UHN_2016_weightAverage_q_within_2SD.csv', 0.9) # 0.7584745762711864

