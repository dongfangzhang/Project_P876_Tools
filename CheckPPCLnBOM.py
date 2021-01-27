# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:45:42 2020

@author: zhang_d2
"""
import pdfplumber
import pandas as pd
import re
from pandas import DataFrame
#%% 
PDFpath=r'C:\Users\zhang_d2\Desktop\P.876_IBCM10.pdf'
Excelpath=r'C:\Users\zhang_d2\Desktop\PPCL-P.876-M50-CA-ALT2_20200703.xlsx'
#%% check name consistent
PDFName=PDFpath.split('BOM')[1]
ExcelName=Excelpath.split('PPCL')[1]
if PDFName.split('.')[1]==ExcelName.split('.')[1]:
    print('Name consistent check successful!')
else:
    print('Name not match to each other')
#%%  pdfplumber
with pdfplumber.open(PDFpath) as pdf:
    PDFInit=' '    #len(pdf.pages)  # pages of pdf
    for i in range(len(pdf.pages)):
        page=pdf.pages[i]#read the i+1 page
        page_content='\n'.join(page.extract_text().split('\n')[:-1]) #read the text and the next step is to delete the pages number
        PDFInit=PDFInit+page_content
#%%
c=[]
PDFSplit=re.split('\n\d+0 ',PDFInit)
dflist=[]
for i in PDFSplit:
    if i[0] == 'L':
        piece=re.split('\n| ',i)
        dflist.append(piece)
PDFdf=DataFrame(dflist)
#%%
PDFContent=PDFdf.loc[:,[1,2]] 
PDFdict=dict(zip(PDFContent[2],PDFContent[1]))

#%%  Excel Reader
ExInit=pd.read_excel(Excelpath,header=1)
#%%
ExInit.to_csv(r'C:\Users\zhang_d2\Desktop\TransferCa.xlsx',encoding='utf-8')
CSVInit=pd.read_csv(r'C:\Users\zhang_d2\Desktop\TransferCa.xlsx',header=1,index_col=0)
#%%
CSVInit.fillna(" ",inplace = True)
#%%
n_row=0
CSVlist=[]
CSVPriceCheck=[]
for i in CSVInit['ICT']:
    n_row += 1
    if i == 'L' and CSVInit['数量\nAmount'][n_row] != ' ':  
        CSVlist.append([str(int(CSVInit['数量\nAmount'][n_row])),str(int(CSVInit['物料号/\nSAP number'][n_row]))])
        #CSVPriceCheck.append([str(int(CSVInit['数量\nAmount'][n_row])),str(int(CSVInit['物料号/\nSAP number'][n_row])),str(int(CSVInit['预估单价\nEstimate unit price'][n_row])),str(int(CSVInit['预算总价\nAmount Price'][n_row]))])
#%%
ExContent=DataFrame(CSVlist)   
Exdict=dict(zip(ExContent[1],ExContent[0]))  

#%%  compare Excel and PDF
badflag=0
for key in PDFdict:
    if key in Exdict:
        if PDFdict[key]!=Exdict[key]:
            badflag=1
            print(key)       
if badflag==0:
    print('Quantity and Sap Number consistent check successful!')
else:
    print('Quantity and Sap Number consistent check fail!!!')
    









