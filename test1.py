import urllib2
import json

response = urllib2.urlopen('http://192.168.33.10/test/json.php?id=3&name=gorira')
content = json.loads(response.read())
print(content)