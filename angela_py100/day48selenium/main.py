# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
chrome_driver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = ""
# url = "https://www.amazon.com/MSI-MPG-B550-Motherboard-Processors/dp/B089CQFHHZ/ref=pd_sbs_1/137-2717329-5041766?pd_rd_w=JV2W8&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=WG6PWP08CSVYAM4166HQ&pd_rd_r=871a31d2-0c73-48ef-8bbb-a18ebd95fa0f&pd_rd_wg=Hq5lz&pd_rd_i=B089CQFHHZ&psc=1"
# driver.get(url)
# price = driver.find_element_by_id("priceblock_ourprice")
# print("price: ", price.text)

# url = "https://python.org"
# driver.get(url)
# search_bar = driver.find_element_by_name("q")
# print("search_bar: ", search_bar.tag_name)
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
#
# # harder to find, use css_selector.
# documentation = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation.text)

url = "https://python.org"
driver.get(url)
# by xpath. when no particular id, class, name
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print('bug_link: ', bug_link.text, '\n')

# links = driver.find_elements_by_css_selector('.event-widget li')
# linkarr = []
# [linkarr.append(link.text) for link in links]
# linkdict = {}
# for link in linkarr:
#     linkdict[link.split('\n')[0]] = link.split('\n')[1]
# print('linkdict: ', linkdict)

event_times = driver.find_elements_by_css_selector('.event-widget time')
# '.event-widget a' will get first 'More', so not ok.
# event_names = driver.find_elements_by_css_selector('.event-widget a')
event_names = driver.find_elements_by_css_selector('.event-widget li a')

events = {}
for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

driver.quit()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
