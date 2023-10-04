#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui as pya
import pyperclip as pyc
import time
import random

# In[2]:


# 0 - Abrir o Navegador

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Opera')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')

# 1 - Abrir o site do Rewards

time.sleep(10)
pyc.copy('https://rewards.bing.com/pointsbreakdown')
time.sleep(3)
pya.hotkey('ctrl', 'v')
pya.hotkey('enter')
time.sleep(10)
pya.click(x=491, y=377)

# 2 - Pontos de pesquisas no pc

time.sleep(2)
pya.click(x=247, y=192)
time.sleep(2)
pya.click(x=434, y=243)

contador = 0
y = random.randint(0, 1000)
while contador < 40:
    pyc.copy(f'{y}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=378, y=140)
    contador += 1
    
    
pya.click(x=1347, y=6)
time.sleep(1)
pya.click(x=750, y=411)

# 3 - Pontos do Edge

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Edge')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')
time.sleep(10)
pya.click(x=239, y=55)
time.sleep(2)

contador2 = 0
x = random.randint(0, 1000)
while contador2 < 15:
    pyc.copy(f'{x}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=280, y=117)
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
time.sleep(5)
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

# 5.1 - Trocar a conta e repetir o processo

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Opera')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')

# 5.2 - Abrir o site do rewards
time.sleep(5)
pyc.copy('https://rewards.bing.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')
pya.hotkey('enter')
time.sleep(5)

# 5.3 - Trocando a conta
pya.click(x=1272, y=135)
time.sleep(1)
pya.click(x=1265, y=195)
time.sleep(15)
pya.click(x=494, y=433)
time.sleep(5)
pya.click(x=684, y=348)
pya.click(x=684, y=348)
pya.click(x=684, y=348)
time.sleep(1)
pya.hotkey('backspace') 
time.sleep(1)
pyc.copy('Kos281@hotmail.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')
pya.hotkey('enter')
time.sleep(8)
pya.hotkey('enter')
time.sleep(3)
pya.hotkey('enter')
time.sleep(5)

# 5.4 - Farmando os pontos
pya.click(x=934, y=432)
time.sleep(1)
pya.click(x=491, y=377)
time.sleep(3)
pya.click(x=1116, y=137)
time.sleep(5)
pya.click(x=247, y=192)
time.sleep(2)
pya.click(x=434, y=243)

contador3 = 0
y = random.randint(0, 1000)
while contador3 < 40:
    pyc.copy(f'{y}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=378, y=140)
    contador3 += 1
    
    
pya.click(x=1347, y=6)
time.sleep(1)
pya.click(x=750, y=411)

# 6 - Pontos do Edge

time.sleep(1)
pya.click(x=22, y=746)
pyc.copy('Edge')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')
time.sleep(10)
pya.write('adas')
pya.hotkey('enter')
time.sleep(3)
pya.click(x=1077, y=119)
time.sleep(1)
pya.click(x=1280, y=169)
time.sleep(10)
pya.click(x=1090, y=114)
time.sleep(3)
pyc.copy('Kos281@hotmail.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')
time.sleep(3)
pya.click(x=658, y=422)
time.sleep(3)
pya.click(x=784, y=486)
time.sleep(3)
pya.click(x=795, y=533)
time.sleep(3)
pya.click(x=795, y=533)
time.sleep(10)

contador4 = 0
x = random.randint(0, 1000)
while contador4 < 15:
    pyc.copy(f'{x}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=280, y=117)
    contador4 += 1
    
time.sleep(3)
pya.click(x=1095, y=116)
time.sleep(1)
pya.click(x=1285, y=165)
time.sleep(3)
pya.click(x=1079, y=115)
time.sleep(3)
pyc.copy('Kaua281@hotmail.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')
time.sleep(3)
pya.click(x=658, y=422)
time.sleep(3)
pya.click(x=784, y=486)
time.sleep(3)
pya.click(x=795, y=533)
time.sleep(3)
pya.click(x=795, y=533)
time.sleep(4)
pya.click(x=1339, y=12)
    
# 7 - tirar print da pontuação e mandar no whatsapp pessoal

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
time.sleep(5)
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


# In[9]:


time.sleep(5)
pya.position()


# In[14]:


time.sleep(3)
pya.click(x=1095, y=116)
time.sleep(1)
pya.click(x=1285, y=165)
time.sleep(3)
pya.click(x=1079, y=115)
time.sleep(3)
pyc.copy('Kaua281@hotmail.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')
time.sleep(3)
pya.click(x=658, y=422)
time.sleep(3)
pya.click(x=784, y=486)
time.sleep(3)
pya.click(x=795, y=533)
time.sleep(3)
pya.click(x=795, y=533)


# In[10]:


time.sleep(10)
pya.click(x=1090, y=114)
time.sleep(3)
pyc.copy('Kos281@hotmail.com')
time.sleep(3)
pya.hotkey('ctrl', 'v')
time.sleep(3)
pya.click(x=658, y=422)
time.sleep(3)
pya.click(x=784, y=486)
time.sleep(3)
pya.click(x=795, y=533)
time.sleep(3)
pya.click(x=795, y=533)
time.sleep(10)


# In[3]:


# 0 - Abrir o Navegador

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Opera')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')

# 1 - Abrir o site do Rewards

time.sleep(10)
pyc.copy('https://rewards.bing.com/pointsbreakdown')
time.sleep(3)
pya.hotkey('ctrl', 'v')
pya.hotkey('enter')
time.sleep(10)
pya.click(x=491, y=377)

# 2 - Pontos de pesquisas no pc

time.sleep(2)
pya.click(x=247, y=192)
time.sleep(2)
pya.click(x=434, y=243)

contador = 0
y = random.randint(0, 1000)
while contador < 40:
    pyc.copy(f'{y}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=378, y=140)
    contador += 1
    
    
pya.click(x=1347, y=6)
time.sleep(1)
pya.click(x=750, y=411)

# 3 - Pontos do Edge

time.sleep(5)
pya.click(x=22, y=746)
pyc.copy('Edge')
time.sleep(2)
pya.hotkey('ctrl','v')
time.sleep(1)
pya.hotkey('enter')
time.sleep(10)
pya.click(x=239, y=55)
time.sleep(2)

contador2 = 0
x = random.randint(0, 1000)
while contador2 < 15:
    pyc.copy(f'{x}')
    pya.hotkey('ctrl', 'v')
    time.sleep(2)
    pya.hotkey('enter')
    time.sleep(3)
    pya.click(x=280, y=117)
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
time.sleep(5)
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





# In[ ]:




