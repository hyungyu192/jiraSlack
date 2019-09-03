#-*- coding:utf-8 -*-

import json,os
import requests, urllib.parse,subprocess,time
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
from webhooks import webhook
import logging



logger = logging.getLogger('automatorLogger') 

headers = {'content-encoding': 'gzip','content-type':'application/json'}


url = ''

resp  =  requests.get(url,headers=headers) 
if resp.status_code >= 200:
    if resp.status_code < 300:
        json_data = json.loads(resp.text)
        print(json.dumps(json_data,sort_keys = True, indent = 4))
    else:
        print('!!!error : ' + str(resp.status_code))
        print(resp)
    