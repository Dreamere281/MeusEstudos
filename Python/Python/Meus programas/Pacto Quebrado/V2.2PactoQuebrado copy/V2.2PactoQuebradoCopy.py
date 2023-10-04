#!/usr/bin/env python
# coding: utf-8


import pyautogui as pya
import pyperclip as pyc
import time
import random

# 1 - Pontos no Edge https://www.bing.com/?scope=web&cc=BR&FORM=HDRSC1

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Microsoft Edge')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')
time.sleep(20)
pyc.copy('FarmDePontos')

time.sleep(2)
pya.hotkey('ctrl','v')
pya.hotkey('enter')
time.sleep(4)

contador2 = 0
while contador2 < 70:
    x = random.randint(0, 1000)
    pyc.copy(f'{x}')
    time.sleep(1)
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=236, y=118)
    pya.hotkey('enter')
    contador2 += 1

# 2 - Mudando a conta
pya.click(x=1125, y=115) 
time.sleep(2)
pya.click(x=1285, y=167)
time.sleep(3)
pya.click(x=1135, y=117)
time.sleep(3)

# Conta Secundária
pyc.copy('Kos281@hotmail.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')

time.sleep(2)
pya.click(x=541, y=458)
time.sleep(2)
pya.click(x=798, y=481)
time.sleep(4)
pya.hotkey('enter')
time.sleep(3)
pya.hotkey('enter')
time.sleep(5)

contador3 = 0
pya.click(x=236, y=118)
while contador3 < 70:
    x = random.randint(0, 1000)
    pyc.copy(f'{x}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=236, y=118)
    contador3 += 1



pya.click(x=1125, y=115) 
time.sleep(2)
pya.click(x=1285, y=167)
time.sleep(3)
pya.click(x=1135, y=117)
time.sleep(3)

# Voltando Para A Conta Principal
pyc.copy('Kaua281@hotmail.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')

time.sleep(2)
pya.click(x=541, y=458)
time.sleep(2)
pya.click(x=798, y=481)
time.sleep(4)
pya.hotkey('enter')
time.sleep(3)
pya.hotkey('enter')
time.sleep(5)

time.sleep(1)
pya.click(x=1347, y=6)

# 3 - tirar print da pontuação e mandar no whatsapp pessoal

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

