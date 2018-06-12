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
                self.dictcity = ['北京市', '中山市', '上海市', '广州市', '长春市', '天津市', '重庆市', '哈尔滨市', '西安市', '武汉市'
                                '沈阳市', '南京市', '成都市', '石家庄市', '大连市', '齐齐哈尔市', '南昌市', '郑州市', '兰州市', '唐山市'
                                '鞍山市', '徐州市', '济南市', '长沙市', '乌鲁木齐市', '太原市', '抚顺市', '杭州市', '青岛市', 
                                '贵阳市', '包头市', '吉林市', '福州市', '淄博市', '昆明市', '邯郸市', '保定市', '张家口市', '大同市',
                                '呼和浩特市', '本溪市', '丹东市', '锦州市','阜新市', '辽阳市', '鸡西市', '鹤岗市', '大庆市',	'伊春市',
                                '佳木斯市',	'牡丹江市', '无锡市', '常州市', '苏州市','宁波市'
安徽省合肥市	安徽省淮南市	安徽省淮北市	福建省厦门市
山东省枣庄市	山东省烟台市	山东省潍坊市	山东省泰安市
山东省临沂市	河南省开封市	河南省洛阳市	河南省平顶山市
河南省安阳市	河南省新乡市	河南省焦作市	湖北省黄石市
湖北省襄樊市	湖北省荆州市	湖南省株洲市	湖南省湘潭市
湖南省衡阳市	广东省深圳市	广东省汕头市	广东省湛江市
广西南宁市	广西柳州市	青海省西宁市', '']
                self.intentlist = [
                        ['weather', ['天气', '天气怎么样', '查询天气', '今天天气'], [self.dictcity], 'weather'],
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
                                slots = intentlist[a][2]
                                return {
                                        'intent': self.intentlist[a][0],
                                        'skills': self.intentlist[a][3],
                                        'slots': slots
                                        'command': [
                                                'skills_requests'
                                        ]
                                }
                         a = a + 1

class skills(Xiaolan):

    def __init__(self):

        self.skillsdef = {
                'weather': weather.start(),
                'clock': clock.start(),
                'joke': joke.start(),
                'smarthome': self.sm.main(),
                'news': news.start()
        }

    def startskills(self, intentdict, text):
                         
        
        
        

    
