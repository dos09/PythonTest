from datetime import datetime, timedelta
now = datetime.now()
d1 = now - timedelta(days=3)
d2 = now - timedelta(days=2)
d3 = now - timedelta(days=1)
name = 'a'
a = {'name': 'a', 'last_update': d1}
b = {'name': 'a', 'last_update': d2}
c = {'name': 'b', 'last_update': d3}
data = [a, b, c]
data.sort(key=lambda x: (x['name'] == name, x['last_update']), reverse=True)
for item in data:
    print(item)