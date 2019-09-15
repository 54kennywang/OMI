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
            if(float(dataList[1]) >= X and float(dataList[2]) >= X and float(dataList[3]) >= X and float(dataList[4]) >= X and float(dataList[5]) >= X and float(dataList[6]) >= X and float(dataList[7]) >= X and float(dataList[8]) >= X):
                counter += 1

    print('above ' + str(X) + ': ' + str(counter) + ' / ' + str(x) + ' = ' + str(float(counter/x)))

    inputData.close()


if(__name__ == '__main__'):
    # above('2016_average_within_1SD.csv', 0.7) # 0.03415559772296015
    # above('2016_average_within_2SD.csv', 0.9) # 0.8121442125237192

    above('2016_weightedAverage_within_1SD.csv', 0.5) # 0.5256166982922201
    above('2016_weightedAverage_within_1SD.csv', 0.7) # 0.026565464895635674
    above('2016_weightedAverage_within_2SD.csv', 0.9) # 0.7343453510436433

    above('UHN_2016_weightAverage_within_1SD.csv', 0.5) # 0.4788135593220339
    above('UHN_2016_weightAverage_within_1SD.csv', 0.7) # 0.01694915254237288
    above('UHN_2016_weightAverage_within_2SD.csv', 0.9) # 0.7288135593220338

