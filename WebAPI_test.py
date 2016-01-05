import urllib2, urllib

#URL
url = 'http://192.168.33.10/test/json.php'

#parames
id = 4
name = 'gorira'

#parames_encode
params = {'id' : id,'name':name}
params = urllib.urlencode(params)

#URL_parames_bond
URL = url + '?' + params

print URL

#server_reqest
response = urllib2.urlopen(URL)

#server_response
content = response.read()
print(content)