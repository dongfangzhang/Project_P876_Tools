# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:45:42 2020

@author: zhang_d2
"""

import PyPDF2
import pdfplumber
import pandas as pd
import re
#%%  pyPDF2
path=r'C:\Users\zhang_d2\Desktop\BOM-P.876-M50-MA ALT1-20200603.pdf'
mypdf=open(path,mode='rb')
pdf_document=PyPDF2.PdfFileReader(mypdf)
#%%  pdfplumber
path=r'C:\Users\zhang_d2\Desktop\BOM-P.876-M50-MA ALT1-20200605.pdf'
with pdfplumber.open(path) as pdf:
    content=' '
    #len(pdf.pages)  # pages of pdf
    for i in range(len(pdf.pages)):
        #pdf.pages[i] #read the i+1 page
        page=pdf.pages[i]
        #pages.extract_text() #read the text and the next step is to delete the pages number
        page_content='\n'.join(page.extract_text().split('\n')[:-1])
        content=content+page_content
    print(content)
#%%
#pdf_document.numPages

#%%
#first_page=pdf_document.getPage(0)

#%%
#print(first_page.extractText())
#mypdf.close
#%%
#path=r'C:\Users\zhang_d2\Desktop\BOM-P.876-M50-MA ALT1-20200605.pdf'
#with pdfplumber.open(path) as pdf:
    #first_page=pdf.pages[0]
    #for table in first_page.extract_tables():
        #df=pd.DataFrame(table[1:],columns=table[0])
#%%
c=[]
c=re.split('\n\d+0 ',content)
#%%
df=[]
for i in c:
    if i[0] == 'L':
        d=re.split('\n| ',i)
        df.append(d)
        