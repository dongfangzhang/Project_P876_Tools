# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:01:28 2020

@author: zhang_d2
"""
import pandas as pd
import re
from pandas import DataFrame
#%%
Excelpath=r'C:\Users\zhang_d2\Desktop\IBCTagList (2).xlsx'
#%% Init
ExInit=pd.read_excel(Excelpath)
#%% fill Nan
ExInit.fillna(" ",inplace = True)
#%% get FunctionText content; use " " to split
TagSplit=[]
TagList=ExInit.Functiontext
for a in TagList:
    b=re.split(' ',a)
    TagSplit.append(b)
#%% get first alphabet Uppercase
TagUp=[]
for a in TagSplit:
    Index=[]
    for b in a:
        b=str.capitalize(b)
        Index.append(b)
    TagUp.append(Index)
#%% Combine content
TagCom=[]
for a in TagUp:
    TagCom.append(''.join(a))


#%%  splited by "++"
PosSplit=[]
PosList=ExInit.SymbolicAutomatic
for a in PosList:
    b=a.split("++")
    #b=re.split('++',a)
    PosSplit.append(b)
#%% Take station number out
PosSt=[]
for a in PosSplit:
    if a[0][0]=="=":
        PosSt.append(a[0][6:9])
    else:
        PosSt.append('')
#%% Take cylinder number out
PosCynBG=[]
for a in PosSplit:
    if len(a)==2:
        if re.search('(BG\d+)|(QM\d+-MB\d)',a[1]):
            b=re.search('(BG\d+)|(QM\d+-MB\d)',a[1]).group()
            if b[0]=='Q':
                c=b.replace('-','_')
            PosCynBG.append(c)
        else:
            PosCynBG.append('')
    else:
        PosCynBG.append('')
        
#%%Combine the cylinder and Station
ResCom=[]
n=0
for a in PosSt:
    if a=='':
        if PosCynBG[n]=='':
            ResCom.append(TagCom[n])
        else:
            ResCom.append(PosCynBG[n]+'_'+TagCom[n])
    else:
        if PosCynBG[n]=='':
            ResCom.append(a+'_'+TagCom[n])
        else:
            ResCom.append(a+'_'+PosCynBG[n]+'_'+TagCom[n])  
    n+=1    
#%%
#ExInit['Test']=Res
Res=DataFrame(ResCom) 
Res.to_excel(r'C:\Users\zhang_d2\Desktop\IBCTagListResult.xlsx',encoding='gbk')       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#%% Test
'''
c=[]
test2=re.finditer('(SF\d+)|(BF\d+)',test[1])
for a in test2:
    c.append(a.group())
'''