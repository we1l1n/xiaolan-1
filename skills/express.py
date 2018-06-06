# coding=utf-8
'''快递查询技能'''

import sys
import os
import requests
import json
import demjson
import base64
import hashlib
import httplib
import urllib
import urllib2
sys.path.append('/home/pi/xiaolan/')
import speaker
from tts import baidu_tts
from tts import youdao_tts
from stt import baidu_stt
from recorder import recorder
import setting

def start(tok):

    main(tok)
    
def number_choose(text, tok):
    
    bt = baidu_tts()
    base = 0
    try:
        for texts in text:
            if text[base] == '一' or text[base] == '1':
                text[base] = 1
            elif text[base] == '二' or text[base] == '2':
                text[base] = 2
            elif text[base] == '三' or text[base] == '3':
                text[base] = 3
            elif text[base] == '四' or text[base] == '4':
                text[base] = 4
            elif text[base] == '五' or text[base] == '5':
                text[base] = 5
            elif text[base] == '六' or text[base] == '6':
                text[base] = 6
            elif text[base] == '七' or text[base] == '7':
                text[base] = 7
            elif text[base] == '八' or text[base] == '8':
                text[base] = 8
            elif text[base] == '九' or text[base] == '9':
                text[base] = 9
            elif text[base] == '零' or text[base] == '0':
                text[base] = 0
            base = base + 1
    except KeyError:
        return str(text)
    except TypeError:
        bt.tts('对不起，快递单号读取错误', tok)
        speaker.speak()
    else:
        return str(text)
        
    
def main(tok):
    
    bt = baidu_tts()
    yt = youdao_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r = recorder()
    
    selfset = setting.setting()
    hash = hashlib.md5()
    
    bt.tts('您好，请说出您要查询的快递单号', tok)
    speaker.speak()
    speaker.ding()
    r.exrecord()
    speaker.dong()
    
    requestData = {
                   'OrderCode': number_choose(bs.stt('./voice.wav', tok), tok),
                   'ShipperCode':'YTO',
                   'LogisticCode':'12345678'
                  }
    
    data = {
            'EBusinessID': selfset['express']['EBusinessID'],
            'RequestType': '1002',
            'RequestData': urllib.urlencode(str(requestData)) ,
            'DataType': '2',
           }
    hash.update(str(requestData) + selfset['express']['key'], encoding='utf-8')
    data['DataSign'] = urllib.urlencode(base64.b64encode(hash.hexdigest()))
    json = requests.post('http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx',
                         data=data,
                         headers='application/x-www-form-urlencoded;charset=utf-8')
    try:
        bt.tts(json['Traces'][-1]['AcceptStation'], tok)
        speaker.speak()
    except KeyError:
        bt.tts('对不起，包裹信息查询失败', tok)
        speaker.speak()
        
        
    
    
    
    
    
    
