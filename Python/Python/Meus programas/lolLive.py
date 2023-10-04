#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pyautogui as pya
import pyperclip as pyc
import time 


# In[6]:
# 0 - Abrir o Navegador
time.sleep(2)
pya.click(x=117, y=745, button='right')
time.sleep(2)
pya.click(x=120, y=553)

# 1 - Abrir o Site do Lolesports

time.sleep(2)
pya.hotkey('ctrl', 't')
time.sleep(4)
pyc.copy('https://lolesports.com')
pya.hotkey('ctrl', 'v')
time.sleep(3)
pya.hotkey('enter')
time.sleep(5)

# 2 - Acessar a live

pya.click(x=96, y=256)


# In[ ]:




