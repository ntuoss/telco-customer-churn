#warning, this file is not gonna be very professional
#Its also gonna be full of stupid comments to entertain myself



# importing stuff that i'll (probably) need
import pandas as pd
import numpy as np
import math
import os
#apparently this is useful
import warnings

#this did not do anything LOL
#edit:i figured it out!
print(os.listdir("../telco-customer-churn/data"))

#reading in the data(at least i think i did, theres a little tick so im hopeful :) )
data = pd.read_csv("../telco-customer-churn/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

#this returns the top 10 rows of data(tails returns the bottom rows)
data.head(10)
#tbh it looks pretty clean to me LOL
#why do the strings not have inverted commas like during the pandas workshop

#gets overview of dataframe -> number of rows, indexes, and all that good stuff
data.info()
#oh theres only 21 columns
#i guess i can change all the 'yes' and 'no' to booleans

#shows only the columns with numbers and stats of the columns
data.describe()

#shows number of rows and columns respectively
data.shape
#wow thats a lot of rows

#shows column names
data.columns

#displays the "customerID" column
data["customerID"]

#flipping columns and rows
data.T

#for filtering(in this case its finding all the rows with 'male' in the 'gender column')

data[data['gender'].isin(['Male'])]

#also lists out the data
data

#data.dropna(how='any') drops rows that have missing data
#data.fillna(value=5) fills in missing data with 5

#displays the data and shows whether there are any missing values(not very useful though)
pd.isna(data)
