# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:59:55 2020

@author: zhang_d2
"""

import pandas as pd
import re
from pandas import DataFrame
import os
#%%import
Excelpath=r'C:\Users\zhang_d2\Desktop\P.876_IBC_20200713.xlsx'
#%% Init and fill Nan
ExInit=pd.read_excel(Excelpath)
ExInit.fillna(" ",inplace = True)
#%% get FunctionText content;to replace some required content; use " " to split
TagSplit=[]
Tagright=[]
TagList=ExInit.Functiontext
for a in TagList:
    a=a.replace('-','_').replace('.','_').replace(':','_').replace('(','_').replace(')','')#.replace(' above','').replace('below','')
    a=a.replace('stroke','cyl')
    a=a.replace('horizontal','hori').replace('vertical','vert')
    a=a.replace('presence','pos').replace('position','pos')
    a=a.replace(' advanced','adv').replace(' extended','ext').replace(' extend','ext').replace(' retracted','ret').replace(' retract','ret')
    a=a.replace('rotating','rot').replace('pick and place','PnP')
    a=a.replace('nning','n').replace('ing','')
    b=re.split(' ',a)
    TagSplit.append(b)
    #Tagright.append(a)
#%% get first alphabet Uppercas; Combine Capitalized content
TagUp=[]
for a in TagSplit:
    Index=[]
    for b in a:
        if b!='':
            if re.search('[a-z]',b[0]):
                b=str.capitalize(b)
            #print(b)
        Index.append(b)
    TagUp.append(Index)
TagCom=[]
for a in TagUp:
    TagCom.append(''.join(a))
#%%  splited by "++"; Take station and Module number out
PosSplit=[]
PosModule=[]
PosList=ExInit.SymbolicAutomatic
for a in PosList:
    b=a.split("++")
    #b=re.split('++',a)
    PosSplit.append(b)
PosSt=[]
for a in PosSplit:
    if a[0][0]=="=":
        PosSt.append(a[0][6:9])
        PosModule.append(a[0][2:5])
    else:
        PosSt.append('')
        PosModule.append('')
#%% Take cylinder number out
PosCynNum=[]
for a in PosSplit:
    if len(a)==2:
        if re.search('(AA\d+-QM\d+-MB\d+)',a[1]) :
            b=re.search('(QM\d+-MB\d+)',a[1]).group()
            if b[0]=='Q':
                b=b.replace('Q','M')
            PosCynNum.append(b)
        else:
            PosCynNum.append('')
    else:
        PosCynNum.append('')
#%%Combine the cylinder and Station
ResNameDes=[]
ResModuleSt=[]
ResName=[]
n=0
for a in PosModule:
    if a!='' and PosSt[n]!='' and PosCynNum[n]!='':
        if re.search('[0-9]',PosSt[n][0]):
            ResNameDes.append((TagCom[n],TagList[n]))
            ResModuleSt.append((PosModule[n],PosSt[n],PosCynNum[n]))
        else:
            ResName.append('')
            ResNameDes.append('')
            ResModuleSt.append('')
    else:
        ResName.append('')
        ResNameDes.append('')  
        ResModuleSt.append('')
    n+=1 
#%%
    
    
def Filter():
    final_dict = {}
#    def _(str1,str2):
#        str_size = len(str1) if len(str1) < len(str2) else len(str2)
#        for i in range(str_size):
#            if str1[i]==str2[i]:
#                pass
#            else:
#                break
#        return str1[:i]
    def _(str1,str2):
        str_size = len(str1) if len(str1) < len(str2) else len(str2)
        for i in range(str_size):
            if str1[i]==str2[i]:
                pass
            else:
                break
        return str1[:i]    
    def inner(key,Cyldict):
        nonlocal final_dict
        m,s,c = key
        c = c.split('-')
        if (m,s,c[0]) not in final_dict.keys():
            final_dict.update({(m,s,c[0]):{c[1]:Cyldict[key][1]}})
            final_dict[(m,s,c[0])].update({'tmp':Cyldict[key][0]})
            final_dict[(m,s,c[0])].update({'id':c[0]})
            final_dict[(m,s,c[0])].update({'Module':m})
            final_dict[(m,s,c[0])].update({'Station':s})
            final_dict[(m,s,c[0])].update({'Name':(c[0]+'_'+Cyldict[key][0])})
        else:
            final_dict[(m,s,c[0])].update({c[1]:Cyldict[key][1]})
            #final_dict[(m,s,c[0])].update({'Name':_(Cyldict[key][0], final_dict[(m,s,c[0])]['tmp'])})
            final_dict[(m,s,c[0])].pop('tmp')
        return final_dict
    return inner
#%%
Cyldict= dict(zip(ResModuleSt,ResNameDes))
fill=Filter()
tmp = {}
for key in Cyldict.keys():
    if len(key) <1:
        pass
    else:
        tmp = fill(key,Cyldict)
    
CylDictFinal = {}
for items in tmp.items():
    if 'MB1' in items[1].keys() and 'MB2' in items[1].keys():
        CylDictFinal.update({items[0]:(items[1]['id'] + ':'+ items[1]['MB1'] + ' / ' + items[1]['MB2'],items[1]['Name'])})
    elif 'MB1' in items[1].keys() :
        CylDictFinal.update({items[0]:(items[1]['id'] + ':'+ items[1]['MB1'] ,items[1]['Name'])})  
    elif 'MB2' in items[1].keys() :
        CylDictFinal.update({items[0]:(items[1]['id'] + ':'+ items[1]['MB2'] ,items[1]['Name'])}) 
      