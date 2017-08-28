import urllib.parse as urlparse

def examine_url(url):
    res = urlparse.urlparse(url)
    print(res)
    values = {
        'username': res.username, 
        'password': res.password, 
        'hostname': res.hostname, 
        'port': res.port,
        'scheme': res.scheme, 
        'netloc': res.netloc, 
        'path': res.path, 
        'params': res.params, 
        'query': res.query,
        'fragment': res.fragment
    }
    for k, v in values.items():
        print('{:>8}:'.format(k), v)


url = 'mongodb://user_asen:pass_asen@myhost:3306/mydatabase'
#url = 'mongodb://user_asen:pass_asen@myhost:3306'

examine_url(url)