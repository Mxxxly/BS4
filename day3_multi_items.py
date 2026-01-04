import requests
from bs4 import BeautifulSoup


# this is to find the length of a div or tag
# url = "https://books.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # To count the amount of the tags

# books = soup.find_all("article", class_="product_pod")
# # print(len(books))

# for book in books:
#     title = book.find("a")["title"]
#     price = book.find("p", class_="price_color").text
#     print(title, "-", price)


# url = "https://books.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# books = soup.find_all("article", class_="product_pod")

# for book in books:
#     title = book.find("a").get("title")
#     price = book.find("p", class_="price_color").text
#     print(title, "-", price)

# correct way to scrape the book titles and prices

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.find("h3").find("a").get("title")
    price = book.find("p", class_="price_color").text
    print(title, "-", price)




# Instead of just printing, let’s store.

# book_list = []

# for book in books:
#     title = book.find("a")["title"]
#     price = book.find("p", class_="price_color").text

#     book_data = {
#         "title": title,
#         "price": price
#     }

#     book_list.append(book_data)

# print(book_list)



# for book in books:
#     title_tag = book.find("a")
#     price_tag = book.find("p", class_="price_color")

#     title = title_tag["title"] if title_tag else "No title"
#     price = price_tag.text if price_tag else "No price"

#     print(title, "-", price)