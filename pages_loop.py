import re
import requests
from bs4 import BeautifulSoup


page = 1

while True:
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    if response.status_code != 200:
        break  # stop if page doesn't exist

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    if not books:
        break  # no books = stop pagination

    print(f"\n📘 Page {page} — {len(books)} books found")

    for book in books:
        title = book.find("h3").find("a").get("title")
        price = book.find("p", class_="price_color").text
        print(title, "-", price)


    
    if page == 2:  # limit to first 3 pages for demo
        print(f'reached limit page:{page} stopping here')
        break

    page += 1

  
