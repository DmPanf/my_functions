# my_functions.py
# 17-04-2023 DNP
# import my_functions as mf

from IPython.display import clear_output, Javascript
from google.colab import drive
import requests
import json
import gc

def help():
  print('\n💠 Основные функции библиотеки:')
  print('mf.help()')
  print('mf.clear(wait=False)')
  print('mf.mount()')
  print('mf.memfree()')
  print('mf.set_frame(450)')
  print('mf.set_font(18)')
  print('mf.send_message(message, "HTML")')

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


def send_message(message, parse_mode='Markdown', chat_id=None, token=None, file='/content/drive/MyDrive/zTest/env.json'):
    """
    Пример использования:
    message = f'Отправка сообщения из Colab: <b>[{my_id}]</b>'
    response = send_message(message, 'HTML') 
    print(response)
    """
    if chat_id is None or token is None:
        with open(file) as f:
            data = json.load(f)
        token, chat_id = data.values()
      
    # print('\n', message)
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message, 'parse_mode': parse_mode}
    response = requests.post(url, json=data)
    return json.loads(response.text)

  
# вызов функции help() при импорте модуля
# help()
