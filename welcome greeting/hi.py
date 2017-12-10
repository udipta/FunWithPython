#!/usr/bin/python3
from gtts import gTTS
import os


def TextToSpeech(msg):
  tts = gTTS(text=msg, lang='en')
  tts.save("hi.mp3")
  os.system("mpg321 -q hi.mp3")
  os.remove('hi.mp3')

  
def chkNet():
	import requests
	try:
		response = requests.get("https://www.google.com")
		return True
	except requests.ConnectionError:
		return False
  
out = os.popen('date "+%r"').read()
usr = os.popen('whoami').read()
host = os.popen('hostname').read()
msg = 'Hi' + usr + '! welcome to '+ host +'! the time is ' + out[:-5]

if chkNet():
  TextToSpeech(msg)
