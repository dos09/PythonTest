from banana import Banana
from flask import Flask, request, render_template
import json

app = Flask(__name__, template_folder="pages")

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/banana')
def banana():
    return Banana().run()

@app.route('/test/detect_request_type', methods = ['GET', 'POST'])
def detect_request_type():
    if request.method == 'GET':
        return '[Server]: Request method is GET'
    
    if request.method == 'POST':
        return '[Server]: Request method is POST'
    
@app.route('/test/post', methods = ['POST'])
def process_post_request():
    # printed in terminal
    print('received post request at /test/post with data:')
    for k, v in request.form.items():
        print('[{0}, {1}]'.format(k, v))
        
    return '[Server]: received {0} items'.format(len(request.form))

@app.route('/test/json')
def return_json():
    d = {
        'key A': 'value A',
        'key B': 'value B'
    }
    res = json.dumps(d)
    print(res)
    return res

@app.route('/page')
def show_page():
    return render_template('page.html')
# default folder for pages is 'templates' in the root of my application

if __name__ == '__main__':
    app.run(debug=True)

# 1. How to use:    
# - change environment to one that has flask installed
# - python test_flask.py
# - in browser: http://localhost:5000/page
# 2. On errors:
# can check in terminal to see the status code of a given request
# example:
# "POST /test/json HTTP/1.1" 405 -
# search for 'http status code 405'