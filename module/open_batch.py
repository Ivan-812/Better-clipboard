import subprocess
import time
import os


class Process:
    def __init__(self, filename):
        self.pid = None
        self.open_batch(filename)

    def open_batch(self, filename):
        if not self.pid:
            dir_name = os.path.dirname(filename)
            proc = subprocess.Popen(['start', 'cmd', '/c', filename], shell=True, cwd=dir_name)
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
    p = Process('C:/Users/02005048/Documents/Ivan/pyqt/Clipboard Tools/sample.bat')
    # p = Process('sample.bat')
    time.sleep(3)
    p.terminate_batch()
