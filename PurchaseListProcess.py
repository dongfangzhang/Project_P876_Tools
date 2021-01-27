# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import pandas as pd
from pandas import DataFrame
from decimal import Decimal

Price=pd.read_excel(r'C:\Users\zhang_d2\Desktop\采购件价格表.xlsx')
List=pd.read_excel(r'C:\Users\zhang_d2\Desktop\2200_zhang_d2_P.876_IBC_2020-04-29_13-01-40_complete.xlsx')
List2=pd.read_excel(r'C:\Users\zhang_d2\Desktop\ERP柜内.xlsx')

#%%
PriceDict=dict(zip(Price['Material'],Price['net price']))
#STdic= dict(zip(dic['DE'],dic['En']))
#round(PriceDict())

#%%
#List1=List.drop([0])
#%%
result1=[]
noPrice1=[]
i=0
for a in List['Partnumber']:
    try:
        result1.append(PriceDict[a])
        i+=1
    except KeyError:
        result1.append(' ')
        noPrice1.append(a)
        i+=1
    continue


#%%
result2=[]
noPrice2=[]
i=0
for a in List2['Partnumber']:
    try:
        result2.append(PriceDict[a])
        i+=1
    except KeyError:
        result2.append(' ')
        noPrice2.append(a)
        i+=1
    continue
#%%
#CnTranslated=pd.read_excel(r'C:\Users\zhang_d2\Desktop\P&G AIS translation\CnTranslated.xlsx') 
"""
df.fillna("NA",inplace = True)
if df.isna().sum().sum() == 0:
    print("df Sanity test past")

Translated.fillna("NA",inplace = True)
if Translated.isna().sum().sum() == 0:
    print("Translated Sanity test past")

#content=[['','','','','','','']for i in range(10000)]
#number=['']*10000
#errorname=['']*10000
EnCombined=['' for i in range(9000)]
CnCombined=['' for i in range(9000)]
n=0
for a in df['de-DE']:
    try:
        CNcontent=a.split(" - ")
        ENcontent=a.split(" - ")
        
        CNcontent[1]=df['StationName'][n]
        ENcontent[1]=df['StationName'][n]
        CNcontent[2]=Translated['zh-CN'][n]
        ENcontent[2]=Translated['en-GB'][n]
        CnCombined[n]=' - '.join(CNcontent[0:3])
        EnCombined[n]=' - '.join(ENcontent[0:3])
        n+=1
    except IndexError:
        if a == 'Reserve':
            CnCombined[n]=df['de-DE'][n]
            EnCombined[n]=df['de-DE'][n]
        else:
            CnCombined[n]=Translated['zh-CN'][n]
            EnCombined[n]=Translated['en-GB'][n]
        n+=1
    continue
"""
#CnCombined=DataFrame(CnCombined,columns=['zh-CN'])
#CnCombined.to_excel(r'C:\Users\zhang_d2\Desktop\First time translate\CnCombined.xlsx',encoding='gbk')

#EnCombined=DataFrame(EnCombined,columns=['en-GB'])
#EnCombined.to_excel(r'C:\Users\zhang_d2\Desktop\First time translate\EnCombined.xlsx',encoding='gbk')



