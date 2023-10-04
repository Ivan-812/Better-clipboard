from flask import Flask, render_template, request, jsonify
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


def open_browser():
    command = 'start chrome --incognito --window-size=800,600 http://127.0.0.1:252/'
    subprocess.Popen(command.split(), shell=True)
    # webbrowser.open_new('http://127.0.0.1:252/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(port=252)
