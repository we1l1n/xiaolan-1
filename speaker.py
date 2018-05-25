# -*- coding: utf-8 -*-
# 音响控制器
import sys
import os

def ding(): #开始录制指令提示音

    os.system('omxplayer /home/pi/xiaolan/musiclib/ding.wav')

def dong(): #结束录制指令提示音

    os.system('omxplayer /home/pi/xiaolan/musiclib/dong.wav')

def kacha(): #拍照声
    
    os.system('omxplayer /home/pi/xiaolan/musiclib/kacha.mp3')
    
def speak(): #说出的回话
    
    os.system('omxplayer /home/pi/xiaolan/musiclib/say.mp3')

def play(song_name): #音乐播放器
    
    print '正在播放:' + song_name
    os.system('omxplayer /home/pi/xiaolan/musiclib/music.mp3')
    
def speacilrecorder():

    os.system('omxplayer /home/pi/xiaolan/musiclib/speacilrecorder.mp3')
