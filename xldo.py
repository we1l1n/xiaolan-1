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
    mode = sys.argv[1]
    if mode == 'unwelcome':
        awaken()
    elif mode == 'unawaken':
        convenstation()
    elif mode == 'awaken':
        awaken()
    elif mode == 'convenstation':
        convenstation()
    else:
        welcome()
except:
    print ('错误！请随意输入一个字符，如python xldo.py a')
