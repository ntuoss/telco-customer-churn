#basic tools
import pandas as pd
import os
import numpy as np
#As sugguested by Anqi
import warnings
warnings.filterwarnings('ignore')

#ploting tools
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
%matplotlib inline
plt.style.use('seaborn-whitegrid')
plt.rcParams['savefig.facecolor']='white'

params = {'figure.figsize': (18,12),
            'axes.titlesize': 20}
plt.rcParams.update(params)

######################overview of the data###############################
#reading in the file
infile = "../WA_Fn-UseC_-Telco-Customer-Churn.csv"
telcom = pd.read_csv(infile)
telcom.head()
####default as 5
#DataFrame.head(n=5)[source]
#Return the first n rows.
#This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.


print ("Features : \n" ,telcom.columns.tolist())
# >>Features :
# >>['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn']

##select the column to convert tolist
##e.g. gender = telcom['gender'].tolist() ==>> [Female, Male]



print ("\nMissing values :  ", telcom.isnull().sum().values.sum())
#we have no null value! which is good, but still some datacleans need to do further


plt.figure()
#usage, pandas plot just dataframe.plot.bar(), dataframe.plot.pie()
#telcom["Churn"].value_counts().plot.pie(autopct  = "%1.0f%%",fontsize = 12,wedgeprops = {"linewidth" : 2, "edgecolor" : "w"},
                                       )
telcom['Churn'].value_counts().plot.bar()
plt.title("Churned v.s Unchurned customers")

#more usage for example three columns, want to pair speed, lifespan to the index animal

# speed = [0.1, 17.5, 40, 48, 52, 69, 88]
# lifespan = [2, 8, 70, 1.5, 25, 12, 28]
# index = ['snail', 'pig', 'elephant',
# ...          'rabbit', 'giraffe', 'coyote', 'horse']
# df = pd.DataFrame({'speed': speed,
# ...                    'lifespan': lifespan}, index=index)
#ax = df.plot.bar(rot=0)

#######################DataClean#########################

#replace 'No internet service' to N for the following columns

replace_cols = [ 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport','StreamingTV', 'StreamingMovies']
for i in replace_cols :
    telcom[i]  = telcom[i].replace({'No internet service' : 'N'})
#Replacing spaces with null values in total charges column
telcom['TotalCharges'] = telcom["TotalCharges"].replace(" ",np.nan)
