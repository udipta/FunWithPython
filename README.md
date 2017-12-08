# FunWithPython
trying the gTTS first time

#install gTTS

sudo pip3 install gTTS

#install mpg321

sudo apt install mpg321

#to run as default

chmod +x hi.py quote.py

nano .bashrc

[add at the EOF]

./hi.py [or] multiTTS.py> /dev/null 2> &1

./quote.py > /dev/null 2> &1
