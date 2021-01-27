# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:30:43 2020

@author: zhang_d2
"""

import pandas as pd
from pandas import DataFrame

ca=pd.read_excel(r'C:\Users\zhang_d2\Desktop\PPCL-P.876-M50-CA-ALT2_20200703.xlsx',header=1)
ma=pd.read_excel(r'C:\Users\zhang_d2\Desktop\PPCL-P.876-M50-MA-ALT2_20200703.xlsx',header=1)

#%%
ca.to_csv(r'C:\Users\zhang_d2\Desktop\TransferCa.xlsx',encoding='utf-8')
caTrans=pd.read_csv(r'C:\Users\zhang_d2\Desktop\TransferCa.xlsx',header=1,index_col=0)

ma.to_csv(r'C:\Users\zhang_d2\Desktop\TransferMa.xlsx',encoding='utf-8')
maTrans=pd.read_csv(r'C:\Users\zhang_d2\Desktop\TransferMa.xlsx',header=1,index_col=0)
#%%
caTrans.fillna(" ",inplace = True)
maTrans.fillna(" ",inplace = True)
#%%
caTrans.drop([1])

maTrans.drop([1])
#%%
n_row=0
for i in caTrans['数量\nAmount']: 
    if i == ' ':
        break
    else:
        #int(i)
        n_row += 1
casap=caTrans.loc[0:n_row]
#%%
n_row=0
for i in maTrans['数量\nAmount']: 
    if i == ' ':
        break
    else:
        #int(i)
        n_row += 1
#%%
masap=maTrans.loc[0:n_row]
#%%
CaExcel=DataFrame(casap,columns=['ICT','物料号/\nSAP number','工位\nStation','数量\nAmount'])
CaExcel.to_excel(r'C:\Users\zhang_d2\Desktop\resultCa.xlsx',encoding='gbk')   

MaExcel=DataFrame(maTrans,columns=['ICT','物料号/\nSAP number','工位\nStation','数量\nAmount'])
MaExcel.to_excel(r'C:\Users\zhang_d2\Desktop\resultMa.xlsx',encoding='gbk') 
#%%
