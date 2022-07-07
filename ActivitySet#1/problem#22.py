import json
import urllib
from urllib import request
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
if len(url) == 0:
    url = 'http://py4e-data.dr-chuck.net/comments_1546540.json'

print ('Retrieving:', url)
datacomputacional = urllib.request.urlopen(url)
datapython = datacomputacional.read()
info = json.loads(datapython)

count = 0
sum = 0

for item in info["comments"]:
    count += 1
    sum += float (item["count"])

print (count)
print (sum)