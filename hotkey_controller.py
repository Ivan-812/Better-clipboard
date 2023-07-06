from PyQt5.QtCore import QObject, pyqtSignal
from pynput import keyboard
import clip

class HotkeyListener(QObject):
    hotkey_pressed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.debug_active = False
        self.function_active = True
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        hotkeys = {
            '<ctrl>+a': self.active_print_key,
            '<ctrl>+c': self.on_copy
        }

        # Add hotkeys for 'Ctrl+1' to 'Ctrl+0'
        for i in range(10):
            hotkey = f'<alt>+{i}'
            callback = lambda i=i: self.paste_hotkey_onclick(i)
            hotkeys[hotkey] = callback

        self.hotkey_listener = keyboard.GlobalHotKeys(hotkeys)
        self.hotkey_listener.start()

    def active_print_key(self):
        self.debug_active = not self.debug_active
        print('Print key de/activated.')

    def on_press(self, key):
        if self.debug_active:
            try:
                print(f'Key {key.char} pressed')
            except AttributeError:
                print(f'Special key {key} pressed')

    def on_copy(self):
        clip.clip()
        self.hotkey_pressed.emit('on_copy')


    def paste_hotkey_onclick(self, i):
        if self.function_active:
            clip.paste_index(i)

    def stop(self):
        self.listener.stop()
        self.hotkey_listener.stop()