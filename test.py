import json
import requests
import sys

url = 'http://13thagegen.matthewodle.com'

try:
    r = requests.get(url)
except:
    print ("target unavailable: {}".format(url))
    sys.exit()

assert r.status_code == 200

character = json.loads(r.text)

print (character)

