# importing the pandas library
from csv import QUOTE_NONNUMERIC
from numpy import int_
import pandas as pd

# reading the csv file

ORIGINAL = 'original.csv'
PRICE_CHANGE = 'changes.csv'
COL_NAME = 'Price Seq'
COL_NEW_PRICE = 'Price'

df1 = pd.read_csv(ORIGINAL)
df1_columns = df1.columns
df2 = pd.read_csv(PRICE_CHANGE, usecols=[COL_NAME, COL_NEW_PRICE])

df1.set_index(COL_NAME, inplace=True)
df1.update(df2.set_index(COL_NAME))
df1.reset_index(inplace=True)
df1[df1_columns].to_csv("test_final.csv", index=False, quotechar='"', quoting=QUOTE_NONNUMERIC, lineterminator='\r\n')
