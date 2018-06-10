import sys
import os
import xldo
from tts import baidu_tts

def start():
    bt = baidu_tts()
    tok = bt.get_token()
    xldo.convenstation(tok)
