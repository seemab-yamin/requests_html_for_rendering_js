from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://react-amazon-bestsellers-books-dy.netlify.app/"

session = HTMLSession()
resp = session.get(url)
soup = BeautifulSoup(resp.text, "lxml")

# will be none as we haven't render the js till yet
print(soup.find_all("article", class_="book"))

# render js
resp.html.render()

# get article elements
print(resp.html.find("article.book"))

# parse rendered html to the soup
soup = BeautifulSoup(resp.html.html, "lxml")

# get all books as rendered by page
books = soup.find_all("article", class_="book")

# traverse each book
for book in books:
    print(book.find("h2").text)

# TODO
# Read documentation: https://requests.readthedocs.io/projects/requests-html/en/latest/
