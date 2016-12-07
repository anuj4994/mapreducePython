#!/usr/bin/env python

"""
Created on Mon Dec  5 16:05:14 2016

@author: Anuj Shah
"""

import sys

words=[]
temp_list=[]
for line in sys.stdin:
       line = line.strip()
       count = line.count(',')
       if (len(words)>27) and words[0] != "DATE":
             words = words[-5:]
             for word in words:
                   if len(word)>0:
                       print "%s\t%s"%(word, 1)
words=[]
temp_list=[]
