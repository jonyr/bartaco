# importing the pandas library
from csv import QUOTE_NONNUMERIC, QUOTE_MINIMAL
from operator import index
from numpy import int_
import pandas as pd

# reading the csv file

ORIGINAL = 'juicer file output 9-29.csv'
PRICE_CHANGE = 'price_change_THURSDAY_17hr.csv'
COL_NAME = 'Price Seq'
COL_NEW_PRICE = 'Price 1'

df1 = pd.read_csv(ORIGINAL)
print(df1.head())

df1_columns = df1.columns
df2 = pd.read_csv(PRICE_CHANGE, usecols=[COL_NAME, COL_NEW_PRICE], index_col=[COL_NAME])
print('df1', df1['Price Seq'].head())
print('df2', df2['Price Seq'].head())
df2['Price Seq']=df2['Price Seq'].astype('float64')
df3=df1.merge(df2, on='Price Seq', how='inner')

df3['Price 1_x']=df3['Price 1_y']
df3.drop(['Price 1_y'], axis=1, inplace=True)
#df3=df3.drop('Price 1_y')
df3.rename(columns={'Price 1_x': 'Price 1'}, inplace=True)
#df3.rename('Price 1_x', 'Price 1')
print(df3.shape)

#df1.set_index(COL_NAME, inplace=True)
#print(df1)
#df1.update(df2.set_index(COL_NAME))
#df1.reset_index(inplace=True)
#df1[df1_columns].to_csv("test_final.csv", quoting=QUOTE_NONNUMERIC, index=False, line_terminator='\r\n')
