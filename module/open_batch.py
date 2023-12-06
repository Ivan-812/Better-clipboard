import subprocess
import time
import os


class Process:
    def __init__(self, string, mode='batch'):
        self.pid = None
        self.open_batch(string, mode)


    def open_batch(self, filename, mode='batch'):
        if not self.pid:
            if mode == 'batch':
                dir_name = os.path.dirname(filename)
                proc = subprocess.Popen(['start', 'cmd', '/c', filename], shell=True, cwd=dir_name)
            else:
                proc = subprocess.Popen(['start', 'cmd', '/c', filename], shell=True)
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

    p = Process(commands2, mode='cmd')
    # p = Process('sample.bat')
    time.sleep(3)
    p.terminate_batch()
