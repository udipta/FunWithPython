#!/usr/bin/python3
from gtts import gTTS
import os


def textToSpeech(msg,language):
	tts = gTTS(text=msg, lang=language)
	tts.save("hi.mp3")
	os.system('mpg321 hi.mp3')
	os.remove('hi.mp3')

txt = ['FOR ENGLISH PRESS 1','বাংলার জন্য ২ টিপুন','हिंदी के लिए ३ दबाएं']
lng = ['en', 'bn', 'hi']
for i in range(0, len(txt)):
	textToSpeech(txt[i], lng[i])

out = os.popen('date "+%r"').read()
msg =['Hi Uddipta! welcome to jarvis! the time is', 'উদ্দীপ্ত ! জারভিসে আপনাকে স্বাগত । এখন সময়..', 'उदिप्ता! जार्विस में आपका स्वागत है! अब समय है..']

i = int(input())
if i in range(4):
	j = i-1
	temp = msg[j] + out[:-5]
	textToSpeech(temp,lng[j])
else :
	textToSpeech("Sorry! it's an invalid response",'en')
