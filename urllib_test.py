import urllib,requests
requests.get('URL')
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('URL', params=payload)

print r