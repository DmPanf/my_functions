# my_functions.py
# 17-04-2023 DNP
# import my_functions as mf

from IPython.display import clear_output, Javascript
from google.colab import drive
import gc

def help():
  print('\nОсновные функции библиотеки:\n')
  print('mf.help()')
  print('mf.clear(wait=False)')
  print('mf.memfree()')
  print('mf.set_frame(450)')
  print('mf.set_font(18)')

def clear(wait=False):
    clear_output(wait=wait)
    
def memfree():
    gc.collect()
    
def mount():
    drive.mount('/content/drive')

def set_frame(max_height=450):
    display(Javascript(f'''
    google.colab.output.setIframeHeight(0, true, {{maxHeight: {max_height}}})
    '''))

def set_font(font_size=16):
    display(Javascript(f'''
    for (rule of document.styleSheets[0].cssRules){{
        if (rule.selectorText=='body') {{
          rule.style.fontSize = '{font_size}px'
          break
        }}
      }}
    '''))
