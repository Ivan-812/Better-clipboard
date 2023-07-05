from pynput import keyboard
import clip

class HotkeyListener:
    def __init__(self):
        self.active = False
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        hotkeys = {
            '<ctrl>+e': self.terminate,
            '<ctrl>+a': self.active_print_key,
            '<ctrl>+c': clip.clip
        }

        # Add hotkeys for 'Ctrl+1' to 'Ctrl+0'
        for i in range(10):
            hotkey = f'<ctrl>+{i}'
            callback = lambda i=i: clip.paste_index(i)
            hotkeys[hotkey] = callback

        self.hotkey_listener = keyboard.GlobalHotKeys(hotkeys)
        self.hotkey_listener.start()

    def terminate(self):
        raise keyboard.Listener.StopException

    def active_print_key(self):
        self.active = not self.active
        print('Print key de/activated.')

    def on_press(self, key):
        if self.active:
            try:
                print(f'Key {key.char} pressed')
            except AttributeError:
                print(f'Special key {key} pressed')

    def stop(self):
        self.listener.stop()
        self.hotkey_listener.stop()
