import subprocess
import time

# Call the batch file (replace 'my_batch_file.bat' with your batch file)
# subprocess.Popen(['post_alert.bat'], creationflags=subprocess.CREATE_NO_WINDOW)

cmd = 'py C:/Users/02005048/Documents/Repo/C360-Monitor/post_alert.py'
subprocess.call(cmd, shell=True)

