from flask import Flask, request, Response
from flask.json import jsonify
from datetime import datetime
import json
from flask_cors import CORS

app = Flask(__name__)
# without the below setting the returned json is formatted (indented)
# which makes the data unnecessarily big
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
CORS(app)  # for cross domain requests


@app.route('/')
def index():
    return 'Root , now: %s' % (datetime.now())


@app.route('/readjson', methods=['POST'])
def read_json():
    print('read_json')
    for k, v in request.form.items():
        print('[{0}, {1}]'.format(k, v))

    return 'read_json OK'


@app.route('/readheaders', methods=['POST'])
def read_headers():
    print('read_headers')
    for k, v in request.headers.items():
        print(k, v)
    print('asd header: ', request.headers.get('asd'))
    print('Content-Type header: ', request.headers.get('content-type'))

    return 'read_headers OK'


@app.route('/getjson', methods=['GET'])
def return_json():
    d = {
        'key A': 'value A',
        'key B': 'value B'
    }
    return jsonify(d)


@app.route('/getarr', methods=['GET'])
def return_arr():
    arr = [2, 288]
    d = {'arr': arr}
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)
