# -*- coding: utf-8 -*-

''' 地图技能 '''

import sys
import os
import urllib
import urllib2
import httplib
import requests
import json
import demjson
sys.path.append('/home/pi/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts

def start(tok):
    
    m = map()
    m.main(tok)
    
class map(object):
    
    def __init__(self):
      
        pass
      
    def main(self, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = map()
        
        bt.tts('欢迎使用小蓝地图技能，API服务由腾讯地图提供', tok)
        speaker.speak()
        bt.tts('支持查找路线，附近有什么服务等，如：从这里到美丽公园怎么走？，又比如：美丽公园附近有什么吃的？', tok)
        speaker.speak()
        bt.tts('请说出您的需要', tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        text = bs.stt('./voice.wav', tok)
        command = m.choose_command(text, tok)
        
    def choose_command(self, text, tok):
        
        if 
