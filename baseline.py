# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:56:14 2017

@author: qiaosj
"""

trainfile="./evaluation_public.tsv"
with(open(trainfile)) as f:
    lines = [line.strip().split('\t') for line in f.readlines()]


import pandas as pd  

df=pd.DataFrame()

ids=[]
tcount=[]
r=[]

for line in lines:
    ids.append(line[0])
    if len(line)==2:
        line.append('')
#    label.append(line[3])
    dtl=line[2].replace(' ','').replace('，',' 。').replace('、',' 。').split('。')
    pool=[]
    t=0
    length=0
    for i in dtl:
        if len(i)<20:
            continue
        length+=1
        if i not in pool:
            pool.append(i)
        else:
#            break
            t+=1
    if length==0:
        r.append(0)
    else:
        r.append(1.*t/length)
    tcount.append(t)
  
        
df['id']=ids
df['space']=tcount
df['label']='NEGATIVE'
df['label'][(df['space']==0)]='POSITIVE'


result=df[['id','label']]
result.to_csv('./test.csv',index=False,header=False)