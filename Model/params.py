# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:30:19 2024

@author: java
"""

import pandas as pd

# Quarterly
fileGDP = pd.read_csv('Inputs/GDP.csv')

# Monthly
fileRecession = pd.read_csv('Inputs/USREC.csv', names=['Date', 'Recession'])

fileCPI = pd.read_csv('Inputs/USACP030000CTGYM.csv', names=['Date', 'CPI'])

# Yearly
filePersonalConsumerExpenditure = pd.read_csv('Inputs/DCAFRC1A027NBEA.csv',
                                              names=['Date', 'PCE'])

fileInflation = pd.read_csv('Inputs/FPCPITOTLZGUSA.csv'
                            , names=['Date', 'Inflation'])

fileWasteGenerated = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Materials generated')

fileWasteRecycled = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Materials recycled')

fileWasteLandfilled = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Materials landfilled')

fileWasteCombusted = pd.read_excel('Inputs/Materials_Municipal_Waste_Stream_1960_2018.xlsx',
                                   sheet_name='Material combusted')