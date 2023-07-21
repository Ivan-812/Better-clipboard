import pyperclip
import time
import json
import os
import sys

from pynput.keyboard import Key, Controller


class ClipboardManager:
    def __init__(self):
        # Check if the script is running as a PyInstaller bundle
        if getattr(sys, 'frozen', False):
            # If yes, use the _MEIPASS attribute to get the bundle directory
            bundle_dir = sys._MEIPASS
        else:
            # If not, use the __file__ attribute to get the script directory
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the path to the .json file relative to the bundle directory
        json_path = os.path.join(bundle_dir, "config/clipboard.json")

        if not os.path.exists(os.path.join(bundle_dir,'config')):
            os.makedirs(os.path.join(bundle_dir, 'config'))

        # Check if the .json file exists
        if not os.path.exists(json_path):
            # If not, create an empty .json file
            default_content = {
                "num_of_clipboard": 1,
                "recent_clipboard": 0,
                "0": {
                    "name": "Default",
                    "recent": "",
                    "1": "",
                    "2": "",
                    "3": "",
                    "4": "",
                    "5": "",
                    "6": "",
                    "7": "",
                    "8": "",
                    "9": "",
                    "0": "",
                }
            }
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(default_content, f)

        # Open the .json file
        self.file = open(json_path, 'r+', encoding='utf-8')
        self.clipboards = json.load(self.file)

        self.clipboard_index = str(self.get_recent_clipboard())
        self.working_clipboard = self.clipboards[self.clipboard_index]

    def clip(self):
        time.sleep(0.1)
        self.working_clipboard['recent'] = pyperclip.paste()
        self.save_json()
        # print_clipboard()

    def paste_index(self, index, extra_key=False):
        keyboard = Controller()
        keyboard.release(Key.alt)
        print(extra_key)
        if extra_key:
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            print('pressed backspace')
        keyboard.type(self.working_clipboard[str(index)])

    def get_num_of_clipboards(self):
        return self.clipboards['num_of_clipboard']

    def get_recent_clipboard(self):
        return self.clipboards['recent_clipboard']

    def manage_clipboards(self, name, mode='create'):
        if mode == 'create':
            new_clipboard = {
                str(self.clipboards['num_of_clipboard']): {
                        "name": name,
                        "recent": "",
                        "1": "",
                        "2": "",
                        "3": "",
                        "4": "",
                        "5": "",
                        "6": "",
                        "7": "",
                        "8": "",
                        "9": "",
                        "0": "",
                    }
            }
            self.clipboards.update(new_clipboard)
            self.clipboards['num_of_clipboard'] += 1
        elif mode == 'delete':
            for i in range(self.clipboards['num_of_clipboard']):
                if self.clipboards[str(i)]['name'] == name:
                    del self.clipboards[str(i)]
                    self.clipboards['num_of_clipboard'] -= 1
        self.save_json()

    def change_working_clipboard(self, index):
        if index == -1:
            recent = self.get_recent_clipboard()
            self.clipboard_index = str(recent)
            self.working_clipboard = self.clipboards[self.clipboard_index]
        elif index == -2:
            self.clipboard_index = '0'
            self.clipboards['recent_clipboard'] = 0
            self.working_clipboard = self.clipboards[self.clipboard_index]
        elif index < self.get_num_of_clipboards():
            self.clipboard_index = str(index)
            self.working_clipboard = self.clipboards[self.clipboard_index]
            self.clipboards['recent_clipboard'] = index
        self.save_json()

    def get_clipboard_data(self, key):
        return self.working_clipboard[str(key)]

    def save_to_copy(self, text):
        pyperclip.copy(text)
        self.working_clipboard['recent'] = text
        self.save_json()


    def save_to_index(self, index, content=None):
        if content is None:
            content = self.working_clipboard['recent']
        self.working_clipboard[str(index)] = content
        self.save_json()

    def print_clipboard(self):
        for c in range(self.clipboards['num_of_clipboard']):
            index = str(c)
            print('----------')
            print('Index: ' + index + '; Name: ' + self.clipboards[index]['name'])
            print('Recent: ' + self.clipboards[index]['recent'])
            for i in range(10):
                print('Key ' + str(i) + ': ' + self.clipboards[index][str(i)])

    def save_json(self):
        self.file.seek(0)
        json.dump(self.clipboards, self.file)
        self.file.truncate()