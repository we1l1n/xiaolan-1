# coding=utf-8
'''快递查询技能'''

import sys
import os
import requests
import json
import base64
import hashlib
import urllib
from urllib import parse
import re
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
    try:
        text.replace('零', 0)
        text.replace('一', 1)
        text.replace('二', 2)
        text.replace('三', 3)
        text.replace('四', 4)
        text.replace('五', 5)
        text.replace('六', 6)
        text.replace('七', 7)
        text.replace('八', 8)
        text.replace('九', 9)
    except TypeError:
        return text
    except KeyError:
        return text
    else:
        return text
        
        
        
def main(tok):
    
    bt = baidu_tts()
    yt = youdao_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r = recorder()
    
    selfset = setting.setting()
    hash = hashlib.md5()
    
    bt.tts('您好，请说出您的快递单号和快递公司', tok)
    speaker.speak()
    speaker.ding()
    r.exrecord()
    speaker.dong()
    idss = bs.stt('./voice.wav', tok)
    ids = number_choose(ids, tok)
    
    requestData = {
                   'OrderCode': ids,
                   'ShipperCode': service,
                   'LogisticCode':'12345678'
    }

    data = {
        'EBusinessID': '1349773',
        'RequestType': '1002',
        'RequestData': parse.quote(str(requestData)),
        'DataType': '2',
    }
    strings = str(requestData) + '1f0c5c35-67a8-495f-b3ab-a7fc534a826f'
    string = strings.encode(encoding='UTF-8', errors='strict')
    hashs.update(string)
    s = hashs.hexdigest().encode('utf-8')
    y = base64.b64encode(s)
    z = str(y, 'utf-8')
    data['DataSign'] = parse.quote(z, 'utf-8')
    r = requests.post('http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx',
                      data=data)
    json = r.json()
    try:
        bt.tts(json['Traces'][-1]['AcceptStation'], tok)
        speaker.speak()
    except KeyError:
        bt.tts('对不起，包裹信息查询失败', tok)
        speaker.speak()
        
    
    
    
    
    
    
