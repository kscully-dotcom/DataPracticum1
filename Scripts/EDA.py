# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:32:01 2024

@author: java
"""

import pandas as pd
from ydata_profiling import ProfileReport
import matplotlib.pyplot as plt

# Quarterly
fileGDP = pd.read_csv('Inputs/GDP.csv', names=['Date', 'GDP'], header=0)

# Monthly
fileRecession = pd.read_csv('Inputs/USREC.csv', names=['Date','Rec'], header=0)
fileCPI = pd.read_csv('Inputs/USACP030000CTGYM.csv', 
                      names=['Date', 'CPI'], header=0)

#Yearly
filePCE = pd.read_csv('Inputs/DCAFRC1A027NBEA.csv',
                                              names=['Date', 'PCE'],
                                              header=0)

fileInflation = pd.read_csv('Inputs/FPCPITOTLZGUSA.csv',
                            names=['Date', 'Inflation'], header=0)

fileWasteGenerated = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Materials generated', index_col=0)
fileWasteRecycled = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Materials recycled', index_col=0)
fileWasteLandfilled = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Materials landfilled', index_col=0)
fileWasteCombusted = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Material combusted', index_col=0)
print("GDP Dates: ", fileGDP.Date.min())
print("CPI Dates: ", fileCPI.Date.min())
print("PCE Dates: ", filePCE.Date.min())
print("Inflation Dates: ", fileInflation.Date.min())

filePCE.Date = pd.to_datetime(filePCE.Date, errors='coerce')
filePCE = filePCE.set_index('Date').resample('M').ffill().reset_index()
fileInflation.Date = pd.to_datetime(fileInflation.Date, errors='coerce')
fileInflation = fileInflation.set_index('Date').resample('M').ffill().reset_index()
fileGDP.Date = pd.to_datetime(fileGDP.Date, errors='coerce')
fileGDP = fileGDP.set_index('Date').resample('M').ffill().reset_index()

fileWasteGenerated = fileWasteGenerated.T
fileWasteGenerated = fileWasteGenerated[['Products - Textiles']].copy()
fileWasteGenerated.reset_index(inplace=True)
fileWasteGenerated.rename(columns={'index':'Date',
                                   'Products - Textiles':'WasteGenerated'},
                          inplace=True)
# =============================================================================
fileWasteGenerated.Date = pd.to_datetime(fileWasteGenerated.Date, format='%Y')
fileWasteGenerated = fileWasteGenerated.set_index('Date').resample('M').ffill().reset_index()

fileWasteRecycled = fileWasteRecycled.T
fileWasteRecycled = fileWasteRecycled[['Products - Textiles']].copy()
fileWasteRecycled.reset_index(inplace=True)
fileWasteRecycled.rename(columns={'index':'Date',
                                  'Products - Textiles':'WasteRecycled'},
                         inplace=True)
fileWasteRecycled.Date = pd.to_datetime(fileWasteRecycled.Date, format='%Y')
# ============================================================================
fileWasteRecycled = fileWasteRecycled.set_index('Date').resample('M').ffill().reset_index()

fileWasteCombusted = fileWasteCombusted.T
fileWasteCombusted = fileWasteCombusted[['Products - Textiles']].copy()
fileWasteCombusted.reset_index(inplace=True)
fileWasteCombusted.rename(columns={'index':'Date',
                                   'Products - Textiles':'WasteCombusted'},
                          inplace=True)
fileWasteCombusted.Date = pd.to_datetime(fileWasteCombusted.Date, format='%Y')
fileWasteCombusted = fileWasteCombusted.set_index('Date').resample('M').ffill().reset_index()


fileWasteLandfilled = fileWasteLandfilled.T
fileWasteLandfilled = fileWasteLandfilled[['Products - Textiles']].copy()
fileWasteLandfilled.reset_index(inplace=True)
fileWasteLandfilled.rename(columns={'index':'Date',
                                    'Products - Textiles':'WasteLandfilled'},
                           inplace=True)
fileWasteLandfilled.Date = pd.to_datetime(fileWasteLandfilled.Date, format='%Y')
fileWasteLandfilled = fileWasteLandfilled.set_index('Date').resample('M').ffill().reset_index()

fileRecession.Date = pd.to_datetime(fileRecession.Date, errors='coerce')
fileRecession = fileRecession.set_index('Date').resample('M').ffill().reset_index()

fileCPI.Date = pd.to_datetime(fileCPI.Date, errors='coerce')
fileCPI = fileCPI.set_index('Date').resample('M').ffill().reset_index()


df = fileRecession.merge(
    fileGDP, how='left').merge(
    fileInflation, how='left').merge(
    filePCE, how='left').merge(
    fileCPI, how='left').merge(
    fileWasteGenerated, how='left').merge(
    fileWasteRecycled, how='left').merge(
    fileWasteCombusted, how='left').merge(
    fileWasteLandfilled, how='left')

df['WasteRecycled'] = df['WasteRecycled']/df['WasteGenerated']
df['fileWasteCombusted'] = df['fileWasteCombusted']/df['WasteGenerated']
df['fileWasteLandfilled'] = df['fileWasteLandfilled']/df['WasteGenerated']

full = df[(df['Date'] >= '1960-01-31') & (df['Date'] <= '2022-01-31')].copy().reset_index(drop=True)
train_test = df[(df['Date'] >= '1960-01-31') & (df['Date'] <= '2018-01-31')].copy().reset_index(drop=True)
validate = df[(df['Date'] >= '2019-01-31')].copy().reset_index(drop=True)

# =============================================================================
# profile = ProfileReport(train_test, title="Profiling Report")
# profile.to_file("train_test_EDA.html")
# =============================================================================
print(full.columns)


full.to_csv('full_dataset.csv', index=False)
full.iloc[:,1:] = full.iloc[:,1:].apply(lambda x: (x-x.mean())/ x.std(), axis=0)


# =============================================================================
# =============================================================================
# plt.plot('Date','CPI',data=full)
# plt.plot('Date','GDP',data=full)
plt.plot('Date','PCE',data=full)
# plt.plot('Date','Inflation',data=full)
# =============================================================================
plt.plot('Date','WasteRecycled',data=full)
plt.plot('Date','WasteCombusted',data=full)
plt.plot('Date','WasteLandfilled',data=full)
plt.plot('Date','WasteGenerated',data=full, color='black')
plt.legend(loc='upper left')
# =============================================================================

full.to_csv('Normalized Full data set.csv', index=False)
train_test.to_csv('Train_Test data set.csv', index=False)
validate.to_csv('validation data set.csv', index=False)
