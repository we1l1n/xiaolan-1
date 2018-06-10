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
import setting

def start(tok):
    
    m = map()
    m.main(tok)
    
class maps(object):
    
    def __init__(self):
      
        pass
    
    def near(self, place, tok):
        
        selfset = setting.setting()
        citys = requests.get('http://apis.map.qq.com/ws/location/v1/ip')
        nears = requests.get('http://apis.map.qq.com/ws/place/v1/search?' + 'boundary=region(' + city + ',0)&keyword=' + place + '&page_size=5&page_index=1&orderby=_distance&key=' + setting['map']['key'])
        
        
    def go_way(self, place_f, place_s, tok):
        
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
        
        m = map()
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        if '从' in text and '怎么去' in text:
            m.go_way(text[0:-7], text[-8:-3], tok)
        elif '从' in text and '怎么走' in text:
            m.go_way(text[0:-7], text[-8:-3], tok)
        elif '附近' in text:
            m.near(text[0:5], tok)
        else:
            bt.tts('对不起，暂时不支持该功能', tok)
            speaker.speak()
