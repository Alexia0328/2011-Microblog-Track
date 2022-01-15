#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import nltk
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
wordIndexing = {}
wordweightindex={}
totaldoc = 0
def calculatelength(array):
    result=0
    for i in array:
        result=result+i**2
    result=math.sqrt(result)
    return result
def Preprocessing(path):
    file=open(path,encoding='utf-8')
    line=file.readline()
    stopWords=set(stopwords.words('english'))
    while line:
        results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
        line = re.sub(results, '', line)
        words=word_tokenize(line)
        wordweight=[]
        
        Index=0
        for w in words:
            if (w not in stopWords)and(w.isalpha()):
                if(w not in wordIndexing): 
                    wordIndexing[w]=[[words[0],Index]]
                    wordweight.append(1)
                    Index=Index+1
                else:
                    before=wordIndexing[w]
                    IntheIndex=False
                    
                    for [i,j] in before:
                        if(i==words[0]):
                            IntheIndex=True
                            wordweight[j]=wordweight[j]+1
                    if not IntheIndex:
                        before.append([words[0],Index])
                        wordweight.append(1)
                        Index=Index+1
        if(len(wordweight)==0):
            value=0
        else:
            value=max(wordweight)                 
        wordweightindex[words[0]]=[value,wordweight]   
        global totaldoc 
        totaldoc = totaldoc+1
        line = file.readline()
    
def calculateweight():
    for i in wordIndexing:
        j=wordIndexing[i]
        idf=math.log2(totaldoc/len(j))
        for [z,s] in j:
            [t,m]=wordweightindex[z]
            m[s]=((0.5 + 0.5 * (m[s]/t)) * idf)
            
def calculatequery(query):
    words=word_tokenize(query)
    stopWords=set(stopwords.words('english'))
    Index=0
    queryarray=[]
    appeartime=[]
    queryresult=[]

    for w in words:
        if (w not in stopWords)and(w.isalpha()):
            if(w not in wordIndexing): 
                continue #idf=0 ignore directly
            else:
                if(w not in queryarray):
                    queryarray.append(w)
                    appeartime.append(1)
                else:
                    appeartime[queryarray.index(w)]=appeartime[queryarray.index(w)]+1
    a=max(appeartime)
    z=0

    for i in queryarray:
        j=wordIndexing[i]
        idf=math.log2(totaldoc/len(j))
        queryresult.append((0.5 + 0.5 * (appeartime[z]/a)) * idf)
        z=z+1
    querylength=calculatelength(queryresult)
    return [queryarray,queryresult,querylength]
def ranking(query):
    finalresult={}
    index=0
    [a,b,c]=calculatequery(query)
    for i in a:
        j=wordIndexing[i]
        for [z,s] in j:
                [t,m]=wordweightindex[z]
                if z in finalresult:
                    finalresult[z]=finalresult[z]+m[s]*b[index]
                else:
                    finalresult[z]=m[s]*b[index]
        index=index+1
    for i in finalresult:
        j=finalresult[i]
        [t,m]=wordweightindex[i]
        
        finalresult[i]=j/(calculatelength(m)*c)
    ranked=sorted(finalresult.items(), key=lambda x: x[1], reverse=True)
    return ranked
def outputresult(filepath):
    f = open(filepath)
    line=f.readline()
    queryarray=[]
    while line:
        if ('<top>' in line):        
            thisquert=[]
            line = f.readline()
            line=line.strip('<num> Number: MB')
            line=line.strip(' </num>\n')
            thisquert.append(line)
            line = f.readline()
            line=line.strip('<title>')
            line=line.strip('</title>\n')
            thisquert.append(line)
            line = f.readline()
            line = f.readline()
            line=line.strip('<querytweettime>')
            line=line.strip('</querytweettime>\n')
            thisquert.append(line)
            queryarray.append(thisquert)
        line = f.readline()
    with  open('output.txt','w') as fa:
            for i in range(len(queryarray)):
                result=list(ranking(queryarray[i][1]))
                if (len(result)<1000):
                    length=len(result)
                else:
                    length=1000
                for index in range(length):
                    fa.write(str(queryarray[i][0])+" Q0 ")
                    fa.write(str(queryarray[i][2])+" ")
                    fa.write(str(index+1)+" ")
                    fa.write(str(result[index][1]))
                    fa.write(" query")
                    fa.write("\n")
            fa.close()
            
 

         
   
                
            
    
    
Preprocessing("Trec_microblog11.txt")
calculateweight()
outputresult('topics_MB1-49.txt')

