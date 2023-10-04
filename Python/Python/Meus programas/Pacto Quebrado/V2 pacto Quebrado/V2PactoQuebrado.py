#!/usr/bin/env python
# coding: utf-8

# In[11]:

import pyautogui as pya
import pyperclip as pyc
import time
import random

# 3 - Pontos no Edge https://www.bing.com/?scope=web&cc=BR&FORM=HDRSC1

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Edge')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')
time.sleep(10)
pyc.copy('https://www.bing.com/?scope=web&cc=BR&FORM=HDRSC1')
time.sleep(2)
pya.hotkey('ctrl','v')
pya.hotkey('enter')
time.sleep(4)
pya.click(x=413, y=229)
time.sleep(2)

contador2 = 0
x = random.randint(0, 1000)
while contador2 < 70:
    pyc.copy(f'{x}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=236, y=118)
    contador2 += 1
   
    
time.sleep(1)
pya.click(x=1347, y=6)

# 4 - tirar print da pontuação e mandar no whatsapp pessoal

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Opera')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')

time.sleep(10)
pyc.copy('https://rewards.bing.com/pointsbreakdown')
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')
time.sleep(10)
pya.hotkey('fn', 'prtsc')
time.sleep(3)
pya.click(x=20, y=286)
time.sleep(10)
pya.click(x=241, y=164)
time.sleep(5)
pya.hotkey('ctrl','v')
time.sleep(2)
pya.hotkey('enter')
time.sleep(8)
pya.click(x=1347, y=6)

# In[ ]:




