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
from xldo import Xiaolan
from recorder import recorder
from tts import baidu_tts
from stt import baidu_stt
from tts import youdao_tts
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
                self.dictcity = [
                                '北京市', '中山市', '上海市', '广州市', '长春市', '天津市', '重庆市', '哈尔滨市', '西安市', '武汉市',
                                '沈阳市', '南京市', '成都市', '石家庄市', '大连市', '齐齐哈尔市', '南昌市', '郑州市', '兰州市', '唐山市',
                                '鞍山市', '徐州市', '济南市', '长沙市', '乌鲁木齐市', '太原市', '抚顺市', '杭州市', '青岛市', 
                                '贵阳市', '包头市', '吉林市', '福州市', '淄博市', '昆明市', '邯郸市', '保定市', '张家口市', '大同市',
                                '呼和浩特市', '本溪市', '丹东市', '锦州市','阜新市', '辽阳市', '鸡西市', '鹤岗市', '大庆市',	'伊春市',
                                '佳木斯市',	'牡丹江市', '无锡市', '常州市', '苏州市','宁波市', '合肥市', '淮南市', '安徽省淮北市', '福建省厦门市',
                                '枣庄市', '烟台市', '潍坊市', '泰安市', '临沂市', '开封市', '洛阳市', '平顶山市', '安阳市', '新乡市', '焦作市', '黄石市',
                                '襄樊市', '荆州市', '株洲市', '湘潭市', '衡阳市', '深圳市',' 汕头市', '湛江市', '南宁市', '柳州市', '西宁市'
                ]
                self.intentlist = [
                        ['weather', ['天气', '天气怎么样', '查询天气', '今天天气'], ['city', self.dictcity], 'weather'],
                        ['talk', ['我想跟你聊一聊', '我想聊你'], [], 'tuling'],
                        ['joke', ['我想听笑话', '笑话', '冷笑话', '给我讲一个笑话'], [], 'joke'],
                        ['news', ['我想听新闻', '今天的新闻', '新闻', '今天有什么新闻'], ['newstype', self.dictnewstype] 'news'],
                        ['smarthome', ['打开', '关闭', '开启', '获取', '传感器', '智能家居'], ['mode', self.dicthassmode, 'cortolmode', self.dicthasscortolmode, 'device': self.dictdevice], 'hass'],
                        ['clock', ['设定一个闹钟', '闹钟', '设置新闹钟', '新建闹钟'], ['day', self.dictday, 'weekday', self.dictweekday, 'hour', self.dicthour, 'minute', self.dictminute], 'clock']
                ]
                self.music_service = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query=', 'hot': 'method=baidu.ting.song.getRecommandSongList&song_id=877578&num=12'}
                self.turn = 0
                self.turns = 1
        
        def get_slots(slotslist, text):

            try:
                for a in self.turn:
                        if slotslist[1][a] in text:
                                returndict = {
                                        slotslist[0]: slotslist[1][a]
                                }
                                break
                        else:
                                a = a + 2
                return returndict
            except KeyError:
                return None
                        
        def iflytek_intent(self, text):
                
                appid = self.selfset['main_setting']['NLU']['iflytek']['appid']
                apikey = self.selfset['main_setting']['NLU']['iflytek']['key']
                curtimeo = int(time.time())
                curtimef = str(curtimeo)
        
                try:
                        textl = base64.b64encode(text)
                except TypeError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'speaker', 'speacilrecorder'
                                ]
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                        }
        
                csumc = apikey + curtimef + 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9' + 'text=' + textl

                c = hashlib.md5()
                c.update(csumc)
                checksuml = c.hexdigest()
        
                headers = {'X-Appid': appid, 'Content-type': 'application/x-www-form-urlencoded; charset=utf-8', 'X-CurTime': curtimef, 'X-Param': 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9', 'X-CheckSum': checksuml}
                url = 'http://api.xfyun.cn/v1/aiui/v1/text_semantic?text=' + textl
        
                r = requests.post(url,
                                  headers=headers)
                json = r.json()
                try:
                        intent = json['data']['service']
                except KeyError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                ]
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                        }
                except TypeError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                ]
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                                        
                        }
                else:
                        if intent != None or intent != '':
                            return {
                                    'intent': intent,
                                    'skill': intent,
                                    'command': [
                                            'skills_requests'
                                    ]
                                    'states': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                        else:
                            return {
                                    'intent': None,
                                    'skill': None,
                                    'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                    ]
                                    'states': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                

        def xl_intent(self, text):
                
            try:
                for b in self.turn:
                    
                        if self.intentlist[b][1][b] in text:
                                if self.intentlist[b][2] != [] or self.intentlist[b][1] != None:
                                        slots = self.xlnlu.get_slots(self.intentlist[b][2], text)
                                else:
                                        slots = 'unset'
                                returndict = {
                                        'intent': self.intentlist[b][0],
                                        'skill': self.intentlist[b][3],
                                        'slots': slots
                                        'command': [
                                                'skill', 'start'
                                        ]
                                        'states': [
                                                'xl_nlu_intent_back'
                                        ]
                                }
                                break
                        else:
                                b = b + 1
                return returndict
            except KeyError:
                return {
                        'intent': self.xlnlu.iflytek_intent(text),
                        'skill': self.xlnlu.iflytek_intent(text),
                        'slots': None,
                        'commmands': [
                                'skill', 'start'
                        ]
                        'states': [
                                'iflytek_nlu_intent_back'
                        ]
                }
                        
                                
                                
                                

class Skills(Xiaolan):

    def __init__(self):

        self.skillsdef = {
                'weather': ['weather', weather.start()],
                'clock': ['clock', clock.start()],
                'joke': ['joke', joke.start()],
                'smarthome': ['smarthome', self.sm.main()],
                'news': ['news', news.start()]
        }

    def startskills(self, intentdict, text):
        
        if intentdict[3] == self.skillsdef[intentdict[0]][0]:
            
        
        

    
