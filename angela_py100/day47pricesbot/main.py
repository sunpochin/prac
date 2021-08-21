# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import lxml
import requests

# url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
# headers = {
#     "content-type": "text",
#     "Accept-Language": "zh-TW,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
#     }
# response = requests.get(url, headers=headers)
# contents = response.text
# #print("contents: ", contents)
# soup = BeautifulSoup(contents, 'lxml')
# price = soup.find("p", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice")
# print("price: ", price)

url = "https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK/ref=sr_1_1?dchild=1&keywords=AMD+Ryzen+7+5800X+8-core%2C+16-Thread+Unlocked+Desktop+Processor&qid=1629212257&sr=8-1"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
# print("response: ", response)
# soup = BeautifulSoup(response.content, "lxml")
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

# price = soup.find(id="priceblock_ourprice").get_text()
try:
    price = soup.find(id="priceblock_ourprice").get_text()
except AttributeError:
    price = soup.find(id="priceblock_dealprice").get_text()

# title = soup.find(name="span", class_="a-size-medium a-color-base a-text-normal").get_text().strip()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print("\n price: ", price_as_float)
