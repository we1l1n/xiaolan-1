# -*- coding: utf-8 -*-
# 小蓝中央控制

import sys
import os
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import speaker
import nlp
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
from smarthome import hass

# 小蓝设置部分:
def set():
    setting = {
               #设置分层第一层（技能，TTS,STT的设置）
               'main_setting': {
                   # 设置分层第二层
                   'STT': 'Baidu_STT', #STT服务选择，目前仅支持百度
                   'TTS': 'Baiud_TTS', #TTS服务选择，目前仅支持百度
                   'your_name': '翊闳',
                   'loc': '中山'
               }
               'weather': {                     #天气技能，KEY在心知天气获取
                   'key': 'sxyi6ehxblxkqeto'
               }
               'tuling': {                      #图灵聊天技能，KEY,USER_ID在www.tuling123.com获取
                   'key': 'c380ed8f2880443c84892ace36ba6bad',
                   'user_id': '167031'
               }
               'news': {                        #新闻技能，KEY在阿凡达数据获取
                   'key': 'b8fff66168feb233d5cdb2f7931750f3'
               }
               'joke': {                        #说笑话技能，KEY在阿凡达数据获取
                   'key': 'a63ac25e95f741aea51167a05891498c'
               }
               'smarthome': {                   #智能家居技能，passwd，url，port在hass上
                   'passwd': 'y20050801',
                   'url': 'http://hassio.local',
                   'port': '8123'
               }
                   
                   
                           
                            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def welcome():

    print ('''

    ###################################
    #     小蓝-中文智能家居对话机器人      #
    #   (c)蓝之酱-1481605673@qq.com    #
    # www.github.com/xiaoland/xiaolan #
    #         欢迎使用!!!  :)          #
    ###################################

    ''')
    os.system('omxplayer /home/pi/xiaolan/musiclib/welcome.mp3')
    os.system('pulseaudio --start')
    awaken()

def awaken():

    os.system('python /home/pi/xiaolan/snowboy.py')

def convenstation():

    bs = baidu_stt(1, 2, 3, 4)
    bt = baidu_tts()
    r = recorder()
    s = skills()
    
    tok = bt.get_token()

    speaker.ding()
    r.record()
    speaker.dong()
    text = bs.stt('./voice.wav', tok)
    
    intent = nlp.get_intent(text)
    s.getskills(intent, text, tok)

def sconvenstation():

    speaker.speacilrecorder()

class skills(object):

    def __init__(self):

        pass

    def getskills(self, intent, text, tok):

        if intent == 'clock':
            clock.start(tok)
        elif intent == 'camera':
            camera.start(tok)
        elif intent == 'smarthome':
            smarthome.start(tok)
        elif intent == 'weather':
            weather.start(tok)
        elif intent == 'music':
            music.start(tok)
        elif intent == 'mail':
            mail.start(tok)
        elif intent == 'joke':
            joke.start(tok)
        elif intent == 'news':
            news.start(tok)
        elif intent == 'tuling':
            tuling.start(text, tok)
        elif intent == 'snowboytrain':
            snowboytrain.start(tok)
        elif intent == 'raspberrypi-gpio':
            raspberrypigpio.start(tok)
        elif intent == 'respeaker':
            speaker.speak()
        elif intent == 'no':
            sconvenstation()
        elif intent == 'reintent':
            intent = nlp.do_intent(text, tok)
            s.getskills(intent, text, tok)

try:
    
    if sys.argv[1] != None:
        mode = sys.argv[1]
        if mode == 'unawaken':
            convenstation()
        elif mode == 'awaken':
            awaken()
        elif mode == 'convenstation':
            convenstation()
    else:
        welcome()
except:
    welcome()
