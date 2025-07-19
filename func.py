from gtts import gTTS

import os

f=open('mytextfile.txt')

x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)
audio.save("audio.wav")
os.system("audio.wav")