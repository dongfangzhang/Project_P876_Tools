# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:13:16 2020

@author: zhang_d2
"""
try:
     import Tkinter as Tk ## notice capitalized T in Tkinter
except ImportError:
    import tkinter as Tk ## notice lowercase 't' in tkinter here...
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from copy import deepcopy
from CylDict import CylDictFinal
import sys
#%%
class GenerateCyl(object):
    def __init__(self, filelocation, cyl_list, header=None):
        self.file = filelocation
        self.tree = ET.parse( self.file)
        self.root = self.tree.getroot()
        self.cyl_list = cyl_list     
        self.header = header  if header != None else 'new_cyl'
        
    def __call__(self):
        programs_root = self.root.find('.//Programs')  
        rll_root = programs_root.find('.//RLLContent')  
#        for a in rll_root:
#            print(a.attrib)
        if not 'Number' in rll_root[-1].attrib.keys():
            sys.exit(-1)
        # get last rung number
        rung_last = int(rll_root[-1].attrib['Number'])   
        # copy last rung
        i=0
        for cyl_desc,cyl_name in  self.cyl_list:
            #find cyl name
            pattern = ('CylinderIBC(',')')
            start = rll_root[-1][1].text.find(pattern[0]) + len(pattern[0])
            end = rll_root[-1][1].text.find(pattern[1],start)
            pattern = rll_root[-1][1].text[start:end]
            #replace rungs in the pattern files
            if i <= rung_last:              
                multistring = rll_root[i][0].text.split('\n')                
                multistring[2] = cyl_desc
                rll_root[i][0].text = '\n'.join(multistring)
                rll_root[i][1].text=rll_root[i][1].text.replace(pattern,cyl_name)               
            elif i> rung_last:
                # increase rung number
                rung_new = deepcopy(rll_root[-1])
                rung_last += 1
                # description update
                rung_new.attrib['Number'] = str(rung_last)
                multistring = rung_new[0].text.split('\n')
                multistring[2] = cyl_desc
                rung_new[0].text = '\n'.join(multistring)
                # name update
                rung_new[1].text = rung_new[1].text.replace(pattern,cyl_name)
                # add to etree
                rll_root.append(rung_new)
            i+=1
        self.tree.write(f'{self.header}.L5X',xml_declaration=True,encoding="UTF-8")
#%%
if __name__ == "__main__":
    # cylinder definition as list of tuple
    ModuleCylsplit =[{} for i in range(8)]
    cyl_list=[]
    print('start')
    tempa=[]
    tempb=[]
    n=0
    # Get File name from user
    root_tk = Tk.Tk()
    root_tk.withdraw()
    filelocation= askopenfilename() 
    root_tk.quit()
    # check file type
    if filelocation[-3:] != 'L5X':
        sys.exit('bastard!')
    #Cyl_list.append[]
    for key in CylDictFinal:
        #ModuleDict.update({((key[0]),(key[1])):CylDictFinal[key]})
        a,b,c=key
        if tempa=='':
            tempa=a
            tempb=b
            ModuleCylsplit[int(tempa[1])].update({(b):{c:CylDictFinal[key]}})
        elif tempa==a:
            if b not in ModuleCylsplit[int(tempa[1])].keys():
                ModuleCylsplit[int(tempa[1])].update({(b):{c:CylDictFinal[key]}})
            else:
                ModuleCylsplit[int(tempa[1])][b].update({c:CylDictFinal[key]})      
        else:
            tempa=a
            ModuleCylsplit[int(tempa[1])].update({(b):{c:CylDictFinal[key]}}) 
    #get the module dictionary
    for Module in ModuleCylsplit: 
        #get the Station dictionary
        for key in Module:
            cyl_list=[]
            #change the sequence for the station dictionary
            ModulekeyOrder=sorted(Module[key])
            #get list for one station 
            for key2 in ModulekeyOrder:
                cyl_list.append(Module[key][key2])
            CylGen = GenerateCyl(filelocation,cyl_list,'Module0'+str(ModuleCylsplit.index(Module))+'0St'+key)
            CylGen()   
