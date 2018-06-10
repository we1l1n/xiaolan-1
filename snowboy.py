# -*- coding: UTF-8 -*-
import sys
import os
import pyaudio
from tts import baidu_tts
from tts import youdao_tts
from stt import baidu_stt
import nlu
import speaker
from recorder import recorder
sys.path.append('/home/pi/xiaolan/snowboy')
import snowboydecoder

class sb(object):
    def __init__(self):
        pass
    def start(self):

        detector = snowboydecoder.HotwordDetector("/home/pi/xiaolan/snowboy/Alexa.pmdl", sensitivity=0.5, audio_gain=1)
        detector.start(convenstation)

def convenstation():

    bs = baidu_stt(1, 2, 3, 4)
    bt = baidu_tts()
    r = recorder()

    speaker.ding()
    r.record()
    speaker.dong()
    text = bs.stt('./voice.wav', tok)
    if text == None:
        speaker.speacilrecorder()
    else:
        return [nlu.get_intent(text, tok), text]


    
