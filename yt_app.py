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
    print(req)

    with open('config/config.json', 'r') as f:
        data = json.load(f)

    # Edit the data
    data['outputPath'] = req['path']
    data['format'] = req['format']

    with open('config/config.json', 'w') as f:
        json.dump(data, f)

    opts = {'outtmpl': req['path'] + '/%(title)s-%(id)s.%(ext)s'}
    if req['format'] == 'mp4':
        yt.download(req['url'], opts)
    else:
        yt.audio(req['url'], opts)
    return 'POST /download completed'


def open_browser():
    command = 'start chrome --incognito --window-size=800,600 http://127.0.0.1:252/'
    subprocess.Popen(command.split(), shell=True)
    # webbrowser.open_new('http://127.0.0.1:252/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(port=252)
