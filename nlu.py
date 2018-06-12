# -*- coding: utf-8 -*-

import sys
if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')
import time
import os
import json
import requests
import demjson
import base64
import hashlib
import setting
from recorder import recorder
from tts import baidu_tts
from stt import baidu_stt
sys.path.append('/home/pi/xiaolan/skills/')
import clock
import weather
import music
import mail
import tuling
import joke
import news
import camera
import snowboytrain
import express
from smarthome import hass
from maps import maps
from music import xlMusic

def get_intent(text, tok):
        
        selfset = setting.setting()
        urlf = 'http://api.xfyun.cn/v1/aiui/v1/text_semantic?text='
        appid = selfset['main_setting']['NLU']['appid']
        apikey = selfset['main_setting']['NLU']['key']
        lastmdl = 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9'
        curtimeo = int(time.time())
        curtimef = str(curtimeo)
        
        try:
                 textl = base64.b64encode(text)
        except TypeError:
                intent = 'no'
                return intent
                
        textv = 'text=' + textl
        
        csumc = apikey + curtimef + 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9' + textv

        c = hashlib.md5()
        c.update(csumc)
        checksuml = c.hexdigest()
        
        headers = {'X-Appid': appid, 'Content-type': 'application/x-www-form-urlencoded; charset=utf-8', 'X-CurTime': curtimef, 'X-Param': 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9', 'X-CheckSum': checksuml}
        url = urlf + textl
        
        r = requests.post(url,
                          headers=headers)
        json = r.json()
        try:
                intent = json['data']['service']
        except KeyError:
                return 'reintent'
        except TypeError:
                return 'reintent'
        else:
                pass
        if intent != None or intent != '':
                return intent
        else:
                do_intent(text, tok)

def do_intent(text, tok):

    sm = hass()
    m = xlMusic()
    services = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query=', 'hot': 'method=baidu.ting.song.getRecommandSongList&song_id=877578&num=12'}
    
    if text != None:
        if '闹钟' in text:
                clock.start(tok)
        elif '打开' in text:
                sm.cortol('turn_on', text[6:-1], tok)
        elif '关闭' in text:
                sm.cortol('turn_off', text[6:-1], tok)
        elif '获取' in text:
                if '传感器' in text or '温度' in text:
                        sm.sensor('sensor', text[6:-1], tok)
                elif '湿度' in text:
                        sm.sensor('sensor', text[6:-1], tok)
                else:
                        sm.sensor('switch', text[6:-1], tok)
        elif '天气' in text:
                weather.main(tok)
        elif '重新说' in text or '重复' in text:
                speaker.speak()
        elif '翻译' in text:
                ts.main(tok)
        elif '搜索' in text:
                tuling.main(text, tok)
        elif '闲聊' in text:
                tuling.main(text, tok)
        elif '怎么走' in text:
                maps.start(tok)
        elif '酒店' in text:
                tuling.main(text, tok)
        elif '旅游' in text:
                tuling.main(text, tok)
        elif '新闻' in text:
                news.start(tok)
        elif '拍照' in text:
                camera.start(tok)
        elif '邮件' in text or '邮件助手' in text:
                mail.start(tok)
        elif '快递' in text:
                express.start(tok)
        elif '笑话' in text:
                joke.main(tok)
        elif '训练' in text:
                snowboytrain.start(tok)
        elif '播放' in text:
            if '音乐' in text:
                m.sui_ji(services, tok)
            else:
                songname = text[2:-1]
                m.sou_suo(services, songname, tok)
        elif '我想听' in text:
            if '音乐' in text:
                m.sui_ji(services, tok)
            else:
                songname = text[3:-1]
                m.sou_suo(services, songname, tok)
        else:
                tuling.start(text, tok)
    else:
        speaker.speacilrecorder()

class skills(Xiaolan):

    def __init__(self):

        pass

    def getskills(self, intent, text):
        
        s = skills()
        m = xlMusic()
        if intent == 'clock':
            clock.start()
        elif intent == 'camera':
            camera.start()
        elif intent == 'smarthome':
            smarthome.start()
        elif intent == 'weather':
            weather.start()
        elif intent == 'music':
            m.start()
        elif intent == 'translate':
            ts.start()
        elif intent == 'email':
            mail.start()
        elif intent == 'joke':
            joke.start()
        elif intent == 'news':
            news.start()
        elif intent == 'express':
            express.start()
        elif intent == 'reintent':
            sk.doskills(text)
        elif intent == 'no':
            speaker.speacilrecorder()
        else:
            sk.doskills(text)
        

    
