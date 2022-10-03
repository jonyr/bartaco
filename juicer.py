# importing the pandas library
from csv import QUOTE_NONNUMERIC
import pandas as pd

# reading the csv file

ORIGINAL = 'juicer file output 9-29.csv'
PRICE_CHANGE = 'price_change_THURSDAY_17hr.csv'
COL_NAME = 'Price Seq'
COL_NEW_PRICE = 'Price 1'
FINAL_NAME = 'updated_price.csv'

df1 = pd.read_csv(ORIGINAL)
df1_columns = df1.columns
df1[COL_NAME] = df1[COL_NAME].astype('int')
df2 = pd.read_csv(PRICE_CHANGE, usecols=[COL_NAME, COL_NEW_PRICE])

df1.set_index(COL_NAME, inplace=True)
df1.update(df2.set_index(COL_NAME))
df1.reset_index(inplace=True)

print(df1.sample())
# df1[['Item name', 'Price Seq', 'Price 1']].to_csv(FINAL_NAME, index=False, quotechar='"', quoting=QUOTE_NONNUMERIC, lineterminator='\r\n')
# df1.to_csv(FINAL_NAME, index=False, quotechar='"', quoting=QUOTE_NONNUMERIC, lineterminator='\r\n')
