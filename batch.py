import json,os
import requests, urllib.parse,subprocess,time
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
from webhooks import webhook
import logging



logger = logging.getLogger('automatorLogger') 

def batch1():
    logger.warn('What do you want to do')

def batch2():
    logger.warn('something else?')

class batchprocess:
    def __init__(self):
        pass
    def startAllBatch(self):
        logger.warn('do you want to automation?')
    def startDoSomething(self,batchList):
        logger.warn('fun job!!')