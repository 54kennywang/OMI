import geopandas
import pandas_bokeh
import matplotlib.pyplot as plt
import pandas as pd
import time
# from bokeh.models.glyphs import MultiLine
# from bokeh.models import ColumnDataSource
# from bokeh.plotting import figure, show, output_file

def loadData(inputFile):
    # colnames = ['Instability_q_DA16', 'PCODE3']
    df = pd.read_csv(inputFile, usecols=[5, 9])
    Instability_q_DA16 = df.Instability_q_DA16.tolist()
    PCODE3 = df.PCODE3.tolist()
    # print(len(Instability_q_DA16))
    # print()
    # print(len(PCODE3))
    return Instability_q_DA16, PCODE3

pandas_bokeh.output_notebook()

canada = geopandas.read_file("./ONldu.shp")
# print(type(canada)) # <class 'geopandas.geodataframe.GeoDataFrame'>

# print(canada.columns) # Index(['PCA_ID', 'POSTALCODE', 'PROV', 'MAF_ID', 'PREC_CODE', 'PCA_COUNT', 'DOM_PCA', 'MULTI_PC', 'DEL_M_ID', 'LONGITUDE', 'LATITUDE', 'geometry'], dtype='object')
print(canada['POSTALCODE'])
# ontario = canada[canada['PRUID'] == '35']


# Sample data to plot
# Instability_q_DA16, PCODE3 = loadData('2016_weightedAverage_calculated_quintiles.csv')
# # df=pd.DataFrame({'PCODE': ['P0V','P0L','P0T','P0Y', 'P0G', 'P2N'], 'A':[6,3,5,2,2,4] })
# df=pd.DataFrame({'PCODE': PCODE3, 'A':Instability_q_DA16})
df=pd.DataFrame({'PCODE': ['M5H3G8', 'M5H2N2', 'M5H2G4', 'M5H3Y2'], 'A':[6,3,5,2] })

# Join ontario dataset with sample data
# new_df=ontario.join(df.set_index('PCODE'), on='CFSAUID')
new_df=canada.join(df.set_index('PCODE'), on='POSTALCODE')

start_time = time.time()
new_df.plot_bokeh(simplify_shapes=5000,
                  category="A",
                  colormap="Spectral",
                  hovertool_columns=["POSTALCODE","A"])
print("--- %s seconds ---" % (time.time() - start_time))