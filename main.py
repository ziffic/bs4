from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

titles = soup.select(".titleline a")
links = soup.select(".titleline a")
scores = soup.select(".score")

title_list = []
link_list = []
score_list = []

for title in titles:
    if "." in title.text:
        continue
    title_list.append(title.text)

for link in links:
    if "?" in link.get("href"):
        continue
    link_list.append(link.get("href"))

for score in scores:
    points = score.getText()
    score_list.append(int(points.split()[0]))

max_score = max(score_list)
max_index = score_list.index(max_score)

print(f"""
1. {title_list[max_index]}\n
2. {link_list[max_index]}\n
3. {score_list[max_index]}\n
""")

# ------------------------------------------------------------------------------
# BEAUTIFUL SOUP BASICS
# ------------------------------------------------------------------------------

# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.getText())

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# section_heading = soup.find(name="h3")
# print(section_heading.get("class"))
