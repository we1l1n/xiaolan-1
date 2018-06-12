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
from xldo import Xiaolan
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

class Nlu(Xiaolan):
        def __init__(self):
                self.intentlist = [
                        ['weather', ['天气', '天气怎么样', '查询天气', '今天天气'], 'weather'],
                        ['talk', ['我想跟你聊一聊', '我想聊你'], 'tuling'],
                        ['default', [], 'tuling'],
                        ['joke', ['我想听笑话', '笑话', '冷笑话', '给我讲一个笑话'], 'joke'],
                        ['news', ['我想听新闻', '今天的新闻', '新闻', '今天有什么新闻'], 'news'],
                        ['smarthome', ['打开', '关闭', '开启', '获取', '传感器', '智能家居'], 'hass'],
                        ['clock'
                self.music_service = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query=', 'hot': 'method=baidu.ting.song.getRecommandSongList&song_id=877578&num=12'}
                self.turn = 0
        def get_intent(text):
        
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
                        return {
                                'intent': None,
                                'skills': None,
                                'command': [
                                        'speacilrecorder'
                                ]
                        }
        
                csumc = apikey + curtimef + 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9' + 'text=' + textl

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
                        return {
                                'intent': None,
                                'skills': None,
                                'command': [
                                        'outputSppech', '对不起，我无法理解您的意思'
                                ]
                        }
                except TypeError:
                        return {
                                'intent': None,
                                'skills': None,
                                'command': [
                                        'outputSppech', '对不起，我无法理解您的意思'
                                ]
                                        
                        }
                else:
                        if intent != None or intent != '':
                            return {
                                    'intent': intent,
                                    'skills': intent,
                                    'command': [
                                            'skills_requests'
                                    ]
                            }
                        else:
                            return {
                                    'intent': None,
                                    'skills': None,
                                    'command': [
                                        'outputSppech', '对不起，我无法理解您的意思'
                                    ]
                            }
                

        def xl_intent(text):

                for a in self.turn:
                         if self.intentlist[a][1][a] in text:
                                return {
                                        'intent': self.intentlist[a][0],
                                        'skills': self.intentlist[a][2],
                                        'command': [
                                                'skills_requests'
                                        ]
                                }

class skills(Xiaolan):

    def __init__(self):

        pass

    def getskills(self, intent, text):
        
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
        

    
