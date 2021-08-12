from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1025278.json"
data = urlopen(url, context=ctx).read().decode()

print("data: ", data)
js = json.loads(data)

sum = 0
for item in js["comments"]:
    print('Name', item['name'])
    print('count', item['count'])
    sum = sum + int(item['count'])
print("sum: ", sum)
