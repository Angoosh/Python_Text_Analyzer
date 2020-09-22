# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:20:46 2020

@author: Carter
"""

import csv

FILE = "text.txt" #path to text file 

dictionary = []
counter = []

def WordCounter(text):
    words = text.split(" ")
    for i in words:
        i = i.strip("\n.;,")
        if i in dictionary:
            ind = dictionary.index(i)
            counter[ind] += 1
        else:
            dictionary.append(i)
            counter.append(1)
        
with open(FILE, "r", encoding="utf-8") as t:
    for line in t:
        WordCounter(line)
    output = [dictionary for _,dictionary in sorted(zip(counter,dictionary))]
    output.reverse()
    counter.sort()
    counter.reverse()
    t.close()
    
for i in range(0,100):#len(dictionary)-1
    print(str(counter[i])+","+str(dictionary[i]))

    