from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# url = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(url)
#
# # articlecnt = driver.find_element_by_id('articlecount')
# articlecnt = driver.find_element_by_css_selector('#articlecount a')
# print('article cnt: ', articlecnt.text)
#
# # all_portals = driver.find_element_by_link_text('All portals')
# # all_portals.click()
#
# search = driver.find_element_by_name('search')
# search.send_keys('python')
# search.send_keys(Keys.ENTER)


# url = "https://secure-retreat-92358.herokuapp.com/"
# driver.get(url)
# fname = driver.find_element_by_name('fName')
# fname.send_keys('pochin')
# lname = driver.find_element_by_name('lName')
# lname.send_keys('sun')
# email = driver.find_element_by_name('email')
# email.send_keys('sunpochin@gmail.com')
# signup = driver.find_element_by_css_selector('form button')
# signup.click()

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)
cookie = driver.find_element_by_id('cookie')
import time
timeout = time.time() + 60*5


cnt = 0
while(True):
    buyCursor = driver.find_element_by_id('buyCursor')
    buyGrandma = driver.find_element_by_id('buyGrandma')
    buyFactory = driver.find_element_by_id('buyFactory')
    buyMine = driver.find_element_by_id('buyMine')

    cnt += 1
    print('cnt: ', cnt)
    cookie.click()
    if time.time() > timeout:
        break
    if (cnt % 5 == 0):
        try:
            if buyMine is None or buyGrandma is None or buyCursor is None:
                print('buyMine: ', buyMine)
                print('buyGrandma: ', buyGrandma)
                print('buyCursor: ', buyCursor)
#                continue
            print('buyMine: ', buyMine.text)
            buyMine.click()
            print('buyGrandma: ', buyGrandma.text)
            buyGrandma.click()
            buyCursor.click()
        except ValueError:
            continue
#    time.sleep(1)
# driver.quit()
