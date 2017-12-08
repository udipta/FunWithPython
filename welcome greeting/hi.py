#!/usr/bin/python3
from gtts import gTTS
import os
out = os.popen('date "+%r"').read()
msg = 'Hi! welcome to jarvis! the time is ' + out[:-5]
tts = gTTS(text=msg, lang='en')
tts.save("hi.mp3")
os.system("mpg321 hi.mp3")
