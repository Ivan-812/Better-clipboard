from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/home')
def example():
    title = 'Hello World'
    numbers = money()
    return render_template('test_template.html', title=title, numbers=numbers)

@app.route('/control')
def control():
    query = request.args.get('option')

@app.route('/data')
def fetching_data():
    my_data = {'key': 'new_value'}
    return jsonify(my_data)

def money():
    out = []
    for i in range(6):
        rand = random.randint(1, 49)
        while rand in out:
            rand = random.randint(1, 49)
        out.append(rand)
    out.sort()
    return out


if __name__ == '__main__':
    app.run(port=1010)
