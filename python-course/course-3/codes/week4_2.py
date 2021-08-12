# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = "http://py4e-data.dr-chuck.net/known_by_Ryhanna.html"
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

pos = 18
times = 7
sum = ""
# Retrieve all of the anchor tags
for it in range(times):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    counter = 0
    for tag in tags:
        counter += 1
        # print('TAG:', tag)
        newurl = tag.get('href', None)
        # print('URL:', newurl)
        url = newurl
        if pos == counter:
            print('Contents:', tag.contents[0])
            sum += tag.contents[0] + " "
            break

print("sum: ", sum)
