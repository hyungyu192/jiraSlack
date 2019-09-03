
import json,os
import requests, urllib.parse,subprocess,time
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
from webhooks import webhook
import logging
from jiraapi import jiraApiPost

logger = logging.getLogger('automatorLogger') 


headers = {'content-type':'application/x-www-form-urlencoded','Accept':'application/json, text/javascript, */*; q=0.01',
'Referer':'https://recommend.wisereport.co.kr/v1/Home/RecommendSummary/naver','Sec-Fetch-Mode':'cors','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.71 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'}

url = 'https://recommend.wisereport.co.kr/v1/Home/TopRecommend'
data = 'proc=3&dt=20190903'

resp = requests.post(url,headers=headers, data=data) #한글빼고 잘댐

dumpData = dump.dump_all(resp) # 없어도 됨 그치만 디버깅용으로 써놓음
print(dumpData.decode('utf-8'))

texts=''

if resp.status_code >= 200:
    if resp.status_code < 300:
        logger.debug('status : ' + str(resp.status_code))
        try:
            json_data = json.loads(resp.text)
            for data in json_data:
                texts +="|"+data['INV_NM']+"|"+data["CMP_CD"]+"|"+data["CMP_NM_KOR"]+"|"+data["REASON_IN"]+"|\n"
            #print(json.dumps(json_data,sort_keys = True, indent = 4))
            jiraApiPost(texts)
            webhook(texts,None,None)
            # return(json_data['key'])
        except:
            logger.debug('Request error')
    else:
        logger.error(resp.text)
