import csv
import pandas as pd


df = pd.read_csv('sales.csv')


df['sales'] = (df.row['jan'] - df.row['feb']) / df.row['jan'] * 100



#df.pct_change( )



# NaN
# **kwargs

# percentage is about taking the number from before, the number next and dividing
# then multiplying by 100

