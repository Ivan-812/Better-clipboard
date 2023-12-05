import time

from flask import Flask, render_template, request, jsonify, Response
import webbrowser
import subprocess
from threading import Timer
import json
import yt

app = Flask(__name__)

@app.route('/')
def example():
    f = open('config/config.json')
    data = json.load(f)
    return render_template('yt.html', data=data)


@app.route('/download', methods=['POST'])
def download():
    req = request.json

    with open('config/config.json', 'w') as f:
        json.dump(req, f)

    yt.json_download(req)
    return 'POST /download completed'

@app.route('/stream')
def stream():
    def event_stream():
        current_log_length = 0
        while True:
            while len(yt.logs) > current_log_length:
                yield 'data: %s\n\n' % yt.logs[current_log_length]
                current_log_length += 1
            time.sleep(1)
    return Response(event_stream(), mimetype="text/event-stream")


def open_browser():
    command = 'start chrome --incognito --window-size=800,600 http://127.0.0.1:252/'
    subprocess.Popen(command.split(), shell=True)
    # webbrowser.open_new('http://127.0.0.1:252/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(port=252)
