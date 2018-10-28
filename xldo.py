# -*- coding: utf-8 -*-
# 小蓝中央控制

import sys
import os
from stt import baidu_stt
from tts import baidu_tts
from tts import youdao_tts
from recorder import recorder
import speaker
from nlu import Nlu
from nlu import Skills
import setting
sys.path.append('/home/pi/xiaolan/skills/')
import clock
import weather
import mail
import tuling
import joke
import news
import camera
import ts
import express
import snowboytrain
from smarthome import hass
from maps import maps
from music import xlMusic


class Xiaolan(object):

    def __init__(self):
        
        self.awaken = self.awaken()
        self.selfset = setting.setting()
        self.xl = Xiaolan()
        self.r = recorder()
        self.bt = baidu_tts()
        self.yt = youdao_tts()
        self.bs = baidu_stt(1, 2, 3, 4)
        self.sk = Skills()
        self.sm = hass()
        self.mu = xlMusic()
        self.ma = maps()
        self.xlnlu = Nlu()
        self.tok = bt.get_token()
        
    def awaken(self):
    
        os.system('python /home/pi/xiaolan/snowboy.py')
    
    def welcome(self):
    
        print ('''

        ###################################
        #     小蓝-中文智能家居对话机器人      #
        #   (c)蓝之酱-1481605673@qq.com    #
        # www.github.com/xiaoland/xiaolan #
        #         欢迎使用!!!  :)          #
        ###################################

        ''')
        bt.tts(self.selfset['main_setting']['your_name'] + '，你好啊，我是你的小蓝', self.tok)
        speaker.speak()
        os.system('pulseaudio --start')
        self.xl.awaken()
    
    def replacenumber(self, text):
        try:
            text.replace('零', 0)
            text.replace('一', 1)
            text.replace('二', 2)
            text.replace('三', 3)
            text.replace('四', 4)
            text.replace('五', 5)
            text.replace('六', 6)
            text.replace('七', 7)
            text.replace('八', 8)
            text.replace('九', 9)
        except TypeError:
            return text
        except KeyError:
            return text
        else:
            return text
        
    
    def convenstation(self):
        
        speaker.ding()
        r.record()
        speaker.dong()
        text = self.bs.stt('./voice.wav', self.tok).replace(',', '')
        text = self.xl.replacenumber(text)
        if text == None or text == '':
            speaker.speacilrecorder()
        else:
            intentdict = xlnlu.xl_intent(text)
            sk.getskills(intentdict[a][0], text)
    


try:
    if sys.argv[1] == 'unawaken':
        convenstation()
    else:
        welcome()
except:
    welcome()
