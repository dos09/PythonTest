# This is here to test client.py

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def url_test():
    header_name = request.headers.get('name')
    body = request.get_json(silent=True) or {}
    body_name = body.get('name')
    print('headers:', request.headers)
    print('request body:', body)
    print('header name:', header_name)
    print('body name:', body_name)
    return "server response text"

if __name__ == '__main__':
    app.run(debug=True)

# curl -X POST "http://127.0.0.1:5000/" -H "Content-Type:
# application/json" -H "name:HEADER NAME" -d "{\"name\":\"BODY NAME\"}"
