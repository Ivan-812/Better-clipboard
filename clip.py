import pyperclip
import time
import json
import os

from pynput.keyboard import Key, Controller

f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "clipboard.json"), 'r+', encoding='utf-8')
clipboard = json.load(f)

def clip():
    time.sleep(0.1)
    clipboard['recent'] = pyperclip.paste()
    save_json()
    # print_clipboard()


def get_json(key):
    return clipboard[str(key)]

def save_to_copy(text):
    pyperclip.copy(text)
    clipboard['recent'] = text
    save_json()

def paste_index(index):
    print(index)
    keyboard = Controller()
    keyboard.release(Key.alt)
    keyboard.type(clipboard[str(index)])


def save_to_index(index, content=None):
    if content is None:
        content = clipboard['recent']
    clipboard[str(index)] = content
    save_json()

def print_clipboard():
    print('----------')
    print('Recent: ' + clipboard['recent'])
    for i in range(10):
        print('Key ' + str(i) + ': ' + clipboard[str(i)])

def save_json():
    f.seek(0)
    json.dump(clipboard, f)
    f.truncate()