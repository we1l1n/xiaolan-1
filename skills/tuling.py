# -*- coding: utf-8 -*-
'''图灵'''
import sys
import os
import requests
import json
import urllib2
import demjson
sys.path.append('/home/pi/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
from recorder import recorder
import setting

def start(text, tok):
  
    main(text, tok)
    
def main(text, tok):
    
    setting = setting.setting()
    ak = setting['tuling']['key']
    ui = setting['tuling']['user_id']
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    dataf = {
	      "reqType":0,
              "perception": {
                  "inputText": {
                      "text": text
                  },
              },
              "userInfo": {
                  "apiKey": ak,
                  "userId": ui
              }
           }
    data = json.dumps(dataf)
    talkback = requests.post(url, data=data)
    talkback_data = talkback.json()
    text = talkback_data["results"][-1]["values"]["text"]
    saytext = text.encode('utf-8','strict')
    bt = baidu_tts()
    bt.tts(saytext, tok)
    speaker.speak()
    
