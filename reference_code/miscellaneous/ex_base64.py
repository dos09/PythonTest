from datetime import datetime
import base64

now = datetime.now()
print(now)

ts = int(datetime.utcnow().strftime('%Y%m%d%H%M%S'))
print(type(ts), ts)

def enc(s):
    return base64.b64encode(s.encode('utf-8'))

def dec(b):
    return base64.b64decode(b).decode('utf-8')

def enc_file(filename):
    with open(filename, 'rb') as file:
        return base64.b64encode(file.read())

def write_file(enc_data):
    with open('new_one.png', 'wb') as file:
        file.write(base64.b64decode(enc_data))

str = "123Asd"
e = enc(str)
print(e)
d = dec(e)
print(d)
e_file = enc_file('logo.png')
print(e_file)
write_file(e_file)