#!/usr/bin/python
# coding=UTF-8
# pre-req: extract text information from 
#          https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7
#          save as temp.txt
# usage: ./alvin.py temp.txt

from __future__ import print_function
import os
import re

with open(os.sys.argv[1], 'r') as alvin:
    lines=alvin.readlines()

for line in lines:
    if line != '\r\n':
        temp=line.replace('（','(').replace('）',')')
        index1=temp.find('(')
        index2=temp.find(')')
        if index1 != -1 and index2 != -1:
            line=temp.replace(temp[index1:index2+1], '')
        temp=line
        index1=temp.find('(')
        index2=temp.find(')')
        if index1 != -1 and index2 != -1:
            line=temp.replace(temp[index1:index2+1], '')

        linelist=line.rstrip('\r\n').replace(' ：','：').replace('： ','：').replace('：',' ').replace('（',' ').split(' ')
        ll=len(linelist)

        if ll not in [8,9,10,12,13,14]:
            pass
        else:
            c=[]
            for i in range(1,ll,2):
                if linelist[i].find(')') == -1 and linelist[i].find('('):
                    c.append(linelist[i])
            print(' '.join(c))
