# -*- coding: UTF-8 -*-
import sys
import os
import pyaudio
sys.path.append('/home/pi/xiaolan/snowboy')
import snowboydecoder

class sb(object):
    def __init__(self):
        pass
    def start(self):

        detector = snowboydecoder.HotwordDetector("/home/pi/xiaolan/snowboy/Alexa.pmdl", sensitivity=0.5, audio_gain=1)
        detector.start(detected_callback)

def detected_callback():
    print "检测到唤醒，转交指令给xldo"
    try:
        sys.exit(-1)
    except SystemExit:
        os.system('python /home/pi/xiaolan/xldo.py convenstation')

    
