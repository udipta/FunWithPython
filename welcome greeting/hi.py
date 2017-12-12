#!/usr/bin/python3
from gtts import gTTS
import os

def TextToSpeech(msg):
  tts = gTTS(text=msg, lang='en')
  tts.save("hi.mp3")
  os.system("mpg321 -q hi.mp3")
  os.remove('hi.mp3')

out = os.popen('date "+%r"').read()
msg = 'Hi' + os.getlogin() + '! welcome to '+ os.uname()[1] +'! the time is ' + out[:-5]

conn = os.popen('timeout 0.11 nm-online').read()
if conn == '':
  TextToSpeech(msg)
