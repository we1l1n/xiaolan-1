# coding:UTF-8
# 小蓝设置部分

import sys
import os


def setting():
    selfset = {
               #设置分层第一层（技能，TTS,STT的设置）
               'main_setting': {
                   # 设置分层第二层
                   'STT': 'Baidu_STT', #STT服务选择，目前仅支持百度
                   'TTS': 'Baiud_TTS', #TTS服务选择，目前仅支持百度
                   'NLP': {            #NLP语义理解服务选择，目前仅支持讯飞
                       'key': '9e1b8f6028b14b969cdec166eca127ea',
                       'appid': '5ace1bbb'
                   },
                   'your_name': '翊闳',
                   'loc': '中山'
               },
               'weather': {                     #天气技能，KEY在心知天气获取
                   'key': 'sxyi6ehxblxkqeto'
               },
               'tuling': {                      #图灵聊天技能，KEY,USER_ID在www.tuling123.com获取
                   'key': 'c380ed8f2880443c84892ace36ba6bad',
                   'user_id': '167031'
               },
               'news': {                        #新闻技能，KEY在阿凡达数据获取
                   'key': 'b8fff66168feb233d5cdb2f7931750f3'
               },
               'joke': {                        #说笑话技能，KEY在阿凡达数据获取
                   'key': 'a63ac25e95f741aea51167a05891498c'
               },
               'smarthome': {                   #智能家居技能，passwd，url，port在hass上
                   'passwd': 'y20050801',
                   'url': 'http://192.168.2.121',
                   'port': '8123'
               },
               'map': {                         #地图技能，key在腾讯地图API上申请
                   'key': 'FRMBZ-IREKF-MA3JI-N32XW-HXUZK-K5FUW'
               }
    }
    return selfset
