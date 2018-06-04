# -*- coding: UTF-8 -*-
import sys
import requests
import os
import json
import demjson
import random
import httplib
import urllib
import urllib2
sys.path.append('/home/pi/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import setting

def start(tok):
    main(tok)
  
def main(tok):
    
    bt = baidu_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r = recorder()
    
    appkey = selfset['ts']['appkey']
    secretkey = selfset['ts']['secretkey']
    httpClient = None
    myurl = '/api'
    q = 'good'
    
    bt.tts('请问您要翻译的是什么语言？', tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    fromLang = lang_choose(bs.stt('./voice.wav', tok), tok)
    bt.tts('请问您要翻译为什么语言？', tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    toLang = lang_choose(bs.stt('./voice.wav', tok), tok)
    bt.tts('请说出您要翻译的内容', tok)
    speaker.speak()
    speaker.ding()
    r.tsrecord()
    speaker.dong()
    tstext = bs.stt('./voice.wav', tok)
    
    salt = random.randint(1, 65536)
    sign = appKey+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
 
    try:
        httpClient = httplib.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
 
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        print response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    
    
    
  
