import pyperclip
import time

from pynput import keyboard
import sys

# if .join() 's listener call this, then can terminate
def on_activate_h():
    print('Hotkey H activated, terminate the program')
    # l.stop()
    raise keyboard.Listener.StopException

def on_activate_i():
    print('Hotkey I activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey_h = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+h'),on_activate_h)
hotkey_i = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+i'),on_activate_i)

l = keyboard.Listener(
        on_press=for_canonical(lambda k: hotkey_h.press(k)),
        on_release=for_canonical(lambda k: hotkey_h.release(k)))
l.start()

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()