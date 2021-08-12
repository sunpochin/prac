import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://py4e-data.dr-chuck.net/comments_1025277.xml"
#parms = dict()
#url = serviceurl + urllib.parse.urlencode(parms)
url = serviceurl
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

print("tree: ", tree)
results = tree.findall('commentinfo')
print("results: ", results)
sum = 0
for elt in tree.iter():
    #    print(elem)
    print(elt.tag, elt.text)
    if("count" == elt.tag):
        sum = sum + int(elt.text)

print("sum: ", sum)

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1:
#         break

#     parms = dict()
#     parms['address'] = address
#     if api_key is not False:
#         parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)

#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print('lat', lat, 'lng', lng)
#     print(location)
