import json
from urllib.request import urlopen
json_url = urlopen('http://python-data.dr-chuck.net/comments_42.json')
data = json.loads(json_url.read())
print(data)
