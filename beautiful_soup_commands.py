from bs4 import BeautifulSoup

with open("html_file.html") as f:
    soup = BeautifulSoup(f,'html.parser')
    
# print(soup.prettify())
#print(soup.title)
#print(soup.title.name)
#print(soup.title.text)
#print(soup.title.string)
#print(soup.p)

#print(soup.p["class"])
# print(soup.a["href"])
#print(soup.findAll('a'))
#print(soup.find("a"))
# for link in soup.find_all("a"):
#     print(link.get("href"))
# print(soup.a["href"])
# 
# for link in soup.find_all("a"):
#     print(link["href"])
# print(soup.get_text())
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(css_soup.p["class"])