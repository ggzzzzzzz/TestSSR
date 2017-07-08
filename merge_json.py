#!/usr/bin/python
# coding=UTF-8
#
# usage: ./merge_json.py 1.json 2.json 3.json ..

import os
import json, codecs

para_count=len(os.sys.argv)

d=dict()
d['configs']=[]
serverandport=[]
if para_count > 1:
    for i in range(1,para_count,1):
        if os.path.exists(os.sys.argv[i]) and os.sys.argv[i].split('.')[-1] == 'json':
            with open(os.sys.argv[i],'r') as json_f:
                ssdict_list=json.load(json_f)['configs']
            for j in ssdict_list:
                account_alias=j['server']+j['server_port']
                if account_alias not in serverandport :
                    d['configs'].append(j)
                    serverandport.append(j['server']+j['server_port'])
            if i > 1:
                print(os.sys.argv[i]+' has been merged into '+os.sys.argv[1])
        else:
            print(os.sys.argv[i]+' not exists or is not a json file.')

    with open(os.sys.argv[1],'w') as outfile:
        json.dump(d, codecs.getwriter('utf-8')(outfile),indent=4, sort_keys=True )
else:
    print(os.sys.argv[0]+' gui-config.json 2.json 3.json')