import pandas as pd
def loadData(inputFile):
    # colnames = ['Instability_q_DA16', 'PCODE3']
    df = pd.read_csv(inputFile, usecols=[5, 9])
    Instability_q_DA16 = df.Instability_q_DA16.tolist()
    PCODE3 = df.PCODE3.tolist()
    print(Instability_q_DA16)
    print()
    print(PCODE3)
    return Instability_q_DA16, PCODE3

if(__name__ == '__main__'):
    loadData('2016_weightedAverage_calculated_quintiles.csv')