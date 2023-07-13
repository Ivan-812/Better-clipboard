from PyQt5.QtCore import QObject, pyqtSignal
from pynput import keyboard

class HotkeyListener(QObject):
    send_signal = pyqtSignal(str, int)

    def __init__(self, hotkey_config=None):
        super().__init__()
        self.debug_active = False
        self.function_active = True
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        self.hotkey_listener_list = []

        self.change_hotkeys(hotkey_config)


    def setup_hotkeys(self, hotkey_config=None):
        hotkeys = {
            '<ctrl>+a': self.active_print_key,
            '<ctrl>+c': self.on_copy
        }

        # Add hotkeys for 'Ctrl+1' to 'Ctrl+0'
        for i in range(10):
            if hotkey_config is None:
                hotkey = f'<alt>+{i}'
            else:
                hotkey = hotkey_config[str(i)]
            callback = lambda i=i: self.paste_hotkey_onclick(i)
            hotkeys[hotkey] = callback

        return hotkeys

    def change_hotkeys(self, hotkey_config=None):
        if len(self.hotkey_listener_list) > 0:
            old_listener = self.hotkey_listener_list.pop()
            old_listener.stop()
        hotkeys = self.setup_hotkeys(hotkey_config)
        listener = keyboard.GlobalHotKeys(hotkeys)
        listener.start()
        self.hotkey_listener_list.append(listener)

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
        self.send_signal.emit('on_copy', -1)

    def paste_hotkey_onclick(self, i):
        if self.function_active:
            self.send_signal.emit('paste_hotkey_onclick', i)

    def stop(self):
        self.listener.stop()
        for listener in self.hotkey_listener_list:
            listener.stop()
