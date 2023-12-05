import subprocess
import time


class Process:
    def __init__(self, filename):
        self.pid = None
        self.open_batch(filename)

    def open_batch(self, filename):
        if not self.pid:
            proc = subprocess.Popen(['start', filename], shell=True)
            self.pid = proc.pid

    def terminate_batch(self):
        if self.pid:
            try:
                subprocess.check_output('Taskkill /PID %d /F' % self.pid)
            except subprocess.CalledProcessError:
                pass
            self.pid = None


if __name__ == '__main__':
    p = Process('C:/Users/02005048/Desktop/sample.bat')
    # p = Process('sample.bat')
    time.sleep(3)
    p.terminate_batch()
