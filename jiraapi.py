#-*- coding:utf-8 -*-

import json,os
import requests, urllib.parse,subprocess,time
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
from webhooks import webhook
import logging

logger = logging.getLogger('automatorLogger') 


headers = {'content-encoding': 'gzip','content-type':'application/json'}


post_dic = {
    'fields': {
      'project': {'key': 'AUTO'},
      'summary': 'title',
      'issuetype': {'id': '10002'},
      'description': 'description_default',
      'assignee': {'name': 'hyungyu192'},
      'priority': {'id': '2'}
       }
    }



def jiraApiPost(cont): #지라 이슈 생성 요청
    try:
        url  = 'http://192.168.90.142:8081/rest/api/2/issue'
        
        post_dic['fields']['summary']="박현규"
        # post_dic['fields']['assignee'] = {'name' : assignee}
        # post_dic['fields']['reporter'] = {'name' : assignee}
        post_dic['fields']['description']=cont

        data = json.dumps(post_dic)
        
        resp = requests.post(url,auth = HTTPBasicAuth('hyungyu192','wnsxo2030!@'),headers=headers, data=data) #한글빼고 잘댐

        if resp.status_code >= 200:
            if resp.status_code < 300:
                logger.debug('status : ' + str(resp.status_code))
                try:
                    json_data = json.loads(resp.text)
                    print(json.dumps(json_data,sort_keys = True, indent = 4))
                    return(json_data['key'])
                except:
                    logger.debug('Request of jiraApiPost')
            else:
                webhook("Jira Api Error : " + str(resp.status_code) +resp.text,None,None)
                logger.error(resp.text)
    except Exception as e:
        webhook("Jira Api Error : " + str(e) + str(resp.status_code) + " " + resp.text,None,None)
        logger.error('Error! Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e)))
        pass


def jiraAPIGet(key):
    try:
        url  = 'http://192.168.90.142:8081/rest/api/2/issue/' + key

        resp = requests.get(url,auth = HTTPBasicAuth('wulf','ajtmf3376'),headers=headers)
        
        if resp.status_code >= 200:
            if resp.status_code < 300:
                #print('status : ' + str(resp.status_code))
                try:
                    json_data = json.loads(resp.text)
                    print(json.dumps(json_data,sort_keys = True, indent = 4))
                    return(json_data)
                except:
                    logger.debug('Request of jiraAPIGet')
            else:
                webhook("Jira Api Error : " + str(resp.status_code) +resp.text,None,None)
                logger.error(resp.text)
    except Exception as e:
        webhook("Jira Api Error : " + str(e) + str(resp.status_code) + " " + resp.text,None,None)
        logger.error('Error! Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e)))
        pass


