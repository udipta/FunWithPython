#!/usr/bin/python3
from gtts import gTTS
import os
import random

def quote(msg):
	out = os.popen('date "+%r"').read()
	message = "Today's Quote is " +msg
	tts = gTTS(text=message, lang='en')
	tts.save("quote.mp3")
	os.system("mpg321 -q quote.mp3")
	os.remove('quote.mp3')

	
def chkNet():
	import requests
	try:
		response = requests.get("https://www.google.com")
		return True
	except requests.ConnectionError:
		return False

	
def readFile(filename):
	with open(filename, 'r+') as f:
		temp = f.read().splitlines()
		return temp

List = readFile('quotes')


if chkNet():
	quote(random.choice(List))
