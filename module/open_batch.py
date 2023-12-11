import subprocess
import time
import os


class Process:
    def __init__(self, string, mode='batch', popup=True):
        self.pid = None
        if mode == 'folder':
            self.open_explorer(string)
        else:
            self.open_batch(string, mode, popup)

    def open_explorer(self, path):
        # Check if the path exists
        if os.path.exists(path):
            # Open the file explorer
            subprocess.run(['explorer', os.path.realpath(path)])
        else:
            print(f"The path {path} does not exist.")

    def open_batch(self, filename, mode='batch', popup=True):
        if not self.pid:
            dir_name = None
            action_array = ['cmd', '/c', filename]
            if mode == 'batch':
                dir_name = os.path.dirname(filename)
            if popup:
                action_array.insert(0, 'start')
            proc = subprocess.Popen(action_array, shell=True, cwd=dir_name)
            self.pid = proc.pid

    def terminate_batch(self):
        if self.pid:
            try:
                subprocess.check_output('Taskkill /PID %d /F' % self.pid)
            except subprocess.CalledProcessError:
                pass
            self.pid = None


if __name__ == '__main__':
    # p = Process('C:/Users/02005048/Desktop/sample.bat')
    # p = Process('C:/Users/02005048/Documents/Ivan/pyqt/Clipboard Tools/sample.bat')
    commands2 = 'cd C:/Users/02005048/Desktop && echo Hello World! && pause && dir && sample.bat && pause'
    commands3 = 'cd C:/Users/02005048/Documents/Ivan/pyqt/Clipboard Tools && dir && pyuic5 -x C:/Users/02005048/Documents/Ivan/pyqt/Clipboard Tools/user_interface/design/clipboard_2.ui -o C:/Users/02005048/Documents/Ivan/pyqt/Clipboard Tools/user_interface/ui.py'

    p = Process(commands3, mode='cmd')
    # p = Process('sample.bat')
    time.sleep(300)
    # p.terminate_batch()
