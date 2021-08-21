from bs4 import BeautifulSoup
from requests_html import HTMLSession
import lxml
import requests

WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "./data/100_best_movies.html"

# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()

    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


# Read web file if it exists, load from internet if it doesn't exist
contents = read_web_file()

# url = "https://www.empireonline.com/movies/features/best-movies-2/"
# response = requests.get(url)
# contents = response.text
soup = BeautifulSoup(contents, 'html.parser')
# print("soup: ", soup.prettify() )
#
h3s = soup.find_all(name="h3")
print("h3s: ", h3s)
#
# movies_tag = soup.find_all(name='div', class_='jsx-3821216435 listicle-item')
# movies_list = [movie.find(name='img')['alt'] for movie in movies_tag]
# #print("movies_tag: ", movies_tag)
# print("movies_list: ", movies_list)


# response = requests.get("https://news.ycombinator.com/news")
# yc_web = response.text
# soup = BeautifulSoup(yc_web, 'html.parser')
#
# # article_tag = soup.find(name="a", class_="storylink")
# # print("article_tag: ", article_tag)
# #
# # article_text = article_tag.getText()
# # article_link = article_tag.get("href")
# # article_upvote = soup.find(name="span", class_="score").getText()
# articles = soup.find_all(name="a", class_="storylink")
# # print("articles: ", articles)
# texts = []
# links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     link = article_tag.get("href")
#     texts.append(text)
#     links.append(link)
#
# #print(int(upvotes[0].split()[0]))
# upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# # for vor
# print("article_text: ", texts)
# print("article_link: ", links)
# print("upvotes: ", upvotes)
#
# largest_num = max(upvotes)
# largest_idx = upvotes.index(largest_num)
#
# print("largest_idx: ", largest_idx, ", largest_num: ", largest_num)
# print("largest text: ", texts[largest_idx])
# print("largest link: ", links[largest_idx])
# TODO: test

# print("text: ", article_text)
# print("article_link: ", article_link)
#print("article_upvotes: ", article_upvotes)

#article_upvote = soup.


# contents = ""
# with open('website.html', 'r') as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# #    soup = BeautifulSoup(contents, 'lxml')
#
# # print("title: ", soup.title)
# # print("title.name: ", soup.title.name)
# # print("title.string: ", soup.title.string)
#
# # print("content: ", content)
# all_anchor_tags = soup.find_all(name="a")
# print("all_anchor_tags: ", all_anchor_tags)
# # for tag in all_anchor_tags:
# #    print("tag.getText(): ", tag.getText())
# #    print(tag.get("href"))
#
# print("\n\n")
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading )
#
# company_url = soup.select_one(selector="p a")
# print("company_url: ", company_url)
#
# my_name = soup.select_one(selector="#name")
# print("my_name: ", my_name)
#
# alla = soup.find_all("a")
# print("alla: ", alla, "\n\n")
#
# alla = soup.select("li a")
# print("alla: ", alla)
#
# form_tag = soup.find("input")
# max_length = form_tag.get("maxlength")
# print("max_length: ", max_length)
