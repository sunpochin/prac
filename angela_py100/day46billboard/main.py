from bs4 import BeautifulSoup
# import lxml
import requests



ret = input("which year do you like to travel(YYYY-MM-DD)? ")
ret = "1999-01-01"
url = "https://www.billboard.com/charts/hot-100/" + ret
response = requests.get(url)
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')

names = [item.getText() for item in soup.find_all("span", class_ = "chart-element__information__song text--truncate color--primary")]
print("names: ", names)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
