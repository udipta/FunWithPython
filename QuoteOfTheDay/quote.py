#!/usr/bin/python3
from gtts import gTTS
import os
import random

def quote(msg):
	out = os.popen('date "+%r"').read()
	message = "Today's Quote is " +msg
	tts = gTTS(text=message, lang='en')
	tts.save("quote.mp3")
	os.system("mpg321 quote.mp3")

file = "quotes"
List =[]
with open(file, 'r+') as f:
	lines = f.readlines()
	for i in range(0, len(lines)):
		line = lines[i]
		line = line[:-2]
		List.append(line)
		if line == "":
			break

quote(random.choice(List))
