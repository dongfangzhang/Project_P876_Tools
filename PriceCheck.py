# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:10:55 2020

@author: zhang_d2
"""
import pandas as pd
#from pandas import DataFrame
#%% content transfer
Excelpath=r'C:\Users\zhang_d2\Desktop\PPCL-P.876-M50-CA-ALT2_20200703.xlsx'
ExInit=pd.read_excel(Excelpath,header=1)
ExInit.to_csv(r'C:\Users\zhang_d2\Desktop\TransferCa.xlsx',encoding='utf-8')
CSVInit=pd.read_csv(r'C:\Users\zhang_d2\Desktop\TransferCa.xlsx',header=1,index_col=0)
CSVInit.fillna(" ",inplace = True)
#%% check the price with the price table; if not same price with the price table or not have price in the price table, need to show the messge
Price=pd.read_excel(r'C:\Users\zhang_d2\Desktop\采购件价格表.xlsx')
PriceDict=dict(zip(Price['Material'],Price['net price']))
#%%
result=[]
noPrice=[]
for a in CSVInit['物料号/\nSAP number']:
    try:
        result.append(PriceDict[a])
        noPrice.append('')
    except KeyError:
        result.append('')
        noPrice.append(a)
    continue